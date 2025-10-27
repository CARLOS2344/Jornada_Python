from datetime import date # Da bliblioteca "datetime" importo a função "date".
ano_atual = date.today().year # Crio uma variável global chamada "ano_atual" e ela vai pegar o ano atual(2025).


def voto(ano): # Crio uma função "def" que é chamada "voto" o qual tem o parâmetro "ano".
  if 16 <= ano_atual - ano < 18 or ano_atual - ano > 60: # Utilizo uma estrutura de condição "if", logo, se a subtração das variáveis "ano_atual" e "ano" forem entre 16 até 17 anos ou for maior que 60 anos, fará os seguintes passos...
    return "VOTO OPICIONAL!" # Retorna para o usuário a mensagem "VOTO OPCIONAL!".
  elif ano_atual - ano >= 18: # Utilizo uma estrutura de condição "elif", logo, se a subtração das variáveis "ano_atual" e "ano" forem maiores ou igual a "18", fará os seguintes passos...
    return "VOTO OBRIGATÓRIO!" # Retorna para o usuário a mensagem "VOTO OBRIGATÓRIO!".
  else: # Utilizo uma estrutura de condição "else", logo, se não for nenhuma das opções a cima, fará os seguintes passos...
    return "NÃO PODE VOTAR!" # Retorna para o usuário a mensagem "NÃO PODE VOTAR!".


nome_da_pessoa = str(input("Digite seu nome: ")).strip().upper() # Crio uma variável global chamada "nome_da_pessoa" e atribuo a função "input()", ou seja, perguntará ao usuário o nome dele.
ano_de_nascimento = int(input(f"{nome_da_pessoa.title()}, digite o ano que você nasceu: ").strip()) # Crio uma variável global chamada "ano_de_nascimento" e atribuo a função "input()", ou seja, perguntará ao usuário a data de nascimento dele.
print(f"{nome_da_pessoa.title()}, você tem {ano_atual - ano_de_nascimento} anos. Portanto, {voto(ano_de_nascimento)}") # Imprime-se o valor final de tudo, com nome, idade e situação de votação.