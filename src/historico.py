"""Registro encadeado de eventos do sistema."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterator, Optional

from .nodos import NodoLista


@dataclass(frozen=True)
class EventoHistorico:
    timestamp: str
    tipo: str
    mensagem: str

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "tipo": self.tipo,
            "mensagem": self.mensagem,
        }

    @staticmethod
    def from_dict(data: dict) -> "EventoHistorico":
        return EventoHistorico(
            timestamp=str(data["timestamp"]),
            tipo=str(data["tipo"]),
            mensagem=str(data["mensagem"]),
        )


class Historico:
    def __init__(self) -> None:
        self.cabeca: Optional[NodoLista[EventoHistorico]] = None
        self.cauda: Optional[NodoLista[EventoHistorico]] = None
        self.tamanho = 0

    def registrar(self, tipo: str, mensagem: str) -> EventoHistorico:
        evento = EventoHistorico(
            timestamp=datetime.now().isoformat(timespec="seconds"),
            tipo=tipo,
            mensagem=mensagem,
        )
        self.adicionar_evento(evento)
        return evento

    def adicionar_evento(self, evento: EventoHistorico) -> None:
        nodo = NodoLista(valor=evento)
        if self.cauda is None:
            self.cabeca = nodo
            self.cauda = nodo
        else:
            self.cauda.proximo = nodo
            self.cauda = nodo
        self.tamanho += 1

    def __len__(self) -> int:
        return self.tamanho

    def __iter__(self) -> Iterator[EventoHistorico]:
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo
