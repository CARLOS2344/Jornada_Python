def leaint(msg):
    """
    -> Valida a entrada para garantir que seja um número inteiro (positivo ou negativo).
    :param msg: A mensagem a ser exibida para o usuário (como no input).
    :return: O valor inteiro digitado.
    """
    while True:
        num_str = str(input(msg)).strip()
        # Validação para números positivos e negativos
        if num_str.isnumeric() or (num_str.startswith('-') and num_str[1:].isnumeric()):
            return int(num_str)
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")


# Programa Principal
n = leaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")