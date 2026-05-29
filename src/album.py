"""Estrutura de album com lista encadeada."""

from __future__ import annotations

from typing import Iterator, Optional

from .figurinha import Figurinha
from .nodos import NodoLista


class Album:
    def __init__(self, total_esperado: int = 700) -> None:
        if total_esperado <= 0:
            raise ValueError("Total esperado deve ser positivo.")
        self.cabeca: Optional[NodoLista[Figurinha]] = None
        self.tamanho = 0
        self.total_esperado = total_esperado

    def inserir(self, figurinha: Figurinha) -> bool:
        if self.consultar_por_numero(figurinha.numero) is not None:
            return False

        novo = NodoLista(valor=figurinha)
        if self.cabeca is None:
            self.cabeca = novo
            self.tamanho += 1
            return True

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo
        self.tamanho += 1
        return True

    def remover(self, numero: int) -> Optional[Figurinha]:
        atual = self.cabeca
        anterior: Optional[NodoLista[Figurinha]] = None

        while atual is not None:
            if atual.valor.numero == numero:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.valor
            anterior = atual
            atual = atual.proximo

        return None

    def consultar_por_numero(self, numero: int) -> Optional[Figurinha]:
        atual = self.cabeca
        while atual is not None:
            if atual.valor.numero == numero:
                return atual.valor
            atual = atual.proximo
        return None

    def buscar_por_jogador(self, jogador: str) -> tuple[Figurinha, ...]:
        alvo = jogador.strip().lower()
        achados: tuple[Figurinha, ...] = tuple()
        atual = self.cabeca
        while atual is not None:
            if alvo in atual.valor.jogador.lower():
                achados = (*achados, atual.valor)
            atual = atual.proximo
        return achados

    def buscar_por_selecao(self, selecao: str) -> tuple[Figurinha, ...]:
        alvo = selecao.strip().lower()
        achados: tuple[Figurinha, ...] = tuple()
        atual = self.cabeca
        while atual is not None:
            if alvo in atual.valor.selecao.lower():
                achados = (*achados, atual.valor)
            atual = atual.proximo
        return achados

    def porcentagem_concluida(self) -> float:
        return (self.tamanho / self.total_esperado) * 100

    def __len__(self) -> int:
        return self.tamanho

    def __iter__(self) -> Iterator[Figurinha]:
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo
