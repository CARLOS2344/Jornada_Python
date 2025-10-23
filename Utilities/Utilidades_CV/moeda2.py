# Aqui fica toda a codificação, ou seja, a parte funcional do código que serão exportados pelos "__init__.py".
def resumo(num=0, porcentagem_maior=0, porcentagem_menor=0): # Criei uma função "def" que é chamada "resumo" o qual tem os parâmetros "num", que tem o valor opcional "0", "porcentagem_maior", que tem o valor opcional "0" e "porcentagem_maior", que tem o valor opcional "0".
    """
    -> Gera um resumo financeiro formatado com os cálculos de aumento,
       redução, dobro e metade de um valor.
    :param num: O valor a ser analisado.
    :param porcentagem_maior: A porcentagem de aumento.
    :param porcentagem_menor: A porcentagem de redução.
    """
    valor_aumentado = num * (1 + porcentagem_maior / 100) # Crio uma variável com escopo local chamada "valor_aumentado" e atribuí o valor dela de "num * (1 + porcentagem_maior / 100)".
    valor_reduzido = num * (1 - porcentagem_menor / 100) # Crio uma variável com escopo local chamada "valor_reduzido" e atribuí o valor dela de "num * (1 - porcentagem_menor / 100)".
    dobro_do_preco = num * 2 # Crio uma variável com escopo local chamada "dobro_do_preco" e atribuí o valor dela de "num * 2".
    metade_do_preco = num / 2 # Crio uma variável com escopo local chamada "metade_do_preco" e atribuí o valor dela de "num / 2".

    print("-" * 35) # Imprime-se "-" trinta e cinco vezes no terminal.
    print("Resumo do Valor".center(35)) # Deixa o valor centralizado usando a formatação "center()".
    print("-" * 35) # Imprime-se "-" trinta e cinco vezes no terminal.
    print(f"{'Preço analisado:':<20}{f'R${num:.2f}'.replace('.', ','):>15}") # Deixa o valor formatado para a esqueda com a formatação ":<20" e coloca o valor formatado monetariamente à direita com a formatação ":>15".
    print(f"{'Dobro do preço:':<20}{f'R${dobro_do_preco:.2f}'.replace('.', ','):>15}") # Deixa o valor formatado para a esqueda com a formatação ":<20" e coloca o valor formatado monetariamente à direita com a formatação ":>15".
    print(f"{'Metade do preço:':<20}{f'R${metade_do_preco:.2f}'.replace('.', ','):>15}") # Deixa o valor formatado para a esqueda com a formatação ":<20" e coloca o valor formatado monetariamente à direita com a formatação ":>15".
    print(f"{porcentagem_maior}% de aumento:".ljust(20) + f"R${valor_aumentado:.2f}".replace('.', ',').rjust(15)) # Deixa o valor formatado para a esqueda com a função "ljust(20)" e coloca o valor formatado monetariamente à direita com a função "rjust(15)".
    print(f"{porcentagem_menor}% de redução:".ljust(20) + f"R${valor_reduzido:.2f}".replace('.', ',').rjust(15))  # Deixa o valor formatado para a esqueda com a função "ljust(20)" e coloca o valor formatado monetariamente à direita com a função "rjust(15)".
    print("-" * 35) # Imprime-se "-" trinta e cinco vezes no terminal.