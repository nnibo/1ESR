
from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.db import get_db
from app.models.curso import CursoCreate, CursoUpdate
from app.services.cursos_service import CursosService

router = APIRouter(prefix="/cursos", tags=["cursos"])

def svc_dep(db = Depends(get_db)) -> CursosService:
    return CursosService(db)

@router.post("", status_code=status.HTTP_201_CREATED)
def criar_curso(payload: CursoCreate, svc: CursosService = Depends(svc_dep)):
    return svc.create(payload)

@router.get("")
def listar_cursos(skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), svc: CursosService = Depends(svc_dep)):
    items, total = svc.list(skip, limit)
    return {"items": items, "total": total, "skip": skip, "limit": limit}

@router.get("/{id}")
def obter_curso(id: str, svc: CursosService = Depends(svc_dep)):
    curso = svc.get_by_id(id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.patch("/{id}")
def atualizar_curso(id: str, patch: CursoUpdate, svc: CursosService = Depends(svc_dep)):
    curso = svc.update_partial(id, patch)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_curso(id: str, svc: CursosService = Depends(svc_dep)):
    ok = svc.delete(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
