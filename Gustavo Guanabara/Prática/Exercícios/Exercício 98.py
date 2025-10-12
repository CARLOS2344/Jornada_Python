from time import sleep # Importo da bliblioteca "time" a função "sleep".


def mensagem_com_linhas(msg): # Crio uma função def "mensagem_com_linhas" que tem o parâmetro "msg".
    print("=" * len(msg)) # Imprime-se "=" de acordo com a quantidade de letras presentes em "msg".
    print(msg) # Imprime-se "msg".
    print("=" * len(msg)) # Imprime-se "=" de acordo com a quantidade de letras presentes em "msg".


def contagem_de_números(): # Crio uma função def "contagem_de_números".
    print("+=" * 15) # Imprimo "+=" quinze vezes no terminal.
    print("Contagem de 1 até 10 de 1 em 1: ") # Imprimo uma mensagem "Contagem de 1 até 10 de 1 em 1: " no terminal.
    for c in range(1, 11): # Utilizo uma estrutura de repetição "for" que tem o começo "1" e tem o fim "11", ou seja, vai ter um looping de 1 até 10 de um em um.
        print(c, end = " ", flush=True) # Imprimo o "c" do "for", para cada looping, coloco um espaço em cada número com o "end = ' ' " e para o sleep funcionar, utiliza-se o "flush=True".
        sleep(1) # Uso a função "sleep" da bliblioteca "time", por conseguinte, a cada looping feito terá um segundo de espera.
    print("Fim da contagem! ") #Imprimo uma mensagem "Fim da contagem! ".
    print("+=" * 15) # Imprimo "+=" quinze vezes no terminal.
    print("Contagem de 10 até 0 de 2 em 2: ") # Aqui, imprime-se a mensagem "Contagem de 10 até 0 de 2 em 2: ". Logo, será outra contagem.
    for c in range(10, -1, -2): # Utilizo uma estrutura de repetição "for" que tem o começo "10" e o final "-1" e vai pular de "-2". Ou seja, vai ter um looping que vai de 10 até 0 pulando de 2 em 2.
        print(c, end = " ", flush=True) # Imprimo o "c" do "for", para cada looping, coloco um espaço em cada número com o "end = ' ' " e para o sleep funcionar, utiliza-se o "flush=True".
        sleep(1) # Uso a função "sleep" da bliblioteca "time", por conseguinte, a cada looping feito terá um segundo de espera.
    print("Fim da contagem! ") # Imprimo a mensagem "Fim da conntagem! ".
    print("+=" * 15) # Imprimo "+=" quinze vezes no terminal.


