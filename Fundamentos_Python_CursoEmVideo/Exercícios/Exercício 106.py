def mensagem_com_linhas_com_cores_verdes(msg): # Crio uma função "def" chamada "mensagem_com_linhas_com_cores_verdes" e tem o parâmetro "msg".
    """
    -> Imprime uma mensagem formatada com linhas e cor magenta.
    :param msg: A mensagem a ser exibida.
    """
    mais_dois = len(msg) + 2 # Criei uma variável com escopo local chamado "mais_dois" o qual acrescenta mais dois elementos em "len()".
    print("\033[0;35m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será verde.
    print(f" \033[0;35m{msg}\033[m") # Imprime-se o parâmetro "msg" com uma cor personalizada "verde".
    print("\033[0;35m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será verde.


def mensagem_com_linhas_azuis(msg): # Crio uma função "def" chamada "mensagem_com_linhas_azuis" que tem o parâmetro "msg".
    """
    -> Imprime uma mensagem formatada com linhas e cor azul.
    :param msg: A mensagem a ser exibida.
    """
    mais_dois = len(msg) + 2 # Criei uma variável com escopo local chamado "mais_dois" o qual acrescenta mais dois elementos em "len()".
    print("\033[0;34m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será azul.
    print(f" \033[0;34m{msg}\033[m") # Imprime-se o parâmetro "msg" com uma cor personalizada "azul".
    print("\033[0;34m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será azul.


def mensagem_com_linhas_vermelhas(msg): # Crio uma função "def" chamada "mensagem_com_linhas_vermelhas" que tem o parâmetro "msg".
    """
    -> Imprime uma mensagem formatada com linhas e cor vermelha.
    :param msg: A mensagem a ser exibida.
    """
    mais_dois = len(msg) + 2 # Criei uma variável com escopo local chamado "mais_dois" o qual acrescenta mais dois elementos em "len()".
    print("\033[0;31m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será vermelho.
    print(f" \033[0;31m{msg}\033[m") # Imprime-se o parãmetro "msg" com uma cor personalizada "vermelha".
    print("\033[0;31m=\033[m" * mais_dois) # Imprime-se a quantidade de "=" de acordo com a quantidade de letras + 2 no parâmetro "msg". Outrossim, será vermelho.


def retornando_o_doc(comando): # Crio uma função "def" chamada "retornando_o_doc" que tem o parâmetro "comando".
    """
    -> Exibe a documentação de um comando Python.
    A função help() imprime a ajuda diretamente e não retorna valor.
    :param comando: A função ou biblioteca a ser consultada.
    """
    interactive_help = help(comando) # Criei uma variável com escopo local chamado "interactive_help" e atribui um valor lógico de chamar a função "help()" e dentro dela terá a mensagem que o usuário digitar.
    return f"/033[1;97m{interactive_help}/033[m" # Retorna para o usuário o resultado final com uma cor personalizada "branco".


while True: # Criei uma estrutura de repetição "while True", ou seja, vai ficar em looping até que o valor seja "False".
    mensagem_com_linhas_com_cores_verdes("SISTEMA DE AJUDA PyHELP") # Chamei a função "mensagem_com_linhas_com_cores_verdes" e coloquei uma mensagem personalizada "SISTEMA DE AJUDA PyHELP".
    option = str(input("\033[1;33mDigite uma função ou bliblioteca >\033[m ")).strip().lower() # Com a função "input()", mando o usuário digitar qual comando ou função será usado na função "help".
    if option == "fim": # Se o usuário digitar "fim", fará os seguintes passos...
        break # Encerra o looping.
    mensagem_com_linhas_azuis(f"PROCESSANDO O COMANDO '{option}'...") # Chamei a função "mensagem_com_linhas_azuis" e coloquei uma mensagem personalizada "PROCESSANDO O COMANDO {Comando que o usuário digitou no "option"}...".
    retornando_o_doc(option) # Mostra o resultado final
mensagem_com_linhas_vermelhas("<< Programa finalizado >>") # Chamei a função "mensagem_com_linhas_vermelhas" e coloquei uma mensagem personalizada "<< Programa finalizado >>".