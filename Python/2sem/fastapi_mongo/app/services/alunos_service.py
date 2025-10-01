
from typing import List, Optional, Tuple, Dict, Any
from pymongo.database import Database
from bson import ObjectId

from app.models.aluno import AlunoCreate, AlunoUpdate
from app.utils.io import oid_or_400, mongo_to_out

COL = "alunos"

class AlunosService:
    def __init__(self, db: Database):
        self.col = db[COL]

    def create(self, data: AlunoCreate) -> Dict[str, Any]:
        doc = data.model_dump()
        doc["curso_ids"] = [oid_or_400(cid) for cid in doc.get("curso_ids", [])]
        res = self.col.insert_one(doc)
        created = self.col.find_one({"_id": res.inserted_id})
        return mongo_to_out(created)

    def get_by_id(self, id: str) -> Optional[Dict[str, Any]]:
        doc = self.col.find_one({"_id": oid_or_400(id)})
        return mongo_to_out(doc) if doc else None

    def list(self, skip: int = 0, limit: int = 20) -> Tuple[List[Dict[str, Any]], int]:
        cursor = self.col.find().skip(skip).limit(limit)
        items = [mongo_to_out(d) for d in cursor]
        total = self.col.count_documents({})
        return items, total

    def update_partial(self, id: str, patch: AlunoUpdate) -> Optional[Dict[str, Any]]:
        data = patch.model_dump(exclude_none=True)
        if "curso_ids" in data:
            data["curso_ids"] = [oid_or_400(cid) for cid in data["curso_ids"]]
        self.col.update_one({"_id": oid_or_400(id)}, {"$set": data})
        doc = self.col.find_one({"_id": oid_or_400(id)})
        return mongo_to_out(doc) if doc else None

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": oid_or_400(id)})
        return res.deleted_count == 1

    def matricular(self, aluno_id: str, curso_id: str) -> Optional[Dict[str, Any]]:
        self.col.update_one({"_id": oid_or_400(aluno_id)}, {"$addToSet": {"curso_ids": oid_or_400(curso_id)}})
        doc = self.col.find_one({"_id": oid_or_400(aluno_id)})
        return mongo_to_out(doc) if doc else None
