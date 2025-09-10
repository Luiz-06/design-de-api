from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from datetime import date, time

# Cria uma instância da nossa API. 
app = FastAPI()

# Define as categorias que nos vamos usar.
class Categoria(str, Enum):
    iniciante = "iniciante"
    amador = "amador"
    profissional = "profissional"

# Esse é o modelo de dados de uma partida.
# Ele diz quais informações uma partida deve ter (ID, nome, data, etc.).
class Partida(BaseModel):
    id_partida: int
    id_adm: int
    nome_partida: str
    local_partida: str
    horario_partida: time
    data_partida: date
    categoria_partida: Categoria
    id_participantes: list[int] = []

# Esse é o modelo de dados de um jogador.
# Ele define as informações de cada pessoa que joga.
class Jogador(BaseModel):
    id_jogador: int
    nome_jogador: str
    categoria_jogador: Categoria
    fone_jogador: int
    avaliacao_jogador: int

# Nosso "banco de dados" de jogadores, que é só uma lista de objetos.
jogadores_db = [
    Jogador(
        id_jogador=1,
        nome_jogador="João Vitor",
        categoria_jogador=Categoria.iniciante,
        fone_jogador=999999999,
        avaliacao_jogador=8,
    ),
    Jogador(
        id_jogador=2,
        nome_jogador="Maria Luiza",
        categoria_jogador=Categoria.amador,
        fone_jogador=888888888,
        avaliacao_jogador=7,
    ),
    Jogador(
        id_jogador=3,
        nome_jogador="Carlos Henrique",
        categoria_jogador=Categoria.profissional,
        fone_jogador=777777777,
        avaliacao_jogador=9,
    ),
    Jogador(
        id_jogador=4,
        nome_jogador="Ana Paula",
        categoria_jogador=Categoria.amador,
        fone_jogador=666666666,
        avaliacao_jogador=8,
    ),
    Jogador(
        id_jogador=5,
        nome_jogador="Pedro Santos",
        categoria_jogador=Categoria.iniciante,
        fone_jogador=555555555,
        avaliacao_jogador=6,
    ),
    Jogador(
        id_jogador=6,
        nome_jogador="Mariana Lima",
        categoria_jogador=Categoria.profissional,
        fone_jogador=444444444,
        avaliacao_jogador=10,
    ),
    Jogador(
        id_jogador=7,
        nome_jogador="Felipe Costa",
        categoria_jogador=Categoria.iniciante,
        fone_jogador=333333333,
        avaliacao_jogador=7,
    ),
]

# Nosso "banco de dados" de partidas, também uma lista de objetos.
partidas_db = [
    Partida(
        id_partida=1,
        id_adm=1,
        nome_partida="teste",
        id_participantes=[1],
        local_partida="Quadra Municipal",
        horario_partida=time.fromisoformat("19:00"),
        data_partida=date.fromisoformat("2025-09-15"),
        categoria_partida=Categoria.iniciante,
    ),
    Partida(
        id_partida=2,
        id_adm=2,
        nome_partida="Desafio Amador",
        id_participantes=[2],
        local_partida="Clube do Bairro",
        horario_partida=time.fromisoformat("20:30"),
        data_partida=date.fromisoformat("2025-09-18"),
        categoria_partida=Categoria.amador,
    ),
    Partida(
        id_partida=3,
        id_adm=4,
        nome_partida="Copa Profissional",
        id_participantes=[6],
        local_partida="Ginásio Central",
        horario_partida=time.fromisoformat("21:00"),
        data_partida=date.fromisoformat("2025-09-20"),
        categoria_partida=Categoria.profissional,
    ),
    Partida(
        id_partida=4,
        id_adm=1,
        nome_partida="Jogo de Treino",
        id_participantes=[5],
        local_partida="Quadra da Praça",
        horario_partida=time.fromisoformat("18:30"),
        data_partida=date.fromisoformat("2025-09-16"),
        categoria_partida=Categoria.iniciante,
    ),
    Partida(
        id_partida=5,
        id_adm=2,
        nome_partida="Amistoso do Fim de Semana",
        id_participantes=[4],
        local_partida="Clube do Bairro",
        horario_partida=time.fromisoformat("10:00"),
        data_partida=date.fromisoformat("2025-09-22"),
        categoria_partida=Categoria.amador,
    ),
]

# Rota de boas-vindas. Simples assim.
# Não precisa de nenhum parâmetro.
@app.get("/")
def helloWorld():
    return "Vôlei do Rogério !!!"


