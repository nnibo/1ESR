
from fastapi import FastAPI
from routers.alunos_controller import router as alunos_router
from routers.cursos_controller import router as cursos_router

app = FastAPI(title="API Escola (Sync Clean)")

app.include_router(alunos_router)
app.include_router(cursos_router)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
