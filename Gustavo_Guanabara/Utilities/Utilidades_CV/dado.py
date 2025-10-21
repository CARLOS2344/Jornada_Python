from Gustavo_Guanabara.Utilities.Mensagem_Personalizada import personalização
def leiadinheiro(msg):
  """
  -> Valida a entrada de um valor monetário, aceitando vírgula como decimal.
  :param msg: (str) A mensagem que será exibida para o usuário.
  :return: (float) O valor numérico inserido.
  """
  while True:
    num_str = str(input(msg).strip().replace(',', '.'))
    if num_str.replace('.', '', 1).isdigit():
      return float(num_str)
    else:
      print(f'\033[0;31mERRO! "{num_str}" não é um preço válido! Tente novamente.\033[m')
