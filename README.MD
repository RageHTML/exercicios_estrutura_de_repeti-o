# Estrutura de Repetição 
### Nesse projeto fiz 4 exercicios para estudo e fixação de loops em python
![python-logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUnEVz-jev6MNWhSixdb49bIfRHZreT_KzBA&s)
## Como testar?
#### Dentro da pasta "estrutura_de_repetição" você vai encontrar 4 exercicios já respondidos,
`1 - ex001.py`
`2 - ex002.py`
`2 - ex003.py`
`3 - ex004.py`

# 1 - Faça um programa que ler 10 números e retorna se o número é positivo ou negativo e seu triplo

```
   for x in range(0,10):
    x = x + 1
    numero = int(input(f"Usuário {x}, insira o número: ")) 
    print(f"O triplo de {numero} = {triplo}")
    triplo = numero * 3 
    if numero >= 0:
        print("positivo")
    if numero <= 0: 
        print("negativo")  
```
