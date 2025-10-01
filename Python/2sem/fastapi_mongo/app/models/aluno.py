
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr

class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    curso_ids: List[str] = Field(default_factory=list)  # strings na API

class AlunoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    curso_ids: Optional[List[str]] = None
