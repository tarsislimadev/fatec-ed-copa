"""Regras de negocio para colecionadores, repetidas e trocas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .album import Album
from .fila import Fila
from .figurinha import Figurinha
from .historico import Historico
from .validacao import validar_texto_nao_vazio


@dataclass(frozen=True)
class PropostaTroca:
    colecionador_a: str
    colecionador_b: str
    numero_a: int
    numero_b: int

    def to_dict(self) -> dict:
        return {
            "colecionador_a": self.colecionador_a,
            "colecionador_b": self.colecionador_b,
            "numero_a": self.numero_a,
            "numero_b": self.numero_b,
        }

    @staticmethod
    def from_dict(data: dict) -> "PropostaTroca":
        return PropostaTroca(
            colecionador_a=str(data["colecionador_a"]),
            colecionador_b=str(data["colecionador_b"]),
            numero_a=int(data["numero_a"]),
            numero_b=int(data["numero_b"]),
        )


class Colecionador:
    def __init__(self, nome: str, total_album: int = 100) -> None:
        validar_texto_nao_vazio(nome, "Nome")
        self.nome = nome.strip()
        self.album = Album(total_esperado=total_album)
        self.repetidas: Fila[Figurinha] = Fila()

    def receber_figurinha(self, figurinha: Figurinha) -> str:
        if self.album.inserir(figurinha):
            return "album"
        self.repetidas.enqueue(figurinha)
        return "repetida"

    def possui_repetida(self, numero: int) -> bool:
        for figurinha in self.repetidas:
            if figurinha.numero == numero:
                return True
        return False

    def remover_repetida(self, numero: int) -> Optional[Figurinha]:
        if self.repetidas.esta_vazia():
            return None

        auxiliar: Fila[Figurinha] = Fila()
        removida: Optional[Figurinha] = None

        while not self.repetidas.esta_vazia():
            atual = self.repetidas.dequeue()
            if removida is None and atual.numero == numero:
                removida = atual
                continue
            auxiliar.enqueue(atual)

        self.repetidas = auxiliar
        return removida

    def listar_repetidas(self) -> tuple[Figurinha, ...]:
        return tuple(self.repetidas)


class SistemaFigurinhas:
    def __init__(self, total_album: int = 100) -> None:
        self.total_album = total_album
        self.colecionadores: dict[str, Colecionador] = {}
        self.propostas: Fila[PropostaTroca] = Fila()
        self.historico = Historico()

    def cadastrar_colecionador(self, nome: str) -> None:
        validar_texto_nao_vazio(nome, "Nome")
        chave = nome.strip().lower()
        if chave in self.colecionadores:
            raise ValueError("Colecionador ja cadastrado.")
        self.colecionadores[chave] = Colecionador(nome=nome.strip(), total_album=self.total_album)
        self.historico.registrar("cadastro", f"Colecionador {nome.strip()} cadastrado.")

    def obter_colecionador(self, nome: str) -> Colecionador:
        chave = nome.strip().lower()
        colecionador = self.colecionadores.get(chave)
        if colecionador is None:
            raise ValueError("Colecionador nao encontrado.")
        return colecionador

    def inserir_figurinha(self, nome: str, figurinha: Figurinha) -> str:
        colecionador = self.obter_colecionador(nome)
        destino = colecionador.receber_figurinha(figurinha)
        if destino == "album":
            self.historico.registrar(
                "insercao",
                f"{colecionador.nome} adicionou figurinha {figurinha.numero} ao album.",
            )
        else:
            self.historico.registrar(
                "repetida",
                f"{colecionador.nome} recebeu repetida {figurinha.numero}.",
            )
        return destino

    def registrar_proposta_troca(
        self,
        colecionador_a: str,
        colecionador_b: str,
        numero_a: int,
        numero_b: int,
    ) -> None:
        self.obter_colecionador(colecionador_a)
        self.obter_colecionador(colecionador_b)
        proposta = PropostaTroca(
            colecionador_a=colecionador_a.strip(),
            colecionador_b=colecionador_b.strip(),
            numero_a=numero_a,
            numero_b=numero_b,
        )
        self.propostas.enqueue(proposta)
        self.historico.registrar(
            "proposta_troca",
            (
                f"Proposta registrada: {proposta.colecionador_a}({proposta.numero_a}) "
                f"<-> {proposta.colecionador_b}({proposta.numero_b})."
            ),
        )

    def processar_proxima_troca(self) -> bool:
        if self.propostas.esta_vazia():
            return False

        proposta = self.propostas.dequeue()
        lado_a = self.obter_colecionador(proposta.colecionador_a)
        lado_b = self.obter_colecionador(proposta.colecionador_b)

        if not lado_a.possui_repetida(proposta.numero_a) or not lado_b.possui_repetida(proposta.numero_b):
            self.historico.registrar(
                "troca_falhou",
                (
                    f"Troca falhou: {proposta.colecionador_a}({proposta.numero_a}) "
                    f"<-> {proposta.colecionador_b}({proposta.numero_b})."
                ),
            )
            return False

        fig_a = lado_a.remover_repetida(proposta.numero_a)
        fig_b = lado_b.remover_repetida(proposta.numero_b)
        if fig_a is None or fig_b is None:
            self.historico.registrar("troca_falhou", "Troca falhou por inconsistencias de repetidas.")
            return False

        lado_a.receber_figurinha(fig_b)
        lado_b.receber_figurinha(fig_a)
        self.historico.registrar(
            "troca_sucesso",
            (
                f"Troca efetuada: {proposta.colecionador_a} recebeu {fig_b.numero} e "
                f"{proposta.colecionador_b} recebeu {fig_a.numero}."
            ),
        )
        return True

    def processar_todas_as_trocas(self) -> int:
        sucessos = 0
        while not self.propostas.esta_vazia():
            if self.processar_proxima_troca():
                sucessos += 1
        return sucessos
