"""Implementacao de fila FIFO com nodos encadeados."""

from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

from .nodos import NodoFila

T = TypeVar("T")


class Fila(Generic[T]):
    def __init__(self) -> None:
        self.inicio: Optional[NodoFila[T]] = None
        self.fim: Optional[NodoFila[T]] = None
        self.tamanho = 0

    def esta_vazia(self) -> bool:
        return self.tamanho == 0

    def enqueue(self, valor: T) -> None:
        novo = NodoFila(valor=valor)
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def dequeue(self) -> T:
        if self.inicio is None:
            raise IndexError("Fila vazia.")

        removido = self.inicio
        self.inicio = removido.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return removido.valor

    def peek(self) -> T:
        if self.inicio is None:
            raise IndexError("Fila vazia.")
        return self.inicio.valor

    def limpar(self) -> None:
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self) -> int:
        return self.tamanho

    def __iter__(self) -> Iterator[T]:
        atual = self.inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo
