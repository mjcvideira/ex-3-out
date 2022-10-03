
"""
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h 5 60m
(b) m/s

"""

"""
Este programa implementa funções aritméticas
"""


def aritmetica(valor1, valor2):
    total = valor1 / valor2
    return total

if __name__ == '__main__':
    km = int(input('diz um numaro'))
    horas = int(input('diz outro'))
    vm = (aritmetica(km, horas))
    print(int(f' velocidade media é {vm} km/hora'))

