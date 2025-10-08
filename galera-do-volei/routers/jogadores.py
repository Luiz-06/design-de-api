from fastapi import APIRouter, HTTPException
from .. import schemas, database


router = APIRouter(
    prefix="/jogadores",
    tags=["Jogadores"]
)


@router.post("/", response_model=schemas.Jogador)
def criar_jogador(novo_jogador: schemas.Jogador):
    if database.get_jogador_por_id(novo_jogador.id_jogador):
        raise HTTPException(status_code=400, detail="Jogador com este ID já existe.")
    
    database.criar_novo_jogador(novo_jogador)
    return novo_jogador


@router.get("/", response_model=list[schemas.Jogador])
def listar_todos_jogadores():
    return database.get_todos_jogadores()


@router.get("/id/{id_jogador}", response_model=schemas.Jogador)
def buscar_jogador_por_id(id_jogador: int):
    jogador = database.get_jogador_por_id(id_jogador)
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogador


@router.get("/nome/{nome_jogador}", response_model=schemas.Jogador)
def buscar_jogador_por_nome(nome_jogador: str):
    jogador = database.get_jogador_por_nome(nome_jogador)
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogador