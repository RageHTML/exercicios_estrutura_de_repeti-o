# Faça um programa que lê a resposta de 15 usuários para a
# seguinte pergunta: “Você gosta de beterraba? Digite 1 para
# SIM e 2 para NÃO”. Após a coleta da resposta de cada
# usuário, o algoritmo deverá exibir a quantidade de
# respostas para cada opção;

sim = 0
nao = 0

for i in range(0,152):
    i += 1 # mesma coisa que i = i + 1
    prompt = int(input(f"Usuário {i} você gosta de beterraba?\nDigite (1) SIM e (2) para NÃO\n --> "))
    if prompt == 1:
        sim += 1
    elif prompt == 2:
        nao += 1
    else:
        print("Insira apenas opções válidas")

    if i == 15:
        print(f"Sim: {sim}\nNão: {nao}")
