# Figurinhas da Copa - Projeto de Estrutura de Dados

Este projeto implementa um sistema de gerenciamento de figurinhas da Copa do Mundo para a disciplina de Estrutura de Dados (Fatec Rio Claro). O foco principal é aplicar estruturas encadeadas próprias, sem depender de estruturas prontas para os componentes exigidos no enunciado.

## Visão rápida

O sistema permite:

- Cadastrar colecionadores
- Inserir figurinhas no álbum
- Armazenar figurinhas repetidas
- Buscar por número, jogador e seleção
- Registrar propostas de troca
- Processar trocas automaticamente
- Manter histórico de operações
- Salvar e carregar dados em JSON

## Requisitos do ambiente

- Python 3.10 ou superior
- Pytest (para rodar os testes)

## Como executar

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Execute o menu interativo:

python -m src.main

## Como rodar os testes

pytest -q

## Estrutura do projeto

- [src](src): código-fonte principal
- [tests](tests): testes automatizados
- [PLAN.md](PLAN.md): plano de implementação
- [Projeto3.pdf](Projeto3.pdf): enunciado do trabalho

## Tecnologias e abordagem

- Linguagem: Python
- Estruturas exigidas implementadas manualmente com nodos encadeados
- Arquitetura separada por domínio, regras de negócio, persistência e interface CLI

## Status atual

- Implementação principal concluída
- Testes automatizados cobrindo fluxos essenciais
- Suite de testes passando localmente

## Para convidados e avaliadores

Se você está conhecendo o projeto agora, siga esta ordem:

1. Leia o escopo em [Projeto3.pdf](Projeto3.pdf).
2. Veja o plano em [PLAN.md](PLAN.md).
3. Execute o sistema com python -m src.main.
4. Rode os testes com pytest -q.

## Contribuição

Contribuições são bem-vindas para melhorias de código, testes e documentação.

## Licença

[MIT](LICENSE)
