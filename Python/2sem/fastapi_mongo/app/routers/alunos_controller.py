
from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.db import get_db
from app.models.aluno import AlunoCreate, AlunoUpdate
from app.services.alunos_service import AlunosService

router = APIRouter(prefix="/alunos", tags=["alunos"])

def svc_dep(db = Depends(get_db)) -> AlunosService:
    return AlunosService(db)

@router.post("", status_code=status.HTTP_201_CREATED)
def criar_aluno(payload: AlunoCreate, svc: AlunosService = Depends(svc_dep)):
    return svc.create(payload)

@router.get("")
def listar_alunos(skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100), svc: AlunosService = Depends(svc_dep)):
    items, total = svc.list(skip, limit)
    return {"items": items, "total": total, "skip": skip, "limit": limit}

@router.get("/{id}")
def obter_aluno(id: str, svc: AlunosService = Depends(svc_dep)):
    aluno = svc.get_by_id(id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.patch("/{id}")
def atualizar_aluno(id: str, patch: AlunoUpdate, svc: AlunosService = Depends(svc_dep)):
    aluno = svc.update_partial(id, patch)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_aluno(id: str, svc: AlunosService = Depends(svc_dep)):
    ok = svc.delete(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

@router.patch("/{id}/matricular")
def matricular_em_curso(id: str, curso_id: str, svc: AlunosService = Depends(svc_dep)):
    aluno = svc.matricular(id, curso_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno
