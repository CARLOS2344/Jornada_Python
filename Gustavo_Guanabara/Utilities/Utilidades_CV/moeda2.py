def resumo(num=0, porcentagem_maior=0, porcentagem_menor=0):
    """
    -> Gera um resumo financeiro formatado com os cálculos de aumento,
       redução, dobro e metade de um valor.
    :param num: O valor a ser analisado.
    :param porcentagem_maior: A porcentagem de aumento.
    :param porcentagem_menor: A porcentagem de redução.
    """
    valor_aumentado = num * (1 + porcentagem_maior / 100)
    valor_reduzido = num * (1 - porcentagem_menor / 100)
    dobro_do_preco = num * 2
    metade_do_preco = num / 2

    print("-" * 35)
    print("Resumo do Valor".center(35))
    print("-" * 35)
    print(f"{'Preço analisado:':<20}{f'R${num:.2f}'.replace('.', ','):>15}")
    print(f"{'Dobro do preço:':<20}{f'R${dobro_do_preco:.2f}'.replace('.', ','):>15}")
    print(f"{'Metade do preço:':<20}{f'R${metade_do_preco:.2f}'.replace('.', ','):>15}")
    print(f"{porcentagem_maior}% de aumento:".ljust(20) + f"R${valor_aumentado:.2f}".replace('.', ',').rjust(15))
    print(f"{porcentagem_menor}% de redução:".ljust(20) + f"R${valor_reduzido:.2f}".replace('.', ',').rjust(15))
    print("-" * 35)