# Essa rota é para um jogador se inscrever em uma partida.
# Ela precisa de dois **querry parameters** na URL: `id_partida` e `id_jogador`.
@app.post("/partidas/inscrever")
def inscreverPartida(id_partida: int, id_jogador: int):
    partida_encontrada = None
    for partida in partidas_db:
        if partida.id_partida == id_partida:
            partida_encontrada = partida
            break

    if not partida_encontrada:
        raise HTTPException(status_code=404, detail="Partida não encontrada.")

    jogador_encontrado = None
    for jogador in jogadores_db:
        if jogador.id_jogador == id_jogador:
            jogador_encontrado = jogador
            break
    
    if not jogador_encontrado:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")

    if jogador_encontrado.categoria_jogador != partida_encontrada.categoria_partida:
        raise HTTPException(status_code=400, detail="Categoria do jogador não é compatível com a categoria da partida.")

    if id_jogador in partida_encontrada.id_participantes:
        raise HTTPException(status_code=400, detail="Jogador já está inscrito nesta partida.")

    partida_encontrada.id_participantes.append(id_jogador)

    return {"mensagem": f"Jogador {id_jogador} inscrito com sucesso na partida {id_partida}."}


# Essa rota cria uma nova partida.
# Ela espera os dados da partida (um JSON) no **body parameter**.
@app.post("/partidas")
def criarPartida(nova_partida: Partida): 
    for partida_existente in partidas_db:
        if partida_existente.id_partida == nova_partida.id_partida:
            raise HTTPException(status_code=400, detail="Partida com este ID já existe.")
    partidas_db.append(nova_partida)
    return {"mensagem": "Partida criada com sucesso!", "partida_criada": nova_partida}


# Rota para pegar a lista completa de todas as partidas.
# Não precisa de nenhum parâmetro.
@app.get("/partidas")
def listarPartidas():
    return partidas_db


# Rota para buscar uma partida específica usando o ID.
# O `id_partida` é um **path parameter** que vai na própria URL.
@app.get("/partidas/id/{id_partida}")
def partidaId(id_partida: int):
    for partida in partidas_db:
        if partida.id_partida == id_partida:
            return partida
    raise HTTPException(status_code=404, detail="Partida não encontrada")


# Rota para buscar uma partida pelo nome dela.
# O `nome_partida` é um **path parameter** que também vai na URL.
@app.get("/partidas/nome/{nome_partida}")
def partidaNome(nome_partida: str):
    for partida in partidas_db:
        if partida.nome_partida == nome_partida:
            return partida
    raise HTTPException(status_code=404, detail="Partida não encontrada")


# Rota para buscar partidas por categoria.
# A `categoria_partida` é um **path parameter** que você coloca na URL.
@app.get("/partidas/categoria/{categoria_partida}")
def partidaCategoria(categoria_partida: Categoria):
    partidas_encontradas = [p for p in partidas_db if p.categoria_partida == categoria_partida]
    if partidas_encontradas:
        return partidas_encontradas
    raise HTTPException(status_code=404, detail="Partida não encontrada")


# Rota para deletar uma partida pelo ID.
# O `id_partida` é um **path parameter** que você passa na URL.
@app.delete("/partidas/{id_partida}")
def excluirPartida(id_partida: int):
    for i, partida in enumerate(partidas_db):
        if partida.id_partida == id_partida:
            del partidas_db[i]
            return {"mensagem": f"Partida com ID {id_partida} excluída com sucesso."}
    raise HTTPException(status_code=404, detail="Partida não encontrada.")


# Essa rota cria um novo jogador.
# Ela espera os dados do jogador (um JSON) no **body parameter**.
@app.post("/jogadores")
def criarJogador(novo_jogador: Jogador): 
    for jogador_existente in jogadores_db:
        if jogador_existente.id_jogador == novo_jogador.id_jogador:
            raise HTTPException(status_code=400, detail="Jogador com este ID já existe.")
    jogadores_db.append(novo_jogador)
    return {"mensagem": "Jogador criado com sucesso!", "jogador_criado": novo_jogador}


# Rota para encontrar um jogador pelo ID.
# O `id_jogador` é um **path parameter** que vai na URL.
@app.get("/jogadores/id/{id_jogador}")
def jogadorId(id_jogador: int):
    for jogador in jogadores_db:
        if jogador.id_jogador == id_jogador:
            return jogador
    raise HTTPException(status_code=404, detail="Jogador não encontrado")
    

# Rota para encontrar um jogador pelo nome.
# O `nome_jogador` é um **path parameter** que vai na URL.
@app.get("/jogadores/nome/{nome_jogador}")
def jogadorNome(nome_jogador: str):
    for jogador in jogadores_db:
        if jogador.nome_jogador == nome_jogador:
            return jogador
    raise HTTPException(status_code=404, detail="Jogador não encontrado")