def contagem_de_números_personalizada(i, f, p): # Crio uma função def "contagem_de_números_personalizada" o qual tem os parâmetros "i","f" e "p".
    print("<< AGORA É SUA VEZ GAFANHOTO(A) >>") # Imprimo uma mensagem "<< AGORA É SUA VEZ GAFANHOTO(A) >>".
    if i > f: # Utilizo uma estrutura de condição "if" que tem "i > f", ou seja, se o início que foi digitado for maior que o final, logo terá que fazer essa sequência...
        if p > 0: # Dentro da outra estrutura de condição "if", utiliza-se outro "if", porém, agora é necessário que o "p > 0", ou seja, o passo digitado terá que ser maior que zero para seguir com os próximos passos...
            passo_convertido = - p # Crio uma variável local chamado "passo_convertido" e atribuo o valor de transformar o passo em negativo.
            p = passo_convertido # Aqui, declaro que a variável local "p" poderá ser igual a variável local "passo_convertido"
            final_menos_um = f - 1 # Cria-se mais uma variável local chamada "final_menos_um" e atribuo o valor de "f - 1", ou seja, o final irá ser subtraído por 1, sendo assim,  o "for" vai ir de acordo com final digitado.
            f = final_menos_um # Aqui, declaro que a variável local "f" poderá ser igual a variável local "final_menos_um".
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de {- p} em {- p}: ") # Aqui é necessário saber um pouco de matemática. Chamo a função "def" lá de cima "mensagem_com_linhas" o qual vai criar uma estrutura de linhas com a mensagem. Outrossim, vai mostrar a sequência do início até o fim e passo, porém no "passo" coloquei denovo o sinal "-" para virar positivo e no "fim", acrescentei "+1" para ir com o valor correto.
        elif p < 0: # Dentro da outra estrutura de condição "if", utiliza-se o "elif", porém, agora é necessário que o "p < 0", ou sejam o passo digitado terá que ser nagativo para seguir com os próximos passos...
            final_menos_um = f - 1 # Cria-se uma variável local chamada "final_menos_um" e atribuo o valor de "f - 1", ou seja, o final irá ser subtraído por 1, sendo assim, o "for" vai ir de acordo com o final digitado.
            f = final_menos_um # Aqui, declaro que a variável local "f" poderá ser igual a variável local "final_menos_um".
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de {- p} em {- p}: ") # Chamo a função "def" que é "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada com linhas e dentro dela terá uma mensagem que vai mostrar a contagem do ínicio, o fim + 1 e transformo o passo em positivo novamente.
        else: # Dentro da outra estrutura de condição "if", utiliza-se o "else", porém, agora se nem o "p" for maior que zero e nem "p" for menor que zero, terá que seguir os seguintes passos...
            p = -1 # A variável local "p" agora terá o valor de "-1".
            final_menos_um = f - 1 # Cria-se uma variável local chamada "final_menos_um" e atruibuo o valor de "f - 1", ou seja, o final irá ser subtraído por 1, sendo assim, o "for" vai ir de acordo com o final digitado.
            f = final_menos_um # Aqui, declaro que a varíavel local "f" poderá ser igual a variável local "final_menos_um".
            mensagem_com_linhas(f"Contagem de {i} até {f + 1} de 1 em 1: ") # Chamo a função "def" que é "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada com linhas e dentro dela terá uma contagem que irá ter o início, o fim + 1 e o passo de um em um.
    else: # Utilizo uma estrutura de condição "else", ou seja, se o "i" não for maior que o "f", logo fazerá essa sequência de passos...
        if p > 0: # Dentro da outra estrutura de condição "else", utiliza-se o "if", ou seja, se o "p > 0" irá fazer essa sequência...
            final_mais_um = f + 1 # Cria-se uma variável local chamada "final_mais_um" e atribuo o valor de "f + 1", ou seja, o final irá ser somado por 1, sendo assim, o "for" vai ir de acordo com o final digitado.
            f = final_mais_um # Aqui, declaro que a variável local "f" poderá ser igual a variável local "final_mais_um".
            mensagem_com_linhas(f"Contagem de {i} até {f - 1} de {p} em {p}: ") # Chamo a função "def" que é "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada com linhas e dentro dela irá fazer uma contagem do início até o final - 1 de passo em passo.
        elif p < 0: # Dentro da outra estrutura de condição "else", utiliza-se o "elif", ou seja, se o "p < 0", logo irá fazer essa sequência...
            passo_convertido = - p # Crio uma variável local chamado "passo_convertido" e atribuo o valor de transformar o passo em positivo.
            p = passo_convertido # Aqui, declaro que a variável local "p" poderá ser igual a variável local "passo_convertido".
            final_mais_um = f + 1 # Cria-se uma variável local chamada "final_mais_um" e atribuo o valor "f + 1", ou seja, o final irá ser somado por 1, sendo assim, o "for" vai ir de acordo com final digitado.
            f = final_mais_um # Aqui, declaro que a variável local "f" poderá ser igual a variável local "final_mais_um".
            mensagem_com_linhas(f"Contagem de {i} até {f - 1} de {p} em {p}: ") # Chamo a função "def" que é "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada com linhas e dentro dela terá uma contagem do início até o final -1 de passo em passo.
        else: # Dentro da outra estrutura de condição "else", utiliza-se outro "else", ou seja, se "p" não for maior que zero ou "p" não for menor que zero, o "p" será zero, logo seguirá os seguintes passos...
            p = 1 # A variável local "p", terá valor de "1".
            final_mais_um = f + 1 # Cria-se uma variável local "final_mais_um" e atribuo o valor "f + 1", ou seja, o final irá ser somado por 1, sendo assim, o "for" vai ir de acordo com o final digitado.
            f = final_mais_um # Aqui, declaro que a variável local "f" poderá ser igual a variável local "final_mais_um".
            mensagem_com_linhas(f"Contagem de {i} até {f - 1} de 1 em 1: ") # Chamo a função "def" que é chamado "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada com linhas e dentro dela terá uma contagem do início até o final -1 de 1 em 1.
    for c in range(i, f, p): # Utilizo uma estrutura de repetição "for" e dento dela, o valor inicial será o "i", o final será "f" e o passo será "p".
        print(c, end = " ", flush=True) # Imprimo o "c" do "for", para cada looping, coloco um espaço em cada número com o "end = ' ' " e para o sleep funcionar, utiliza-se o "flush=True".
        sleep(1) # Uso a função "sleep" da bliblioteca "time", por conseguinte, a cada looping feito terá um segundo de espera.
    print("Fim da contagem! ") # Imprimo a mensagem "Fim da conntagem! ".


