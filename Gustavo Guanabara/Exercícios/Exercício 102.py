def mensagem_com_linhas(msg):
    """-> Imprime uma mensagem personalizada.
    :param msg: A mensagem a ser impressa.
    """
    print("=" * len(msg))
    print(msg)
    print("=" * len(msg))


name = str(input("Digite seu nome: ")).strip().upper()
mensagem_com_linhas(f"Olá, {name.title()} iremos calcular o fatorial de um determinado número! ")


def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    calculo_de_fatorial = 1
    for n in range(num, 0, -1):
        calculo_de_fatorial *= n
        if show == True:
            print(n, end = " ")
            if n > 1:
                print("x", end = " ")
            else:
                print("=", end = " ")
    return calculo_de_fatorial


while True:
    número = int(input("Digite um número para a fatorial: ").strip())
    mensagem_com_linhas("""Meunu de Opções:
[ 1 ] Calcular o fatorial de um número mostrando a multiplicação;
[ 2 ] Calcular o fatorial de um número sem mostrar a multiplicação.""")
    choice = int(input(f"{name.title()}, escolha uma das opções acima: ").strip())
    if choice == 1:
        print(fatorial(número, show=True))
    elif choice == 2:
        print(fatorial(número, show=False))
    else:
        print("Comando inválido! Encerrando o programa... ")
        break
    escolha = str(input(f"{name.title()}, você deseja continuar? [S/N]: ")).strip()[0]
    if escolha in "Ss":
        print("Continuando o programa... ")
        continue
    elif escolha in "Nn":
        print("Encerrando o programa... ")
        break
    else:
        print("Comando inválido! Encerrando o programa... ")
        break
mensagem_com_linhas("<< Programa finalizado>>")

