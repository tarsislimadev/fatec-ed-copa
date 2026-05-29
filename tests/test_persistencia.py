from pathlib import Path

from src.figurinha import Figurinha
from src.persistencia import carregar_json, salvar_json
from src.sistema import SistemaFigurinhas


def test_salvar_e_carregar_json(tmp_path: Path) -> None:
    arquivo = tmp_path / "dados.json"

    sistema = SistemaFigurinhas(total_album=10)
    sistema.cadastrar_colecionador("Ana")
    sistema.inserir_figurinha("Ana", Figurinha(11, "Kane", "Inglaterra"))

    salvar_json(str(arquivo), sistema)

    carregado = carregar_json(str(arquivo))
    ana = carregado.obter_colecionador("Ana")
    assert ana.album.consultar_por_numero(11) is not None
