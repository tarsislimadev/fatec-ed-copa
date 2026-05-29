from src.figurinha import Figurinha
from src.sistema import SistemaFigurinhas


def test_repetidas_e_troca_automatica() -> None:
    sistema = SistemaFigurinhas(total_album=10)
    sistema.cadastrar_colecionador("Ana")
    sistema.cadastrar_colecionador("Bia")

    sistema.inserir_figurinha("Ana", Figurinha(1, "Messi", "Argentina"))
    sistema.inserir_figurinha("Ana", Figurinha(1, "Messi", "Argentina"))
    sistema.inserir_figurinha("Bia", Figurinha(2, "Neymar", "Brasil"))
    sistema.inserir_figurinha("Bia", Figurinha(2, "Neymar", "Brasil"))

    sistema.registrar_proposta_troca("Ana", "Bia", 1, 2)
    assert sistema.processar_proxima_troca() is True

    ana = sistema.obter_colecionador("Ana")
    bia = sistema.obter_colecionador("Bia")

    assert ana.album.consultar_por_numero(2) is not None
    assert bia.album.consultar_por_numero(1) is not None


def test_troca_falha_sem_repetidas() -> None:
    sistema = SistemaFigurinhas(total_album=10)
    sistema.cadastrar_colecionador("Ana")
    sistema.cadastrar_colecionador("Bia")

    sistema.registrar_proposta_troca("Ana", "Bia", 10, 20)
    assert sistema.processar_proxima_troca() is False
