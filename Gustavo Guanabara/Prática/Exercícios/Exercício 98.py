from time import sleep
def mensagem_com_linhas(msg):
    print("=" * len(msg))
    print(msg)
    print("=" * len(msg))


def contagem_de_números():
    print("+=" * 15)
    print("Contagem de 1 até 10 de 1 em 1: ")
    for c in range(1, 11):
        print(c, end = " ", flush=True)
        sleep(1)
    print("Fim da contagem! ")
    print("+=" * 15)
    print("Contagem de 10 até 0 de 2 em 2: ")
    for c in range(10, -1, -2):
        print(c, end = " ", flush=True)
        sleep(1)
    print("Fim da contagem! ")
    print("+=" * 15)


def contagem_de_números_personalizada(i, f, p):
    print("<< AGORA É SUA VEZ GAFANHOTO(A) >>")
    if i > f:
        if p > 0:
            passo_convertido = - p
            p = passo_convertido
            final_menos_um = f - 1
            f = final_menos_um
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de {- p} em {- p}: ")
        elif p < 0:
            final_menos_um = f - 1
            f = final_menos_um
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de {- p} em {- p}: ")
        else:
            p = -1
            final_menos_um = f - 1
            f = final_menos_um
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de 1 em 1: ")
    else:
        if p > 0:
            final_mais_um = f + 1
            f = final_mais_um
            mensagem_com_linhas(f"Contagem de {i} até {f - 1} de {p} em {p}: ")
        elif p == 0:
            p = 1
            final_mais_um = f + 1
            f = final_mais_um
            mensagem_com_linhas(f"Contagem de {i} até {f - 1} de 1 em 1: ")
    for c in range(i, f, p):
        print(c, end = " ", flush=True)
        sleep(1)
    print("Fim da contagem! ")
    

nome_do_gafanhoto = str(input("Digite seu nome, gafanhoto(a): ")).strip().upper()
while True:
    mensagem_com_linhas(f"Olá, {nome_do_gafanhoto.title()} escolha uma dessas opções para prosseguir: ")
    print("""[ 1 ] Contagem de 1 até 10 de 1 em 1 e Contagem de 0 até 10 de 2 em 2
[ 2 ] Contagem personalizada """)
    choice = int(input(f"{nome_do_gafanhoto.title()}, escolha uma das opções acima: ").strip())
    sleep(1.5)
    if choice == 1:
        contagem_de_números()
    elif choice == 2:
        valor_inicial = int(input("Digite o valor inicial da contagem: ").strip())
        valor_final = int(input("Digite o valor final da contagem: ").strip())
        valor_passo = int(input("Digite a quantidade de passos que a contagem deverá fazer: ").strip())
        contagem_de_números_personalizada(i=valor_inicial, f=valor_final, p=valor_passo)
    else:
        print("Comando inválido! Encerrando o programa... ")
        break
    choice_two = str(input(f"{nome_do_gafanhoto.title()}, você deseja continuar escolhendo? [S/N]: ")).strip()[0]
    if choice_two in "Ss":
        print("Continuando o programa... ")
        continue
    elif choice_two in "Nn":
        print("Encerrando o programa... ")
        break
    else:
        print("Comando inválido! Encerrando o programa... ")
        break
sleep(3)
print("<< Programa finalizado >>")