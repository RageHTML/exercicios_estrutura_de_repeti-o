for x in range(0,10):
    x = x + 1 # identificador do loop
    numero = int(input(f"Usuário {x}, insira o número: ")) # input do número
    triplo = numero * 3 # calculando o triplos
    print(f"O triplo de {numero} = {triplo}")
    if numero >= 0:
        print("positivo")
    if numero <= 0: 
        print("negativo") 
        

# O programa ler 10 numeros e retorna se o número é positivo e o seu triplo
    