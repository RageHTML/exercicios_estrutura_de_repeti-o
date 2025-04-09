# Estrutura de Repetição 
### Nesse projeto fiz 4 exercicios para estudo e fixação de loops em python
![python-logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUnEVz-jev6MNWhSixdb49bIfRHZreT_KzBA&s)
## Como testar?
#### Dentro da pasta "estrutura_de_repetição" você vai encontrar 4 exercicios já respondidos,
`1 - ex001.py`
`2 - ex002.py`
`2 - ex003.py`
`3 - ex004.py`
#### No console da sua IDLE digite `python ex001.py` para executar o arquivo
## Exercicios
# 1 - Faça um programa que ler 10 números e retorna se o número é positivo ou negativo e seu triplo
#### usamos `for` ou `while` para iniciar uma estrutura de repetição
#### `in` `range`  para indicar quantas vezes o laço se repete, (0,10) começa em 0 e vai até 10
```
   for x in range(0,10):
```
#### váriavel de controle para identificar o loop
```
    x = x + 1 
```
#### váriavel `numero` para armazenar o número
#### `input(f"Usuário {x}, insira o número: ")` o `f` antes das aspas é uma `F-STRING` é uma ferramenta do Python que permite formatar strings e inserir variáveis dentro delas

```
    numero = int(input(f"Usuário {x}, insira o número: ")) 
```
##### saida console:
![saida_console](/images/console_out.png)
#### Obtendo o triplo do número fornecido
```
    triplo = numero * 3
    print(f"O triplo de {numero} = {triplo}")
```
#### Estrutura de condição para verificar se o número é `positivo` ou `negativo`
```    
    if numero >= 0:
        print("positivo")
    if numero <= 0: 
        print("negativo")  
```
#### Execução final:
![image_final](/images/imagem_final.png)

