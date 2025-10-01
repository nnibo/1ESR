
from typing import Optional
from pydantic import BaseModel, Field

class CursoCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=120)
    descricao: Optional[str] = Field(default=None, max_length=500)

class CursoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=2, max_length=120)
    descricao: Optional[str] = Field(default=None, max_length=500)
