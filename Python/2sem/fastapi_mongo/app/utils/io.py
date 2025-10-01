
from typing import Dict, Any
from bson import ObjectId

def oid_or_400(v: str) -> ObjectId:
    from fastapi import HTTPException
    if not ObjectId.is_valid(v):
        raise HTTPException(status_code=400, detail="ObjectId inválido")
    return ObjectId(v)

def mongo_to_out(doc: Dict[str, Any]) -> Dict[str, Any]:
    if not doc:
        return doc
    out = dict(doc)
    _id = out.pop("_id", None)
    if isinstance(_id, ObjectId):
        out["id"] = str(_id)
    # Se tiver arrays de ObjectId
    for k, v in out.items():
        if isinstance(v, list) and v and isinstance(v[0], ObjectId):
            out[k] = [str(x) for x in v]
    return out
