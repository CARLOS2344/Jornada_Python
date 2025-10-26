def cadastramento_de_pessoas(arquivo="Digite o nome do arquivo: "):
    """
    -> Gerencia um sistema de cadastro de pessoas em um arquivo de texto.

    A função solicita um nome de arquivo, valida-o e, em seguida, exibe um
    menu interativo para cadastrar novas pessoas, listar os cadastros
    existentes ou sair do sistema.

    :param arquivo: (str, opcional) A mensagem a ser exibida ao solicitar o nome do arquivo.
    """
    try:
        arquivo_nome = input(arquivo).strip()
    except KeyboardInterrupt:
        print("\n\033[0;31mO usuário preferiu não digitar!\033[m ")
        return
    while True:
        if arquivo_nome == "":
            print("\033[0;31mERRO! Digite um arquivo válido!\033[m ")
            return
        elif '.txt' not in arquivo_nome:
            print("\033[0;31mERRO! Digite um arquivo que contenha '.txt'!\033[m ")
            return
        else:
            try:
                print("+=" * 15)
                print("MENU INTERATIVO".center(30))
                print("+=" * 15)
                print("""\033[0;33m1\033[m - \033[0;36mCadastrar nova pessoa\033[m
\033[0;33m2\033[m - \033[0;36mListar pessoas cadastradas\033[m
\033[0;33m3\033[m - \033[0;36mSair do sistema\033[m""")
                print("+=" * 15)
                choice = int(input("Digite a opção desejada: ").strip())
                if choice == 1:
                    try:
                        print("=" * 30)
                        print("NOVO CADASTRO".center(30))
                        print("=" * 30)
                        with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
                            while True:
                                try:
                                    nome = str(input("Digite o nome: ")).strip().upper()
                                    if nome == "":
                                        print("\033[0;31mERRO! Digite um nome válido!\033[m ")
                                        return
                                    idade = int(input("Digite a idade: ").strip())
                                    arquivo.write(f"{nome:<10}\t{idade:>2} anos\n")
                                except(ValueError, TypeError):
                                    print("\033[0;31mERRO! Digite uma idade válida!\033[m ")
                                    return
                                except KeyboardInterrupt:
                                    print("\n\033[0;31mO usuário preferiu não digitar!.\033[m ")
                                    return
                                else:
                                    print(f"{nome.title()} cadastrado(a) com sucesso! ")
                                break
                    except:
                        print(f"\033[0;31mERRO! Tente novamente mais tarde.\033[m ")
                        return
                elif choice == 2:
                    try:
                        print("=" * 30)
                        print("PESSOAS CADASTRADAS".center(30))
                        print("=" * 30)
                        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                            print(arquivo.read())
                        print("=" * 30)
                    except:
                        print("\033[0;31mERRO! Tente novamente mais tarde.\033[m ")
                        return
                elif choice == 3:
                    print("=" * 30)
                    print("SAINDO DO SISTEMA".center(30))
                    print("=" * 30)
                    break
                else:
                    print("\033[0;31mERRO! Digite uma opção válida!\033[m ")
            except(ValueError, TypeError):
                print("\033[0;31mERRO! Digite uma opção válida!\033[m ")
            except KeyboardInterrupt:
                print("\n\033[0;31mO usuário preferiu não digitar essa opção.\033[m ")