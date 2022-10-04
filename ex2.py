
"""
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h 5 60m
(b) m/s

"""
def aritmetica(valor1, valor2):
    valor3 = valor2 / 60
    total = valor1 / valor3
    return total
def metro(valor1, valor2):
    valorm = valor1 * 1000
    valorh = valor2 * 60
    total = valorm / valorh

if __name__ == '__main__':
    km = int(input('quantos km'))
    horas = int(input('quantos minutos'))
    vm = (aritmetica(km, horas))
    print(f' velocidade media é {vm} km/hora')
    vs = (aritmetica((km, horas)))
    print(f' velocidade em m/s é {vs}')

