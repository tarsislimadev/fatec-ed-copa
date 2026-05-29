"""Entidade figurinha."""

from __future__ import annotations

from dataclasses import dataclass

from .validacao import validar_numero_figurinha, validar_texto_nao_vazio


@dataclass(frozen=True)
class Figurinha:
    numero: int
    jogador: str
    selecao: str

    def __post_init__(self) -> None:
        validar_numero_figurinha(self.numero)
        validar_texto_nao_vazio(self.jogador, "Jogador")
        validar_texto_nao_vazio(self.selecao, "Selecao")

    def to_dict(self) -> dict:
        return {
            "numero": self.numero,
            "jogador": self.jogador,
            "selecao": self.selecao,
        }

    @staticmethod
    def from_dict(data: dict) -> "Figurinha":
        return Figurinha(
            numero=int(data["numero"]),
            jogador=str(data["jogador"]),
            selecao=str(data["selecao"]),
        )
