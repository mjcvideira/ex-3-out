"""3. Escreva um programa em Python que pede ao utilizador que lhe forneça

um inteiro correspondente a um número de segundos e que calcula o nú-
mero de dias correspondentes a esse número de segundos. O seu programa

deve permitir a interação:
Escreva um número de segundos
? 65432998
O número de dias correspondentes é 757.3263657407407"""
86400
if __name__ == '__main__':
    s = int(input('quantos segundos?'))
    dias = s / 86400
    print(f'o numero de dias é {dias}')