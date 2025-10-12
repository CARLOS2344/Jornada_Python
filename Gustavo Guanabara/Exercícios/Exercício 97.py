def mensagem_adaptada_com_linhas(msg): # Criei uma função def "mensagem_adaptada_com_linhas" que tem um parâmetro "msg"
    mais_dois = len(msg) + 2 # Criei uma variável local "mais_dois" que tem um "len(msg) + 2", ou seja, vai pegar a quantidade de letras em "msg" e vai somar por 2.
    print("=" * mais_dois) # Vai imprimir "=" de acordo com a variável "mais_dois".
    print(f" {msg.title()}") # Vai imprimir o parâmetro "msg" e dou dois espaços no parâmetro para alinhar com a variável "mais_dois"
    print("=" * mais_dois) # Vai imprimir "=" de acordo com a variável "mais_dois".


name = str(input("Digite seu nome, gafanhoto(a): ")).strip().upper() # Criei uma variável "name" o qual pergunta o nome do usuário.
frase_aleatória = str(input(f"{name.title()}, digite uma frase aleatória: ")).strip().upper() # Criei uma variável "frase_aleatória" o qual pergunta uma frase aleatória.
mensagem_adaptada_com_linhas(frase_aleatória) # Aqui, de acordo com o que foi digitado em "frase_aleatória" será colocado na função def "mensagem_adaptada_com_linhas" o qual vai ser transformada no parâmetro "msg".
print("<< Programa finalizado >>") #Imprime-se o fim do programa.
