"""Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos.

numeros = []
numeros.append(int(input(f' 1º numero')))
numeros.append(int(input(f' 2º numero')))
numeros.append(int(input(f' 3º numero')))
print(numeros)
while True:
    novo = numeros[0]
    troquei = False
    for x in range(3):
        if numeros[x] > numeros[x + 1]:
    novo = numeros[x]
        numeros[x] = numeros[x + 1]
        numeros[x + 1] = temp
        troquei = True
        if troquei == False:
            break
"""
if __name__ == '__main__':
    numeros = []
    numaro = int(input(f' quantos numeros?'))
    for x in range(1, numaro + 1):
        numeros.append(int(input(f'numero{x}:')))
    print(numeros)
    menor = numeros[0]
    maior = numeros[0]
    for x in range(1, len(numeros)):
        if numeros[x] < menor:
            menor = numeros[x]
        if numeros[x] > maior:
            maior = numeros[x]
print(f'o maior é {maior}')
print(f'o menor é {menor}')
