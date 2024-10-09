# Conversor de AFND para AFD

Este projeto implementa um conversor de Autômato Finito Não Determinístico (AFND) com transições epsilon (vazio) para um Autômato Finito Determinístico (AFD). Ele também permite testar se um conjunto de palavras é aceito pelo AFD gerado e visualizar os autômatos usando a biblioteca **Graphviz**.

## Estrutura do Projeto

- **converter.py**: Arquivo principal que contém as funções para leitura de autômatos, conversão de AFND para AFD, visualização e teste de aceitação de palavras.
- **entrada.txt**: Arquivo de entrada contendo a definição do AFND (estados, transições, estado inicial e finais).
- **saida.txt**: Arquivo de saída contendo o AFD gerado a partir do AFND fornecido.
- **palavras.txt**: Arquivo contendo uma lista de palavras a serem testadas no AFD.
- **saida_palavras.txt**: Arquivo que contém o resultado do teste de aceitação das palavras (se foram aceitas ou não pelo AFD).
- **grafo_afnd.dot**: Arquivo gerado pelo Graphviz que representa o AFND visualmente.
- **grafo_afd.dot**: Arquivo gerado pelo Graphviz que representa o AFD visualmente.

## Funcionalidades

1. **Leitura de Autômatos**: 
   - A função `ler_arquivo_automato` lê o arquivo de entrada com a definição de um AFND.

2. **Fecho Vazio**:
   - A função `palavra_vazia` (fecho epsilon) determina os estados que podem ser alcançados a partir de um estado usando apenas transições vazias.

3. **Conversão de AFND para AFD**:
   - A função `converter_para_dfa` converte um AFND para um AFD equivalente, eliminando transições não determinísticas.

4. **Teste de Aceitação de Palavras**:
   - A função `testar_palavras` verifica se um conjunto de palavras é aceito pelo AFD gerado.

5. **Visualização de Autômatos**:
   - A função `visualizar_automato` usa a biblioteca Graphviz para gerar um arquivo `.dot` que representa visualmente o AFND e o AFD.

## Como Usar

1. **Entrada do AFND**:
   - O arquivo `entrada.txt` deve ter o seguinte formato:
     - Primeira linha: Lista de estados do AFND.
     - Segunda linha: Estado inicial.
     - Terceira linha: Estados finais.
     - Linhas seguintes: Transições no formato `estado_inicial simbolo estado_destino`.

     Exemplo:
     ```
     A B C
     A
     C
     A 0 B
     B 1 C
     A h C  # h representa transição epsilon (vazia)
     ```

2. **Execução**:
   - Rode o arquivo `converter.py`. O programa irá:
     - Ler o AFND do arquivo `entrada.txt`.
     - Converter o AFND para AFD e salvar em `saida.txt`.
     - Gerar as representações gráficas do AFND e AFD em `grafo_afnd.dot` e `grafo_afd.dot`.
     - Testar as palavras em `palavras.txt` e salvar o resultado em `saida_palavras.txt`.

3. **Visualização**:
   - Use ferramentas como [Graphviz](https://graphviz.org/) para visualizar os arquivos `.dot` gerados.

## Exemplo de Arquivo de Palavras

O arquivo `palavras.txt` deve conter uma lista de palavras (cada palavra em uma linha) a serem testadas no AFD gerado.

  Exemplo:
  ```
  01
  001
  110
  ```

O resultado da aceitação será salvo em `saida_palavras.txt` no formato:
  ```
  01 aceito 
  001 não aceito 
  110 aceito
  ```
## Requisitos

- **Python 3.10+**
- **Bibliotecas**: `graphviz`, `collections`
- **Graphviz**: Necessário para gerar a visualização dos autômatos.

