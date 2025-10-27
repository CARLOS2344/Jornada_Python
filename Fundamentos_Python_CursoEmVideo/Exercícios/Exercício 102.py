def mensagem_com_linhas(msg): # Criei uma função "def" chamada "mensagem_com_linhas" o qual tem o parâmetro "msg".
    """-> Imprime uma mensagem personalizada.
    :param msg: A mensagem a ser impressa.
    """
    print("=" * len(msg)) # Dentro da função, imprime-se "=" a quantidade de letras que tem a mensagem.
    print(msg) # Dentro da função, imprime-se o parâmetro "msg".
    print("=" * len(msg)) # Dentro da função, imprime-se "=" a quantidade de letras que tem a mensagem.


name = str(input("Digite seu nome: ")).strip().upper() # Pergunto o nome do usuário através da função "input()"
mensagem_com_linhas(f"Olá, {name.title()} iremos calcular o fatorial de um determinado número! ") # Chamo/Declaro a função "mensagem_com_linhas", logo, vai fazer uma mensagem personalizada.


def fatorial(num=1, show=False): # Dentro da função "def" chamada "fatorial" tem os parâmetros "num" que tem um valor opcional "1" e "show" que tem o valor opcional "False".
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    calculo_de_fatorial = 1 # Criei uma variável local chamada "calculo_de_fatorial" e atribuo o valor de "1".
    for n in range(num, 0, -1): # Utilizo uma estrutura de repetição "for" e o seu range começa com o parâmetro "num", termina com "0" e vai indo de "-1" em "-1".
        calculo_de_fatorial *= n # Aqui, calcula-se a fatorial do número
        if show == True: # Utilizo uma estrutura de condição "if", logo, se o usuário colocar o "show=True", irá fazer os seguintes passos...
            print(n, end = " ") # Imprime-se o valor "n" da estrutura de repetição "for".
            if n > 1: # Dentro da estrutura de condição "if", utilizo outra estrutura de condição "if", logo, se o valor "n" for maior que "1", irá fazer os seguintes passos...
                print("x", end = " ") # Imprime-se o valor "x". Ou seja, vai ficar imprimindo o valor "x" até que o "n" seja menor que "1".
            else: # Dentro da estrutura de condição "if", utilizo o "else", logo, se não for nenhuma das condições a cima, fará os seguintes passos...
                print("=", end = " ") # Imprime-se o sinal de "igual" no final.
    return calculo_de_fatorial # Vai retornar ao usuário o cálculo da fatorial.


while True: # Aqui, utilizo uma estrutura de repetição "while True", ou seja, toda vez que um valor for True, ele continuará no looping.
    número = int(input("Digite um número para a fatorial: ").strip()) # Peço para o usuário digitar um número.
    mensagem_com_linhas("""Meunu de Opções:
[ 1 ] Calcular o fatorial de um número mostrando a multiplicação;
[ 2 ] Calcular o fatorial de um número sem mostrar a multiplicação.""") # Chamo/Declaro a função "mensagem_com_linhas" e faço um menu personalizado.
    choice = int(input(f"{name.title()}, escolha uma das opções acima: ").strip()) # Mando o usuário digitar a sua escolha com a função "input()".
    if choice == 1: # Utilizo uma estrutura de condição "if", logo, se o valor de "choice" for "1", fará os seguintes passos...
        print(fatorial(número, show=True)) # Vai imprimir o resultado da fatorial, mostrando o processo.
    elif choice == 2: # Utilizo uma estrutura de condição "elif", logo, se o valor de "choice" for "2", fará os seguintes passos...
        print(fatorial(número, show=False)) # Imprime-se o resultado da fatorial sem mostrar o processo, apenas o resultado.
    else: # Utilizo uma estrutura de condição "else", logo, se o valor de "choice" não for "1" ou "2", fará os seguintes passos...
        print("Comando inválido! Encerrando o programa... ") # Imprime-se a mensagem de comando inválido e de encerramento do programa.
        break # Saio do looping com o "break".
    escolha = str(input(f"{name.title()}, você deseja continuar? [S/N]: ")).strip()[0] # Aqui, pergunto ao usuário se ele quer continuar no programa.
    if escolha in "Ss": # Utilizo uma estrutura de condição "if", logo, se o valor digitado em "escolha" estiver em "Ss", fará os seguintes passos...
        print("Continuando o programa... ") # Imprime-se a mensagem de continuando o programa.
        continue # Continua o programa com o "continue".
    elif escolha in "Nn": # Utilizo uma estrutura de condição "elif", logo, se o valor digitado em "escolha" estiver em "Nn" fará os seguintes passos...
        print("Encerrando o programa... ") # Imprime-se a mensagem de encerrando o programa.
        break # Saio do looping com o "break".
    else: # Utilizo uma estrutura de condição "else", logo se a "escolha" não for "Ss" ou "Nn", fará os seguintes passos...
        print("Comando inválido! Encerrando o programa... ") # Imprime-se a mensagem de comando inválido e encerrando o programa.
        break # Saio do looping com o "break".
mensagem_com_linhas("<< Programa finalizado>>") # Chamo/Declaro a função "mensagem_com_linhas" e faço uma mensagem personalizada com "<< Programa finalizado >>".