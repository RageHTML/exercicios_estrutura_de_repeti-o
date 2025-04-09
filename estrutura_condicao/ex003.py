time_x = input(f"Quantos gols foram marcados pelo time x? ")
time_y = input(f"Quantos gols foram marcados pelo time y? ")

if time_x > time_y:
    print(f"Placar do Jogo:\nTime X: {time_x}\nTime Y: {time_y}\nVencedor: Time X")
elif time_y > time_x:
    print(f"Placar do Jogo:\nTime Y: {time_x}\nTime Y: {time_y}\nVencedor: Time Y")
else:
    print(f"Placar do Jogo:\nTime X: {time_x}\nTime Y: {time_y}\nVencedor: Empate")