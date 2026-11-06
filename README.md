# Gerador de Tabela Verdade

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-conclu%C3%ADdo-brightgreen)

Programa em Python que roda no terminal, gera a tabela verdade de uma expressão lógica e diz se ela é **tautologia**, **contradição** ou **contingência**.

Trabalho da disciplina de **Matemática Computacional** (Ciência da Computação).

## O que o programa faz

- Pede uma expressão lógica ao usuário
- Confere se a expressão é válida (parênteses e caracteres)
- Gera todas as linhas da tabela verdade
- Calcula o resultado de cada linha
- Classifica a expressão

## Como funciona

**Número de linhas:** com `n` variáveis, a tabela tem `2^n` linhas. Cada variável nova dobra o tamanho da tabela.

| Variáveis | Linhas |
|:---:|:---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |

**Classificação:**

| Resultado | Quando acontece |
|:---|:---|
| Tautologia | Todas as saídas são 1 |
| Contradição | Todas as saídas são 0 |
| Contingência | Mistura de 0 e 1 |

## Operadores aceitos

| Operação | Símbolos |
|:---|:---:|
| E | `.` `*` `⋅` |
| OU | `+` `v` `V` |
| NÃO | `~` `!` `¬` |
| OU exclusivo (XOR) | `^` |

> A letra `V` não pode ser usada como variável, porque é um símbolo de OU.

## Como executar

É preciso ter o [Python 3](https://www.python.org/downloads/) instalado. Não precisa instalar nenhuma biblioteca.

```bash
python trabalhoFaculdade.py
```

## Exemplo

```text
Digite a Expressão Lógica (ex: (A + B) . ~C): (A + B) . ~C

A   | B   | C   | (A + B) . ~C
------------------------
  0 | 0 | 0   |     0
  0 | 0 | 1   |     0
  0 | 1 | 0   |     1
  0 | 1 | 1   |     0
  1 | 0 | 0   |     1
  1 | 0 | 1   |     0
  1 | 1 | 0   |     1
  1 | 1 | 1   |     0
------------------------
Classificação Lógica: Contingência (valores verdadeiros e falsos)
```

## Observação

Sempre coloque um operador entre as variáveis. Escreva `A . B`, e não `AB`.

## Autores

- Caio Eduardo
- Christian Lorran
- Gabriel Matheus
- Kayke Leonardo
- Luiz Philipe

Professor: Daniel Henrique Matos de Paiva
