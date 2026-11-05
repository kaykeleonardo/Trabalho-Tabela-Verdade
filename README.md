<div align="center">

# 🧮 Gerador de Tabela Verdade e Classificador Lógico

**Gere tabelas-verdade completas e classifique expressões lógicas direto do terminal.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnubash&logoColor=white)
![Dependencies](https://img.shields.io/badge/Depend%C3%AAncias-nenhuma-success?style=for-the-badge)
![Offline](https://img.shields.io/badge/Execu%C3%A7%C3%A3o-100%25%20offline-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-conclu%C3%ADdo-brightgreen?style=for-the-badge)

</div>

---

## 📖 Sobre o projeto

Aplicação de linha de comando (CLI) escrita em **Python puro**, sem bibliotecas externas, que recebe uma expressão da lógica proposicional, gera automaticamente a **tabela-verdade completa** e classifica o resultado como **tautologia**, **contradição** ou **contingência**.

Projeto acadêmico desenvolvido para a disciplina de **Matemática Computacional** do curso de **Ciência da Computação**.

## ✨ Funcionalidades

- ✅ Geração automática de todas as combinações de valores (0 e 1) para qualquer quantidade de variáveis
- ✅ Suporte aos conectivos **E**, **OU**, **NÃO** e **OU exclusivo (XOR)**, com várias notações aceitas
- ✅ Validação de entrada: parênteses balanceados, caracteres inválidos, ausência de variáveis e ausência de operadores
- ✅ Variáveis case-insensitive (`a` e `A` são a mesma proposição)
- ✅ Classificação lógica automática do resultado
- ✅ Execução determinística, local e offline, sem internet e sem inteligência artificial
- ✅ Código modular, separado em funções com responsabilidades únicas

## 📐 Fundamentação matemática

### Total de linhas

Pelo **princípio multiplicativo**, cada proposição pode assumir 2 valores (0 ou 1) de forma independente. Para `n` variáveis distintas, o total de linhas `L` da tabela-verdade é:

```math
L = 2^n
```

| Variáveis (`n`) | Linhas (`L = 2ⁿ`) |
|:---:|:---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

Cada variável nova **dobra** o tamanho da tabela.

### Algoritmo de alternância por blocos

Para que todas as combinações apareçam exatamente uma vez, a coluna da `j`-ésima variável (com `j` começando em 0) alterna entre 0 e 1 em blocos de tamanho:

```math
b_j = \frac{L}{2^{\,j+1}}
```

Para a linha `i` (com `i` de 0 a `L − 1`), o valor da variável `j` é:

```math
v_{i,j} = \left\lfloor \frac{i}{b_j} \right\rfloor \bmod 2
```

No código:

```python
tamanho_bloco = total_linhas // (2 ** (j + 1))
linha[var] = 1 if ((i // tamanho_bloco) % 2 == 1) else 0
```

Exemplo com `n = 3` (`L = 8`): a variável `A` alterna a cada 4 linhas, `B` a cada 2 e `C` a cada 1, o que reproduz a contagem binária de `000` até `111`.

### Classificação lógica

Seja `R` o conjunto das saídas da tabela:

```math
\text{Tautologia} \iff \forall r \in R,\ r = 1
```

```math
\text{Contradição} \iff \forall r \in R,\ r = 0
```

```math
\text{Contingência} \iff \exists\, r_1, r_2 \in R,\ r_1 = 1 \ \wedge\ r_2 = 0
```

## 🔣 Operadores suportados

| Operação | Símbolos aceitos | Equivalente em Python |
|:---|:---:|:---:|
| **E** (conjunção) | `.` &nbsp; `*` &nbsp; `⋅` | `and` |
| **OU** (disjunção) | `+` &nbsp; `v` &nbsp; `V` | `or` |
| **NÃO** (negação) | `~` &nbsp; `!` &nbsp; `¬` | `not` |
| **XOR** (ou exclusivo) | `^` | `^` |
| **Agrupamento** | `(` &nbsp; `)` | `(` &nbsp; `)` |

> ⚠️ Como `v` e `V` são operadores de OU, **a letra V não pode ser usada como nome de variável**.

## 🏗️ Arquitetura

O programa é dividido em quatro etapas, cada uma em sua função:

| Função | Responsabilidade |
|:---|:---|
| `validar_expressao()` | Valida parênteses e caracteres, e extrai as variáveis em ordem alfabética |
| `gerar_tabela_verdade()` | Calcula `2ⁿ`, gera as combinações por blocos e imprime a tabela |
| `avaliar_linha()` | Traduz os símbolos lógicos para Python e avalia a expressão para uma linha |
| `classificar_proposicao()` | Classifica o resultado em tautologia, contradição ou contingência |

### Validação sintática

- **Parênteses:** um contador de profundidade é incrementado em `(` e decrementado em `)`, com a mesma lógica de uma pilha. Ele rejeita um `)` sem `(` correspondente e também parênteses que sobram abertos no final.
- **Sanitização:** qualquer caractere fora do conjunto permitido (letras, operadores, parênteses e espaço) é rejeitado com mensagem de erro.
- **Estrutura mínima:** a expressão precisa ter pelo menos uma variável e pelo menos um operador.

### Avaliação e parsing

Os símbolos lógicos são substituídos pelas palavras-chave do Python (`and`, `or`, `not`), as variáveis são trocadas por seus valores `0`/`1` em cada linha, e o resultado é avaliado com `eval()` nativo. A execução é **estritamente determinística e offline**.

### Decisão de projeto

A tabela mostra apenas as **variáveis de entrada** e o **resultado final** da expressão. As subexpressões intermediárias são omitidas de propósito, para manter a saída legível no terminal e evitar quebra de linhas em expressões longas.

## 🚀 Como executar

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/) instalado
- Nenhuma biblioteca externa (não é necessário `pip install`)

Para conferir a versão instalada:

```bash
python --version
```

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

# 2. Entre na pasta do projeto
cd SEU-REPOSITORIO

# 3. Execute o programa
python trabalhoFaculdade.py
```

> Em alguns sistemas (Linux/macOS), use `python3` no lugar de `python`.

Em seguida, digite a expressão lógica quando o programa pedir.

## 💻 Exemplo de uso

**Entrada:**

```text
Digite a Expressão Lógica (ex: (A + B) . ~C): (A + B) . ~C
```

**Saída:**

```text
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

**Exemplo de erro tratado:**

```text
Digite a Expressão Lógica (ex: (A + B) . ~C): (A + B . C
Erro: Expressão com parênteses desbalanceados.
```

## ⚠️ Limitações conhecidas
- **Precedência do XOR:** em Python, `^` tem precedência maior que `not`, `and` e `or`. Use parênteses ao combiná-lo com outros operadores.
- **Uso do `eval()`:** a entrada é validada antes, mas o programa foi feito para uso local e acadêmico, não para receber entradas de terceiros em um serviço.
- **Variável `V`:** reservada ao operador OU, como explicado acima.

## 👥 Autores

Projeto desenvolvido em grupo para a disciplina de **Matemática Computacional**.

- Caio Eduardo
- Christian Lorran
- Gabriel Matheus
- Kayke Leonardo
- Luiz Philipe

**Orientação:** Prof. Daniel Henrique Matos de Paiva

---

<div align="center">

Feito com 🐍 e lógica proposicional

</div>
