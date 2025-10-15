def mensagem_com_linhas_com_cores_verdes(msg):
    mais_dois = len(msg) + 2
    print("\033[0;35m=\033[m" * mais_dois)
    print(f" \033[0;35m{msg}\033[m")
    print("\033[0;35m=\033[m" * mais_dois)


def mensagem_com_linhas_azuis(msg):
    mais_dois = len(msg) + 2
    print("\033[0;34m=\033[m" * mais_dois)
    print(f" \033[0;34m{msg}\033[m")
    print("\033[0;34m=\033[m" * mais_dois)


def mensagem_com_linhas_vermelhas(msg):
    mais_dois = len(msg) + 2
    print("\033[0;31m=\033[m" * mais_dois)
    print(f" \033[0;31m{msg}\033[m")
    print("\033[0;31m=\033[m" * mais_dois)


def retornando_o_doc(comando):
    interactive_help = help(comando)
    return f"/033[1;97m{interactive_help}/033[m"


while True:
    mensagem_com_linhas_com_cores_verdes("SISTEMA DE AJUDA PyHELP")
    option = str(input("\033[1;33mDigite uma função ou bliblioteca >\033[m ")).strip().lower()
    if option == "fim":
        break
    mensagem_com_linhas_azuis(f"PROCESSANDO O COMANDO '{option}'...")
    retornando_o_doc(option)
mensagem_com_linhas_vermelhas("<< Programa finalizado >>")

