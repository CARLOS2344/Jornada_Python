def mensagem_adaptada_com_linhas(msg):
    mais_dois = len(msg) + 2
    print("=" * mais_dois)
    print(f" {msg.title()}")
    print("=" * mais_dois)


name = str(input("Digite seu nome, gafanhoto(a): ")).strip().upper()
frase_aleatória = str(input(f"{name.title()}, digite uma frase aleatória: ")).strip().upper()
mensagem_adaptada_com_linhas(frase_aleatória)
print("<< Programa finalizado >>")