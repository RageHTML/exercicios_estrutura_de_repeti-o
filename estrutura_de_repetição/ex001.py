for x in range(0,10):
    x = x + 1
    numero = int(input(f"Usuário {x}, insira o número: ")) 
    triplo = numero * 3 
    print(f"O triplo de {numero} = {triplo}")

    if numero >= 0:
        print("positivo")
    if numero <= 0: 
        print("negativo") 