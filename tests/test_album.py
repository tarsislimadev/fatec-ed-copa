from src.album import Album
from src.figurinha import Figurinha


def test_inserir_consultar_remover_album() -> None:
    album = Album(total_esperado=10)
    figurinha = Figurinha(7, "Messi", "Argentina")

    assert album.inserir(figurinha) is True
    assert album.inserir(figurinha) is False
    assert album.consultar_por_numero(7) == figurinha
    assert album.remover(7) == figurinha
    assert album.consultar_por_numero(7) is None


def test_buscas_e_porcentagem() -> None:
    album = Album(total_esperado=4)
    album.inserir(Figurinha(1, "Vinicius Jr", "Brasil"))
    album.inserir(Figurinha(2, "Rodrygo", "Brasil"))
    album.inserir(Figurinha(3, "Mbappe", "Franca"))

    assert len(album.buscar_por_jogador("vini")) == 1
    assert len(album.buscar_por_selecao("brasil")) == 2
    assert album.porcentagem_concluida() == 75.0
