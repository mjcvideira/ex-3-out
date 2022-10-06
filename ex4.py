"""4. Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,
Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18"""
"""
def dia(valor):
    dias = valor / 60
    dias = dias / 60
    dias = dias / 24
    return dias


def hour(valor):
    hours = valor % (24 * 3600)
    hours = hours // 3600

    return hours
"""
def convertor(n):
    dia = n // (24 * 3600)

    n = n % (24 * 3600)
    horas = n // 3600

    n %= 3600
    minutos = n // 60

    n %= 60
    segundos = n
    print(f'Numero convertido é: {dia} dia/s, {horas} hora/s, {minutos} minuto/s, {segundos} segundos.')

if __name__ == '__main__':
    n = int(input('quantos segundos?'))
    print(f'o numero convertido é {convertor(n)}')