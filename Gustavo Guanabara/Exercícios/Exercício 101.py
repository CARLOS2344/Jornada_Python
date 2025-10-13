import datetime
ano_atual = datetime.date.today().year


def voto(ano):
  if ano_atual - ano >= 60:
    return "VOTO OPICIONAL!"
  elif ano_atual - ano >= 18:
    return "VOTO OBRIGATÓRIO!"
  else:
    return "NÃO PODE VOTAR!"


nome_da_pessoa = str(input("Digite seu nome: ")).strip().upper()
ano_de_nascimento = int(input(f"{nome_da_pessoa.title()}, digite o ano que você nasceu: ").strip())
print(f"{nome_da_pessoa.title()}, você tem {ano_atual - ano_de_nascimento} anos. Portanto, {voto(ano_de_nascimento)}")


