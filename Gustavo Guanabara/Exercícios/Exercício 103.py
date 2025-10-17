def mensagem_com_linhas(msg): # Crio uma função "def" chamada "mensagem_com_linhas" que tem o parâmetro "msg".
    print("=" * len(msg)) # Imprime-se "=" de acordo com a quantidade de letras que "msg" tiver.
    print(msg) # Imprime-se "msg".
    print("=" * len(msg)) # Imprime-se "=" de acordo com a quantidade de letras que "msg" tiver.


def ficha_do_jogador(nome="<desconhecido>", gols=0): # Crio uma função "def" chamada "ficha_do_jogador" que tem os parâmetros "nome" que tem o valor opcional "<desconhecido>" e "gols" que tem o valor opcional "0".
    """
    -> Mostra a ficha de um jogador.
    :param nome: (opcional) O nome do jogador.
    :param gols: (opcional) O número de gols marcados.
    :return: A string formatada com os dados do jogador.
    """
    return f"O jogador {nome} fez {gols} gol(s) no campeonato." # Retorna para o usuário todas as informações do jogador.


nome_jogador = str(input("Nome do Jogador: ")).strip().title() # Pergunto ao usuário o nome dele. Outrossim, vale-se observar, que o valor será uma "string".
gols_jogador = str(input("Número de Gols: ")).strip() # Pergunto ao usuário o número de gols dele. Ademais, vale-se observar, que o valor será uma "string".

if gols_jogador.isnumeric(): # Uitlizo uma estrutura de condição "if", logo, se o valor digitado em "gols_jogador" for numérico, fará os seguintes passos...
    gols_jogador = int(gols_jogador) # Transforma uma string em valor "int".
else: # Utilizo uma estrutura de condição "else", logo, se o valor não for numérico, fará os seguintes passos...
    gols_jogador = 0 # Transforma automaticamente o valor em "0".
if nome_jogador == "": # Utilizo uma estrutura de condição "if", logo, se o valor digitado em "nome_jogador" for vazia, fará os seguintes passos...
    print(ficha_do_jogador(gols=gols_jogador)) # Imprime-se apenas os gols do jogador.
else: # Utilizo uma estrutura de condição "else", logo, se não estiver vazia, fará os seguintes passos...
    print(ficha_do_jogador(nome_jogador, gols_jogador)) # Imprime-se a ficha completa do jogador, com nome e gols feitos.