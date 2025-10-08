from pydantic import BaseModel
from enum import Enum
from datetime import date, time


class Categoria(str, Enum):
    iniciante = "iniciante"
    amador = "amador"
    profissional = "profissional"


class Partida(BaseModel):
    id_partida: int
    id_adm: int
    nome_partida: str
    local_partida: str
    horario_partida: time
    data_partida: date
    categoria_partida: Categoria
    id_participantes: list[int] = []


class Jogador(BaseModel):
    id_jogador: int
    nome_jogador: str
    categoria_jogador: Categoria
    fone_jogador: int
    avaliacao_jogador: int