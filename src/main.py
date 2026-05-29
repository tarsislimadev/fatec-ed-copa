"""Interface de linha de comando do projeto."""

from __future__ import annotations

from .figurinha import Figurinha
from .persistencia import carregar_json, salvar_json
from .sistema import SistemaFigurinhas


def ler_int(mensagem: str) -> int:
    valor = input(mensagem).strip()
    return int(valor)


def imprimir_menu() -> None:
    print("\n=== Album da Copa ===")
    print("1. Cadastrar colecionador")
    print("2. Inserir figurinha")
    print("3. Consultar figurinha por numero")
    print("4. Ver album completo")
    print("5. Ver porcentagem concluida")
    print("6. Ver repetidas")
    print("7. Buscar por jogador")
    print("8. Buscar por selecao")
    print("9. Registrar proposta de troca")
    print("10. Processar proxima troca")
    print("11. Ver historico")
    print("12. Salvar em JSON")
    print("13. Carregar de JSON")
    print("0. Sair")


def executar() -> None:
    sistema = SistemaFigurinhas(total_album=100)

    while True:
        imprimir_menu()
        try:
            opcao = ler_int("Escolha uma opcao: ")
        except ValueError:
            print("Opcao invalida.")
            continue

        try:
            if opcao == 0:
                print("Encerrando.")
                break

            if opcao == 1:
                nome = input("Nome do colecionador: ")
                sistema.cadastrar_colecionador(nome)
                print("Colecionador cadastrado.")

            elif opcao == 2:
                nome = input("Nome do colecionador: ")
                numero = ler_int("Numero da figurinha: ")
                jogador = input("Nome do jogador: ")
                selecao = input("Selecao: ")
                destino = sistema.inserir_figurinha(nome, Figurinha(numero, jogador, selecao))
                if destino == "album":
                    print("Figurinha inserida no album.")
                else:
                    print("Figurinha repetida armazenada.")

            elif opcao == 3:
                nome = input("Nome do colecionador: ")
                numero = ler_int("Numero da figurinha: ")
                figurinha = sistema.obter_colecionador(nome).album.consultar_por_numero(numero)
                if figurinha is None:
                    print("Figurinha nao encontrada.")
                else:
                    print(f"#{figurinha.numero} - {figurinha.jogador} ({figurinha.selecao})")

            elif opcao == 4:
                nome = input("Nome do colecionador: ")
                album = sistema.obter_colecionador(nome).album
                if len(album) == 0:
                    print("Album vazio.")
                for figurinha in album:
                    print(f"#{figurinha.numero} - {figurinha.jogador} ({figurinha.selecao})")

            elif opcao == 5:
                nome = input("Nome do colecionador: ")
                porcentagem = sistema.obter_colecionador(nome).album.porcentagem_concluida()
                print(f"Album concluido: {porcentagem:.2f}%")

            elif opcao == 6:
                nome = input("Nome do colecionador: ")
                repetidas = sistema.obter_colecionador(nome).listar_repetidas()
                print(f"Total repetidas: {len(repetidas)}")
                for figurinha in repetidas:
                    print(f"#{figurinha.numero} - {figurinha.jogador} ({figurinha.selecao})")

            elif opcao == 7:
                nome = input("Nome do colecionador: ")
                termo = input("Jogador: ")
                resultados = sistema.obter_colecionador(nome).album.buscar_por_jogador(termo)
                print(f"Encontradas: {len(resultados)}")
                for figurinha in resultados:
                    print(f"#{figurinha.numero} - {figurinha.jogador} ({figurinha.selecao})")

            elif opcao == 8:
                nome = input("Nome do colecionador: ")
                termo = input("Selecao: ")
                resultados = sistema.obter_colecionador(nome).album.buscar_por_selecao(termo)
                print(f"Encontradas: {len(resultados)}")
                for figurinha in resultados:
                    print(f"#{figurinha.numero} - {figurinha.jogador} ({figurinha.selecao})")

            elif opcao == 9:
                a = input("Colecionador A: ")
                b = input("Colecionador B: ")
                numero_a = ler_int("Numero oferecido por A: ")
                numero_b = ler_int("Numero oferecido por B: ")
                sistema.registrar_proposta_troca(a, b, numero_a, numero_b)
                print("Proposta registrada.")

            elif opcao == 10:
                if sistema.processar_proxima_troca():
                    print("Troca efetuada com sucesso.")
                else:
                    print("Nao foi possivel efetuar a troca.")

            elif opcao == 11:
                if len(sistema.historico) == 0:
                    print("Historico vazio.")
                for evento in sistema.historico:
                    print(f"{evento.timestamp} [{evento.tipo}] {evento.mensagem}")

            elif opcao == 12:
                caminho = input("Caminho do arquivo JSON: ").strip()
                salvar_json(caminho, sistema)
                print("Dados salvos.")

            elif opcao == 13:
                caminho = input("Caminho do arquivo JSON: ").strip()
                sistema = carregar_json(caminho)
                print("Dados carregados.")

            else:
                print("Opcao invalida.")

        except ValueError as erro:
            print(f"Erro de validacao: {erro}")
        except FileNotFoundError as erro:
            print(str(erro))


if __name__ == "__main__":
    executar()
