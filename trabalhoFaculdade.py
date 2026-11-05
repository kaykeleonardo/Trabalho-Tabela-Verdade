def validar_expressao(entrada):
    operadores_permitidos = {'⋅', '.', '*', '+', 'v', 'V', '~', '!', '¬', '^'}
    delimitadores = {'(', ')', ' '}
    letras = []
    parenteses_iguais = 0
    contador_operadores = 0

    for x in entrada:
        if x == '(':
            parenteses_iguais += 1
        elif x == ')':
            parenteses_iguais -= 1
            if parenteses_iguais < 0:
                print("Erro: Parênteses fechados incorretamente.")
                return False, []
        elif x.isalpha() and x not in 'vV':
            letra = x.upper()
            if letra not in letras:
                letras.append(letra)
        elif x in operadores_permitidos:
            contador_operadores += 1
        elif x not in delimitadores and x not in operadores_permitidos:
            print(f"Erro: Caractere inválido detectado: {x}")
            return False, []
    
    if parenteses_iguais != 0:
        print("Erro: Expressão com parênteses desbalanceados.")
        return False, []

    if not letras:
        print("Erro: Nenhuma proposição/letra foi informada.")
        return False, []

    if contador_operadores < 1:
        print("Erro: Nenhum operador digitado.")
        return False, []

    letras.sort()
    return True, letras


def avaliar_linha(expressao_original, letras, linha_valores):
    expr = expressao_original.upper()

    expr = expr.replace('⋅', ' and ').replace('*', ' and ').replace('.', ' and ')
    expr = expr.replace('+', ' or ').replace('V', ' or ')
    expr = expr.replace('~', ' not ').replace('!', ' not ').replace('¬', ' not ')
    expr = expr.replace('^', ' ^ ')

    for var in letras:
        expr = expr.replace(var, str(linha_valores[var]))

    return int(bool(eval(expr)))


def classificar_proposicao(resultados):
    if all(r == 1 for r in resultados):
        return "Tautologia (sempre verdadeira)"
    elif all(r == 0 for r in resultados):
        return "Contradição (sempre falsa)"
    else:
        return "Contingência (valores verdadeiros e falsos)"


def gerar_tabela_verdade(entrada, letras):
    n = len(letras)
    total_linhas = 2 ** n
    resultados = []

    print("\n" + " | ".join(letras) + " | " + entrada)
    print("-" * (len(letras) * 4 + 12))

    for i in range(total_linhas):
        linha = {}
        for j, var in enumerate(letras):
            tamanho_bloco = total_linhas // (2 ** (j + 1))
            linha[var] = 1 if ((i // tamanho_bloco) % 2 == 1) else 0

        resultado = avaliar_linha(entrada, letras, linha)
        resultados.append(resultado)
        valores_cols = [str(linha[v]) for v in letras]
        print(f"  {' | '.join(valores_cols)}   |     {resultado}")

    print("-" * (len(letras) * 4 + 12))
    print(f"Classificação Lógica: {classificar_proposicao(resultados)}\n")


def main():
    entrada = input("Digite a Expressão Lógica (ex: (A + B) . ~C): ")
    valida, letras = validar_expressao(entrada)

    if valida:
        gerar_tabela_verdade(entrada, letras)


if __name__ == "__main__":
    main()