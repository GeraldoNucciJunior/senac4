import os
os.system('cls' if os.name == 'nt' else 'clear')
lista =["A",35,3.14,True]
print(lista)

qtde_posicoes =len(lista    )
print ("Quantidade de posições da lista: ", qtde_posicoes)



lista.insert(4,2026)
print(lista)
lista.insert(2,"Ola Mundo")
print(lista)

pause = input("Pressione ENTER para continuar...")

del lista[2]

print (lista)

lista.pop(2)
print(lista)

pause = input("Pressione ENTER para continuar...")


lista.remove("Ola Mundo")
print(lista)

for i in range(2):
    lista.append(i)


print (lista)


