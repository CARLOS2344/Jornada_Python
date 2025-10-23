# Aqui fica toda a codificação, ou seja, a parte funcional do código que serão exportados pelos "__init__.py".
def aumento_porcentagem(valor=0, porcentagem=0, mostrar=False): # Criei uma função "def" que é chamada "aumento_porcentagem" o qual tem os parâmetros "valor", tendo o seu valor opcional 0, "porcentagem", tendo o seu valor opicional 0 e "mostrar", tendo o seu valor opcional "False".
    conversão_de_porcentagem_maior = porcentagem / 100 + 1 # Criei uma variável com escopo local chamado "conversão_de_porcentagem_maior" e atribuí o valor de "porcentagem / 100 + 1".
    valor_final = conversão_de_porcentagem_maior * valor # Criei uma variável com escopo local chamado "valor_final" e atribuí o valor de "conversão_de_porcentagem_maior * valor".
    if mostrar == True: # Utiliza-se uma estrutura de condição "if", logo, caso o usuário coloque o "mostrar" como "True", fará os seguintes passos...
        return f"{valor_final:.2f}".replace('.', ',') # Retorna para o usuário o valor formatado monetariamente do dinheiro.
    else: # Caso o usuário não mude nada, fará os seguintes passos...
        return valor_final # Retorna para o usuário o "valor_final" sem ajustes monetários.


def diminuição_porcentagem(valor=0, porcentagem=0, mostrar=False): # Criei uma função "def" que é chamada "diminuição_porcentagem" o qual tem os parâmetros "valor", tendo o seu valor opcional 0, "porcentagem", tendo o seu valor opicional 0 e "mostrar", tendo o seu valor opcional "False".
    conversão_de_porcentagem_menor = 1 - (porcentagem / 100) # Criei uma variável com escopo local chamado "conversão_de_porcentagem_menor" e atribuí o valor de "1 - (porcentagem / 100)".
    valor_final = conversão_de_porcentagem_menor * valor # Criei uma variável com escopo local chamado "valor_final" e atribuí o valor de "conversão_de_porcentagem_menor * valor".
    if mostrar == True: # Utiliza-se uma estrutura de condição "if", logo, caso o usuário coloque o "mostrar" como "True", fará os seguintes passos...
        return f"{valor_final:.2f}".replace('.', ',') # Retorna para o usuário o valor formatado monetariamente do dinheiro.
    else: # Caso o usuário não mude nada, fará os seguintes passos...
        return valor_final # Retorna para o usuário o "valor_final" sem ajustes monetários.


def dobro_do_número(num=0, mostrar=False): # Criei uma função "def" que é chamada "dobro_do_número" o qual tem os parâmetros "num", que tem o valor opcional "0" e "mostrar", que tem o valor opcional "False".
    dobro_do_número = num * 2 # Criei uma variável com escopo local chamado "dobro_do_número" e atribuí valor de "num * 2".
    if mostrar == True: # Utiliza-se uma estrutura de condição "if", logo, caso o usuário coloque o "mostrar" como "True", fará os seguintes passos...
        return f"{dobro_do_número:.2f}".replace('.', ',') # Retorna para o usuário o valor formatado monetariamente do dinheiro.
    else: # Caso o usuário não mude nada, fará os seguintes passos...
        return dobro_do_número # Retorna para o usuário o "dobro_do_número" sem ajustes monetários.


def metade_do_número(num=0, mostrar=False): # Criei uma função "def" que é chamada "metade_do_número" o qual tem os parâmetros "num", que tem o valor opcional "0" e "mostrar", que tem o valor opcional "False".
    metade_do_número = num / 2 # Criei uma variável com escopo local chamado "metade_do_número" e atribuí valor de "num / 2".
    if mostrar == True: # Utiliza-se uma estrutura de condição "if", logo, caso o usuário coloque o "mostrar" como "True", fará os seguintes passos...
        return f"{metade_do_número:.2f}".replace('.', ',') # Retorna para o usuário o valor formatado monetariamente do dinheiro.
    else: # Caso o usuário não mude nada, fará os seguintes passos...
        return metade_do_número # Retorna para o usuário a "metade_do_número" sem ajustes monetários.


def moeda_monetária(num=0): # Criei uma função "def" que é chamada "moeda_monetária" o qual tem os parâmetros "num" que tem o valor opcional "0"
    return f'{num:.2f}'.replace('.', ',') # Retorna para o usuário o valor formatado monetariamente do dinheiro.