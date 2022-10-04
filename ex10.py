"""
Escreva um programa em Python que lê um número inteiro positivo e
calcula o número obtido do número lido que apenas contém os seus dígitos
impares. Por exemplo,
Escreva um inteiro
? 785554
Resultado: 7555
"""
def impar(num):
    if num % 2 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        n = input('Digite um número inteiro: ')
        nl = []
        for x in n:
            if int(x) % 2 != 0:
                nl.append(x)
        print(int(''.join(nl)))



