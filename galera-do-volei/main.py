from fastapi import FastAPI
from .routers import partidas, jogadores

app = FastAPI(
    title="P2 - Galera do Vôlei API",
    description="Implementação da API para o projeto Galera do Vôlei.",
    version="1.0.0"
)


app.include_router(partidas.router)
app.include_router(jogadores.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"mensagem": "Vôlei do Rogério!!!"}