def mensagem_com_linhas(msg): # Criei uma variável def "mensagem_com_linhas", que por sua vez tem o parâmetro "msg".
    print("=" * len(msg)) # Vai printar a "=" a quantidade de letras que "msg" tiver.
    print(msg) # Imprimi-se na tela a "msg".
    print("=" * len(msg)) # Vai printar a "=" a quantidade de letras que "msg" tiver


def área_do_retângulo(c, l): # Criei uma variável def "área_do_retângulo", que por sua vez tem os parâmetros "c" e "l".
    área = c * l # Criei uma variável local "área" que vai multiplicar os valores "c" x "l".
    print(f"{nome_do_gafanhoto.title()}, os seus valores foram os seguintes: Comprimento = {c}m e Largura = {l}m. A área do retângulo é {área}m²") # Vai imprimir a mensagem com os valores da Largura e Comprimento.


nome_do_gafanhoto = str(input("Digite seu nome gafanhoto(a): ")).strip().upper() # Criei uma variável "nome_do_gafanhoto" que vai perguntar qual será o nome do usuário.
mensagem_com_linhas(f"Olá, {nome_do_gafanhoto.title()}. Iremos fazer um programa que vai calcular a área de um retângulo de acordo com o comprimento x largura fornecidos. ") # Declarei a função "mensagem_com_linhas" e vai printar uma mensagem personalizada pelo def.


comprimento = float(input("Digite o Comprimento(m) do retângulo: ").strip()) # Criei uma variável "comprimento" que vai perguntar o comprimento do retângulo.
largura = float(input("Digite a Largura(m) do retângulo: ").strip()) # Criei uma variável "largura" que vai perguntar a largura do retângulo.
área_do_retângulo(comprimento, largura) #Aqui, coloco "comprimento" e "largura" na função "área_do_retângulo, logo, quando estiverem dentro da função def, terão valores "c" e "l", respectivamente.
