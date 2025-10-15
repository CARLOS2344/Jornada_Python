def mensagem_com_linhas(msg):
    print("=" * len(msg))
    print(msg)
    print("=" * len(msg))


def ficha_do_jogador(nome="<desconhecido>", gols=0):
    """
    -> Mostra a ficha de um jogador.
    :param nome: (opcional) O nome do jogador.
    :param gols: (opcional) O número de gols marcados.
    :return: A string formatada com os dados do jogador.
    """
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


nome_jogador = str(input("Nome do Jogador: ")).strip().title()
gols_jogador = str(input("Número de Gols: ")).strip()

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador) # Transforma uma string em valor númerico.
else:
    gols_jogador = 0
if nome_jogador == "":
    print(ficha_do_jogador(gols=gols_jogador))
else:
    print(ficha_do_jogador(nome_jogador, gols_jogador))
