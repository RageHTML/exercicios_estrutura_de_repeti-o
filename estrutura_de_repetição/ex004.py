# Cada espectador de um cinema respondeu a um questionário
# no qual constava sua opinião em relação ao filme: ótimo – 3,
# bom – 2, regular – 1. Faça um programa que receba a opinião
# de 5 espectadores, calcule e mostre:

regular = 0
bom = 0
otimo = 0 

for i in range(0,5):
    i += 1
    prompt = int(input("O que achou do filme?\n (1) - Regular (2) - Bom (3) - Ótimo\n --> "))
    if prompt == 1:
        regular += 1
    elif prompt == 2:
        bom += 1
    elif prompt ==3:
        regular += 1
    else:
        print(f"\n Usuário {i} Insira uma opção válida\n ")
print(f"Resultados\nRegular: {regular}\nBom: {bom}\nÓtimo: {otimo}")