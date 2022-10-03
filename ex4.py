"""4. Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,
Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18"""
if __name__ == '__main__':
    s = int(input('quantos segundos?'))
    dias = s / 86400
    horas = s / 3600
    minutos = s / 60
    print(f'o numero de dias é {dias}, o de horas é {horas}, minutos é {minutos}, e o de segundos é {s}')