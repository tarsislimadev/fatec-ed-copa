"""Funcoes de validacao de entrada do dominio."""

from __future__ import annotations


def validar_numero_figurinha(numero: int) -> None:
    if not isinstance(numero, int):
        raise ValueError("Numero da figurinha deve ser inteiro.")
    if numero <= 0:
        raise ValueError("Numero da figurinha deve ser positivo.")


def validar_texto_nao_vazio(valor: str, campo: str) -> None:
    if not isinstance(valor, str):
        raise ValueError(f"{campo} deve ser texto.")
    if not valor.strip():
        raise ValueError(f"{campo} nao pode ser vazio.")
