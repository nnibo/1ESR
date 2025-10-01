
from typing import List, Optional, Tuple, Dict, Any
from pymongo.database import Database

from app.models.curso import CursoCreate, CursoUpdate
from app.utils.io import mongo_to_out, oid_or_400

COL = "cursos"

class CursosService:
    def __init__(self, db: Database):
        self.col = db[COL]

    def create(self, data: CursoCreate) -> Dict[str, Any]:
        doc = data.model_dump()
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

    def update_partial(self, id: str, patch: CursoUpdate) -> Optional[Dict[str, Any]]:
        data = patch.model_dump(exclude_none=True)
        self.col.update_one({"_id": oid_or_400(id)}, {"$set": data})
        doc = self.col.find_one({"_id": oid_or_400(id)})
        return mongo_to_out(doc) if doc else None

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": oid_or_400(id)})
        return res.deleted_count == 1
