"""
Escreva um programa que lê uma série de dígitos (terminando com -1) e
calcula o inteiro que tem esses dígitos. Por exemplo, lendo os dígitos 1 5
4 5 8 -1, calcula o número inteiro 15458.
"""
if __name__ == '__main__':
    continuar = 's' or 'S'
    listan = []
    while continuar == 's' or 'S':
        n = int(input('Digite um número inteiro: '))
        if n != -1:
            listan.append(n)
        if n == -1:
            numero = "".join(str(x) for x in listan)
            numeroint = int(numero)
            print(numeroint)
            continuar = int(input('Quer continuar? [1, 2]'))
            print(continuar)
            if continuar == 2:
                print(f'forºça')
                continuar = "n"
                break
            else:
                continuar = "s" or "S"
                print('dalhe')




