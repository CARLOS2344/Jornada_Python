def aumento_porcentagem(valor=0, porcentagem=0, mostrar=False):
    conversão_de_porcentagem_maior = porcentagem / 100 + 1
    valor_final = conversão_de_porcentagem_maior * valor
    if mostrar == True:
        return f"{valor_final:.2f}".replace('.', ',')
    else:
        return valor_final


def diminuição_porcentagem(valor=0, porcentagem=0, mostrar=False):
    conversão_de_porcentagem_menor = 1 - (porcentagem / 100)
    valor_final = conversão_de_porcentagem_menor * valor
    if mostrar == True:
        return f"{valor_final:.2f}".replace('.', ',')
    else:
        return valor_final


def dobro_do_número(num=0, mostrar=False):
    dobro_do_número = num * 2
    if mostrar == True:
        return f"{dobro_do_número:.2f}".replace('.', ',')
    else:
        return dobro_do_número


def metade_do_número(num=0, mostrar=False):
    metade_do_número = num / 2
    if mostrar == True:
        return f"{metade_do_número:.2f}".replace('.', ',')
    else:
        return metade_do_número


def moeda(num=0):
    return f'{num:.2f}'.replace('.', ',')