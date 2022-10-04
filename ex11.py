"""
11. Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""
if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        n = input('Digite um número inteiro: ')
        nl = [n]
        print(nl)
