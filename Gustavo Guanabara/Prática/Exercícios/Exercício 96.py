def mensagem_com_linhas(msg):
    print("=" * len(msg))
    print(msg)
    print("=" * len(msg))


def área_do_retângulo(c, l):
    área = c * l
    print(f"{nome_do_gafanhoto.title()}, os seus valores foram os seguintes: Comprimento = {c}m e Largura = {l}m. A área do retângulo é {área}m²")


nome_do_gafanhoto = str(input("Digite seu nome gafanhoto(a): ")).strip().upper()
mensagem_com_linhas(f"Olá, {nome_do_gafanhoto.title()}. Iremos fazer um programa que vai calcular a área de um retângulo de acordo com o comprimento x largura fornecidos. ")


comprimento = float(input("Digite o Comprimento(m) do retângulo: ").strip())
largura = float(input("Digite a Largura(m) do retângulo: ").strip())
área_do_retângulo(comprimento, largura)