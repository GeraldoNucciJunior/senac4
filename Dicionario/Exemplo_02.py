import os
os.system('cls' if os.name == 'nt' else 'clear')
jogador = {}

jogador["x"] = 150
jogador["y"] = 300
jogador["vida"] = 100
jogador["nome"] = "Hero"

print (f" jogador {jogador['nome']} está na posição x: {jogador['x']} e y: {jogador['y']}.")


            