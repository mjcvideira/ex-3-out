"""
14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""
if __name__ == '__main__':
    continuar = 's' or 'S'
    while continuar == 's' or 'S':
        n = input('Digite um número inteiro: ')
        nl = list(n)
        nl1 = []
        conta = 0
        for x in range(len(nl)):
            conversao = int(nl[x])
            nl1.append(conversao)
        for x in range(len(nl)):
            conta += nl1[x]
        print(conta)
