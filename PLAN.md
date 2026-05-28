# Plano de Implementação - Projeto 3

## Objetivo

Implementar um sistema em Python para gerenciamento de figurinhas da Copa do Mundo, usando estruturas de dados próprias e sem recorrer a `list`, `deque` ou estruturas prontas para representar a lista encadeada e a fila do projeto.

## Escopo confirmado pelos arquivos do projeto

- Entidade principal: `Figurinha`.
- Estruturas auxiliares: `NodoLista` e `NodoFila`.
- Estrutura de coleção: `Album` com lista encadeada.
- Estrutura de apoio: `Fila` FIFO com `enqueue`, `dequeue`, `peek` e `limpar`.
- Registro de trocas e disputa de bafo: `Historico`.
- Funcionalidades esperadas:
  - inserir, remover, consultar e listar figurinhas do álbum;
  - calcular porcentagem concluída do álbum;
  - gerenciar repetidas;
  - buscar por número, jogador e seleção;
  - registrar e executar trocas;
  - persistir e carregar dados em TXT, CSV ou JSON;
  - tratar entradas inválidas.

## Premissas de implementação

- O projeto será implementado em Python.
- As estruturas centrais serão feitas manualmente com nós encadeados.
- O armazenamento em disco será feito com um formato simples e legível, preferencialmente JSON ou TXT, para facilitar carga e salvamento.
- A interface inicial pode ser em linha de comando, deixando o domínio isolado da apresentação.

## Modelo de domínio

### `Figurinha`
- Campos sugeridos: `id`, `nome`, `pais`, `posicao`, `raridade`.
- Responsabilidade: representar os dados de uma figurinha sem lógica de estrutura.

### `NodoLista`
- Campos sugeridos: `figurinha`, `proximo`.
- Responsabilidade: encadear elementos do álbum e das listas internas.

### `Album`
- Campos sugeridos: `cabeca`, `tamanho`.
- Responsabilidade: manter a lista encadeada e oferecer operações de inserção, remoção, busca e listagem.

### `NodoFila`
- Campos sugeridos: `figurinha`, `proximo`.
- Responsabilidade: armazenar um item na fila FIFO.

### `Fila`
- Campos sugeridos: `inicio`, `fim`, `tamanho`.
- Responsabilidade: controlar a fila de repetidas, propostas de troca ou eventos de histórico.

### `Historico`
- Responsabilidade: registrar operações relevantes como trocas, propostas e resultados.

## Estrutura sugerida do projeto

- `src/`
  - `figurinha.py`
  - `nodos.py`
  - `album.py`
  - `fila.py`
  - `historico.py`
  - `persistencia.py`
  - `validacao.py`
  - `main.py`
- `tests/`
- `docs/`

## Plano de execução

### Fase 1 - Base do domínio

1. Criar a classe `Figurinha`.
2. Criar os nós `NodoLista` e `NodoFila`.
3. Definir regras de validação para `id`, `pais`, `posicao` e `raridade`.

Critério de pronto:
- objetos instanciados com validação básica;
- sem uso de estruturas prontas para representar coleções internas.

### Fase 2 - Álbum com lista encadeada

1. Implementar inserção de figurinhas.
2. Implementar remoção por `id`.
3. Implementar busca por `id`, `nome/jogador` e `seleção/pais`.
4. Implementar listagem completa.
5. Implementar cálculo de progresso do álbum.

Critério de pronto:
- operações funcionam em cenários de coleção vazia, elemento único e múltiplos elementos;
- remoção atualiza corretamente a cabeça da lista e o tamanho.

### Fase 3 - Fila e repetidas

1. Implementar `Fila` com `enqueue`, `dequeue`, `peek` e `limpar`.
2. Usar fila para registrar figurinhas repetidas ou movimentações de troca.
3. Criar consultas para contar e listar repetidas.

Critério de pronto:
- a fila mantém ordem FIFO;
- remoção do início e atualização do fim estão corretas.

### Fase 4 - Trocas e histórico

1. Criar fluxo para registrar proposta de troca.
2. Verificar se ambos os lados possuem repetidas compatíveis.
3. Efetuar troca automática quando possível.
4. Registrar todas as ações relevantes em `Historico`.

Critério de pronto:
- toda troca fica auditável;
- o histórico preserva a sequência das operações.

### Fase 5 - Persistência

1. Definir o formato principal de persistência.
2. Implementar salvar e carregar estado do álbum, repetidas e histórico.
3. Garantir compatibilidade com o formato escolhido.

Critério de pronto:
- os dados são restaurados após reiniciar o programa;
- a serialização não depende de estruturas prontas para representar o domínio.

### Fase 6 - Interface e robustez

1. Criar menu simples para cadastro, busca, troca, consulta e persistência.
2. Tratar entradas inválidas com mensagens claras.
3. Cobrir casos de erro comuns: códigos inválidos, seleção inexistente, valores vazios e números fora do intervalo.

Critério de pronto:
- o usuário consegue completar os fluxos principais sem travar o programa;
- erros são tratados de forma previsível.

## Ordem de entrega sugerida

1. Estruturas base e álbum.
2. Fila e repetidas.
3. Trocas e histórico.
4. Persistência.
5. Interface, testes e ajustes finais.

## Testes mínimos

- Inserção e remoção no álbum.
- Busca por `id`, nome e seleção.
- Cálculo de porcentagem do álbum.
- Operações da fila FIFO.
- Registro e execução de trocas.
- Salvamento e carregamento dos dados.
- Validação de entradas inválidas.

## Riscos e cuidados

- Evitar uso de `list`, `deque` ou atalhos que invalidem a avaliação de estruturas de dados.
- Garantir separação entre domínio, persistência e interface.
- Manter nomes de campos e funções consistentes com o enunciado para facilitar a apresentação.
- Preferir implementação incremental com commits pequenos, como pede o enunciado.

## Próximos passos práticos

1. Criar os módulos base em `src/`.
2. Implementar `Figurinha`, `NodoLista`, `NodoFila`, `Album` e `Fila`.
3. Adicionar persistência e histórico.
4. Fechar com testes e menu de execução.