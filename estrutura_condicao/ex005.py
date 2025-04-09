

print("(1) - Média entre os números digitados (2) - Diferença do maior pelo menor (3) -  Produto entre os números digitados  (4) - Divisão do primeiro pelo segundo")
codigo_comando = int(input("Qual o código do comando? "))

a_valor = float(input("Qual o valor de A? "))
b_valor = float(input("Qual o valor de B? "))


if codigo_comando == 1:
    media_valores = ( a_valor + b_valor ) / 2
    print(f"A média final é: {media_valores}")
elif codigo_comando == 2:
    if a_valor > b_valor:
        diferenca_a = a_valor - b_valor
        print(f"{diferenca_a}")
    elif b_valor > a_valor:
        diferenca_b = b_valor - a_valor
        print(diferenca_b)
elif codigo_comando == 3:
    produto_valor = a_valor * b_valor
    print(f"Produto: {produto_valor}")
elif codigo_comando == 4:
    divisao_valor = a_valor / b_valor
    print(f"Divisão: {divisao_valor}")
else: 
    print("Insira um comando válido")
    