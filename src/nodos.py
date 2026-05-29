"""Nodos para estruturas encadeadas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class NodoLista(Generic[T]):
    valor: T
    proximo: Optional["NodoLista[T]"] = None


@dataclass
class NodoFila(Generic[T]):
    valor: T
    proximo: Optional["NodoFila[T]"] = None
