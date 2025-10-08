from datetime import date, time
from .schemas import Jogador, Partida, Categoria


_jogadores_db = [
    Jogador(id_jogador=1, nome_jogador="João Vitor", categoria_jogador=Categoria.iniciante, fone_jogador=999999999, avaliacao_jogador=8),
    Jogador(id_jogador=2, nome_jogador="Maria Luiza", categoria_jogador=Categoria.amador, fone_jogador=888888888, avaliacao_jogador=7),
    Jogador(id_jogador=3, nome_jogador="Carlos Henrique", categoria_jogador=Categoria.profissional, fone_jogador=777777777, avaliacao_jogador=9),
    Jogador(id_jogador=4, nome_jogador="Ana Paula", categoria_jogador=Categoria.amador, fone_jogador=666666666, avaliacao_jogador=8),
    Jogador(id_jogador=5, nome_jogador="Pedro Santos", categoria_jogador=Categoria.iniciante, fone_jogador=555555555, avaliacao_jogador=6),
    Jogador(id_jogador=6, nome_jogador="Mariana Lima", categoria_jogador=Categoria.profissional, fone_jogador=444444444, avaliacao_jogador=10),
    Jogador(id_jogador=7, nome_jogador="Felipe Costa", categoria_jogador=Categoria.iniciante, fone_jogador=333333333, avaliacao_jogador=7),
    Jogador(id_jogador=8, nome_jogador="Lucas Oliveira", categoria_jogador=Categoria.profissional, fone_jogador=222222222, avaliacao_jogador=9),
    Jogador(id_jogador=9, nome_jogador="Julia Martins", categoria_jogador=Categoria.amador, fone_jogador=111111111, avaliacao_jogador=8),
    Jogador(id_jogador=10, nome_jogador="Rafael Souza", categoria_jogador=Categoria.iniciante, fone_jogador=101010101, avaliacao_jogador=7),
]


_partidas_db = [
    Partida(id_partida=1, id_adm=1, nome_partida="Iniciantes da Manhã", id_participantes=[1, 5, 7], local_partida="Quadra Municipal", horario_partida=time.fromisoformat("09:00"), data_partida=date.fromisoformat("2025-10-15"), categoria_partida=Categoria.iniciante),
    Partida(id_partida=2, id_adm=2, nome_partida="Desafio Amador", id_participantes=[2, 4], local_partida="Clube do Bairro", horario_partida=time.fromisoformat("20:30"), data_partida=date.fromisoformat("2025-10-18"), categoria_partida=Categoria.amador),
    Partida(id_partida=3, id_adm=4, nome_partida="Copa Profissional", id_participantes=[6], local_partida="Ginásio Central", horario_partida=time.fromisoformat("21:00"), data_partida=date.fromisoformat("2025-10-20"), categoria_partida=Categoria.profissional),
    Partida(id_partida=4, id_adm=1, nome_partida="Jogo de Treino", id_participantes=[10], local_partida="Quadra da Praça", horario_partida=time.fromisoformat("18:30"), data_partida=date.fromisoformat("2025-10-16"), categoria_partida=Categoria.iniciante),
    Partida(id_partida=5, id_adm=2, nome_partida="Amistoso do Fim de Semana", id_participantes=[9], local_partida="Clube do Bairro", horario_partida=time.fromisoformat("10:00"), data_partida=date.fromisoformat("2025-10-22"), categoria_partida=Categoria.amador),
    Partida(id_partida=6, id_adm=3, nome_partida="Racha de Sexta", id_participantes=[3, 8], local_partida="Arena Vôlei", horario_partida=time.fromisoformat("19:30"), data_partida=date.fromisoformat("2025-10-24"), categoria_partida=Categoria.profissional),
]


## ******************* PARTIDAS ******************* ##
def get_todas_partidas():
    return _partidas_db


def get_partida_por_id(partida_id: int):
    for partida in _partidas_db:
        if partida.id_partida == partida_id:
            return partida
    return None


def get_partida_por_nome(nome: str):
    for partida in _partidas_db:
        if partida.nome_partida.lower() == nome.lower():
            return partida
    return None


def get_partidas_por_categoria(categoria: Categoria):
    return [p for p in _partidas_db if p.categoria_partida == categoria]


def criar_nova_partida(partida: Partida):
    _partidas_db.append(partida)
    return partida


def deletar_partida_por_id(partida_id: int):
    partida_encontrada = get_partida_por_id(partida_id)
    if partida_encontrada:
        _partidas_db.remove(partida_encontrada)
        return True
    return False


## ******************* JOGADORES ******************* ##
def get_todos_jogadores():
    return _jogadores_db


def get_jogador_por_id(jogador_id: int):
    for jogador in _jogadores_db:
        if jogador.id_jogador == jogador_id:
            return jogador
    return None


def get_jogador_por_nome(nome: str):
    for jogador in _jogadores_db:
        if jogador.nome_jogador.lower() == nome.lower():
            return jogador
    return None


def criar_novo_jogador(jogador: Jogador):
    _jogadores_db.append(jogador)
    return jogador