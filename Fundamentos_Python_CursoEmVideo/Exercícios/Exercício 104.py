def leaint(msg): # Crio uma função "def" que é chamada "leaint" o qual tem o parâmetro "msg".
    """
    -> Valida a entrada para garantir que seja um número inteiro (positivo ou negativo).
    :param msg: A mensagem a ser exibida para o usuário (como no input).
    :return: O valor inteiro digitado.
    """
    while True: # Utilizo uma estrutura de repetição "while True", ou seja, enquanto o valor do looping for "True", irá continuar.
        num_str = str(input(msg)).strip() # Criei uma variável global "num_str" e atribui o valor de input(), ou seja, colocará esse número em valor de "str".
        # Validação para números positivos e negativos
        if num_str.isnumeric() or (num_str.startswith('-') and num_str[1:].isnumeric()): # Utilizo uma estrutura de condição "if", logo, analiso se o valor dado é numérico e começa com "-". Sendo assim, seguirá os seguintes passos...
            return int(num_str) # Retorno o valor "int" para o usuário.
        else: # Utilizo uma estrutura de condição "else", logo, se não for nenhuma das opções a cima, fará os seguintes passos...
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m") # Imprime-se uma mensagem de erro, ou seja, se o valor não for numérico, dará erro.


# Programa Principal
n = leaint("Digite um número: ") # Mando o usuário digitar um valor através do input() e o valor digitado irá direto para a função "leaint".
print(f"Você acabou de digitar o número {n}") # Imprime-se a mensagem final.