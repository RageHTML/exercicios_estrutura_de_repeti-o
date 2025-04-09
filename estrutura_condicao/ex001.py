a_nota = float(input("Usuário digite a Av1 "))
b_nota = float(input("Usuário digite a Av2 "))
c_nota = float(input("Usuário digite a Av3 "))

media = (a_nota + b_nota + c_nota) / 3

if media >= 7:
    print("Resultado: Aprovado")
if media <= 0:
    print("Resultado: Reprovado")
else:
    print("Insira um valor válido")

print(f"Nota A: {a_nota}\nNota B: {b_nota}\nNota C: {c_nota}\nMédia Final: {media}")


