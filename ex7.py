"""
Escreva um programa em Python que lê o número de horas, que um em-
pregado trabalhou numa dada semana e o seu salário/hora e calcula o

ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas fôr menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora, em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
"""
if __name__ == '__main__':
    horas = int(input(f'intrudozir horas'))
    shora = int(input(f'intrudozir salário por hora'))
    if horas <= 40:
        ordenado = horas * shora
        print(f'{ordenado}')
    if horas > 40:
        hextra = horas - 40
        ordenado = (40 * shora) + (hextra * (shora * 2))
        print(f'{ordenado}')