nome_do_gafanhoto = str(input("Digite seu nome, gafanhoto(a): ")).strip().upper() # Aqui eu crio uma variável global "nome_do_gafanhoto" e atribuo um valor de input(), ou seja, vai perguntar o nome ao usuário.
while True: # Utilizo a estrutura de repetição "while True", logo, só irá parar se a condição for falsa.
    mensagem_com_linhas(f"Olá, {nome_do_gafanhoto.title()} escolha uma dessas opções para prosseguir: ") # Chamo a função "def" que é chamado "mensagem_com_linhas" o qual vai fazer uma mensagem personalizada e dentro dela terá um menu de opções.
    print("""[ 1 ] Contagem de 1 até 10 de 1 em 1 e Contagem de 0 até 10 de 2 em 2
[ 2 ] Contagem personalizada """)
    choice = int(input(f"{nome_do_gafanhoto.title()}, escolha uma das opções acima: ").strip()) # Crio uma variável local chamado "choice" e atribuo o valor de input(), ou seja, vai perguntar ao usuário qual opção será escolhida.
    sleep(1.5) # Uso a função "sleep" da bliblioteca "time", por conseguinte, a cada looping feito terá um segundo e meio de espera.
    if choice == 1: # Utilizo uma estrutura de condição "if", ou seja, se o usuário digitar na variável local "choice" o valor "1", irá fazer os seguintes passos...
        contagem_de_números() # Irá chamar/declarar a função "def" que é chamada "contagem_de_números".
    elif choice == 2: # Utilizo uma estrutura de condição "elif", ou seja, se o usuário digitar na variável local "choice" o valor "2", irá fazer os seguintes passos...
        valor_inicial = int(input("Digite o valor inicial da contagem: ").strip()) # Aqui eu crio uma variável local chamado "valor_inicial", logo, atribuo o valor de input(), ou seja, perguntará ao usuário qual será o início da contagem.
        valor_final = int(input("Digite o valor final da contagem: ").strip()) # Aqui eu crio uma variável local chamado "valor_final", logo, atribuo o valor de input(), ou seja, perguntará ao usuário qual será o final da contagem.
        valor_passo = int(input("Digite a quantidade de passos que a contagem deverá fazer: ").strip()) # Aqui eu crio uma variável local chamado "valor_passo", logo, atribuo o valor de input(), ou seja, perguntará ao usuário qual será o passo da contagem.
        contagem_de_números_personalizada(i=valor_inicial, f=valor_final, p=valor_passo) # Irá chamar/declarar a função "def" que é chamada de "contagem_de_números_personalizada" e dentro dela deixo bem claro, que o "i = valor_inicial", "f = valor_final" e "p = valor_passo".
    else: # Utilizo uma estrutura de condição "else", ou seja, se o usuário não digitar os valores "1" ou "2", irá fazer os seguintes passos...
        print("Comando inválido! Encerrando o programa... ") # Imprime-se uma mensagem de comando inválido que está encerrando o programa.
        break # Ela encerra o looping e vai direto para a mensagem final.
    choice_two = str(input(f"{nome_do_gafanhoto.title()}, você deseja continuar escolhendo? [S/N]: ")).strip()[0] # Crio uma variável local "choice_two" e atribuo o valor de input(), ou seja, vai perguntar ao usuário se ele vai continuar no programa.
    if choice_two in "Ss": # Utilizo uma estrutura de condição "if", logo, se o usuário digitar "S" ou "s", irá fazer os seguintes passos...
        print("Continuando o programa... ") # Imprime-se uma mensagem de continuando o programa.
        continue # Continua o programa
    elif choice_two in "Nn": # Utilizo uma estrutura de condição "elif", logo, se o usuário digitar "N" ou "n", irá fazer os seguintes passos...
        print("Encerrando o programa... ") # Imprime-se uma mensagem de encerrando o programa.
        break # Vai encerrar o looping e vai direto para a mensagem final.
    else: # Utilizo uma estrutura de condição "else", logo, se o usuário não digitar "Ss" ou "Nn", irá fazer os seguintes passos...
        print("Comando inválido! Encerrando o programa... ") # Imprime-se uma mensagem de comando inválido e encerra o programa.
        break # Vai encerrar o looping e vai direto para a mensagem final.
sleep(3) # Uso a função "sleep" da bliblioteca "time", por conseguinte, após o looping acabar terá 3 segundos de espera.
mensagem_com_linhas("<< Programa finalizado >>") # Chama/Declara a função "def" chamada "mensagem_com_linhas" e vai personalizar a mensagem colocada.
