#Faça um programa que recebe o preço de 10 produtos e
# exibe o valor do produto mais caro

maior_valor = 0 # crio a váriavel maior_valor para guardar o produto de maior preço
for x in range(0,11): # o loop começa em 0 e vai até 10
    x += 1 # adiciono + 1 toda vez que o loop se inicia para identificação do loop
    produto = float(input(f"Usuário {x} Qual o valor do produto? ")) # obtenho o valor do produto
    if produto >= maior_valor: # se o preço do produto for maior que o preço guardado, o produto vai ser o novo maior valor
        maior_valor = produto
print(f"O maior valor é {maior_valor}")