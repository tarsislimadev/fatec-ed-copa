"""Persistencia em JSON para estado do sistema."""

from __future__ import annotations

import json
from pathlib import Path

from .figurinha import Figurinha
from .historico import EventoHistorico
from .sistema import SistemaFigurinhas, PropostaTroca


def salvar_json(caminho: str, sistema: SistemaFigurinhas) -> None:
    dados = {
        "total_album": sistema.total_album,
        "colecionadores": {},
        "propostas": tuple(proposta.to_dict() for proposta in sistema.propostas),
        "historico": tuple(evento.to_dict() for evento in sistema.historico),
    }

    for chave, colecionador in sistema.colecionadores.items():
        dados["colecionadores"][chave] = {
            "nome": colecionador.nome,
            "album": tuple(figurinha.to_dict() for figurinha in colecionador.album),
            "repetidas": tuple(figurinha.to_dict() for figurinha in colecionador.repetidas),
        }

    destino = Path(caminho)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def carregar_json(caminho: str) -> SistemaFigurinhas:
    origem = Path(caminho)
    if not origem.exists():
        raise FileNotFoundError("Arquivo de persistencia nao encontrado.")

    dados = json.loads(origem.read_text(encoding="utf-8"))
    sistema = SistemaFigurinhas(total_album=int(dados["total_album"]))

    for chave, payload in dados["colecionadores"].items():
        sistema.cadastrar_colecionador(str(payload["nome"]))
        colecionador = sistema.colecionadores[chave]

        for item in payload["album"]:
            colecionador.album.inserir(Figurinha.from_dict(item))

        for item in payload["repetidas"]:
            colecionador.repetidas.enqueue(Figurinha.from_dict(item))

    sistema.historico = sistema.historico.__class__()
    for evento in dados["historico"]:
        evt = EventoHistorico.from_dict(evento)
        sistema.historico.adicionar_evento(evt)

    for item in dados["propostas"]:
        sistema.propostas.enqueue(PropostaTroca.from_dict(item))

    return sistema
