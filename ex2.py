
"""
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h 5 60m
(b) m/s

"""
def km(valor1, valor2):
    valor2 = valor2 / 60
    total = valor1 / valor2
    return total
def metro(valor1, valor2):
    valor1 = valor1 * 1000
    valor2 = valor2 * 60
    total = valor1 / valor2
    return total



if __name__ == '__main__':
    kmv = int(input('quantos km'))
    horas = int(input('quantos minutos'))
    print(f'A velocidade média é {km(kmv, horas)} K/H e {metro(kmv, horas)} M/S')

