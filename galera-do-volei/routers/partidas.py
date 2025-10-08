from fastapi import APIRouter, HTTPException
from .. import schemas, database

router = APIRouter(
    prefix="/partidas",
    tags=["Partidas"]
)


@router.post("/inscrever")
def inscrever_em_partida(id_partida: int, id_jogador: int):
    partida = database.get_partida_por_id(id_partida)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada.")

    jogador = database.get_jogador_por_id(id_jogador)
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")

    if jogador.categoria_jogador != partida.categoria_partida:
        raise HTTPException(status_code=400, detail="Categoria do jogador não é compatível com a categoria da partida.")

    if id_jogador in partida.id_participantes:
        raise HTTPException(status_code=400, detail="Jogador já está inscrito nesta partida.")

    partida.id_participantes.append(id_jogador)
    return {"mensagem": f"Jogador {jogador.nome_jogador} inscrito com sucesso na partida {partida.nome_partida}."}


@router.post("/", response_model=schemas.Partida)
def criar_partida(nova_partida: schemas.Partida):
    if database.get_partida_por_id(nova_partida.id_partida):
        raise HTTPException(status_code=400, detail="Partida com este ID já existe.")
    
    database.criar_nova_partida(nova_partida)
    return nova_partida


@router.get("/", response_model=list[schemas.Partida])
def listar_partidas():
    return database.get_todas_partidas()


@router.get("/id/{id_partida}", response_model=schemas.Partida)
def buscar_partida_por_id(id_partida: int):
    partida = database.get_partida_por_id(id_partida)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida


@router.get("/nome/{nome_partida}", response_model=schemas.Partida)
def buscar_partida_por_nome(nome_partida: str):
    partida = database.get_partida_por_nome(nome_partida)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida


@router.get("/categoria/{categoria_partida}", response_model=list[schemas.Partida])
def buscar_partidas_por_categoria(categoria_partida: schemas.Categoria):
    partidas_encontradas = database.get_partidas_por_categoria(categoria_partida)
    if not partidas_encontradas:
        raise HTTPException(status_code=404, detail=f"Nenhuma partida encontrada para a categoria '{categoria_partida.value}'")
    return partidas_encontradas


@router.delete("/{id_partida}")
def excluir_partida(id_partida: int):
    if not database.deletar_partida_por_id(id_partida):
        raise HTTPException(status_code=404, detail="Partida não encontrada.")
    return {"mensagem": f"Partida com ID {id_partida} excluída com sucesso."}