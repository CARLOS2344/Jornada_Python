# Aqui fica toda a codificação, ou seja, a parte funcional do código que serão exportados pelos "__init__.py".
from Utilities.Mensagem_Personalizada import personalização # Da pasta "Utilities", dentro dela, a pasta "Mensagem_Personalizada", importo todas as funções do arquivo "personalização.py" através do "__init__.py". 


def leiadinheiro(msg): # Criei uma função "def" que é chamada "leiadinheiro" que tem o parâmetro "msg".
  """
  -> Valida a entrada de um valor monetário, aceitando vírgula como decimal.
  :param msg: (str) A mensagem que será exibida para o usuário.
  :return: (float) O valor numérico inserido.
  """
  while True: # Criei uma estrutura de repetição "While True", ou seja, enquanto o valor for "True", continuará no looping.
    num_str = str(input(msg).strip().replace(',', '.')) # Nessa linha, pego o parâmetro "msg" e atribuo o valor de "str", outrossim, utiliza-se a formatação "strip()" que vai tirar os espaços desnecessários e "replacee(","".")" o qual vai trocar a vírgula pelo ponto.
    if num_str.replace('.', '', 1).isdigit(): # Aqui coloco uma estrutura de condição "if", ou seja, verifica-se se a variável "num_str" é dígito, logo, com as formatações, tira-se os pontos, ficando um número inteiro. Se for "True", fará os seguintes passos...
      return float(num_str) # Retorna-se para o usuário a variável "num_str" convertido no valor "float".
    else: # Caso a condição for "False", fará os seguintes passos...
      print(f'\033[0;31mERRO! "{num_str}" não é um preço válido! Tente novamente.\033[m') # Manda uma mensagem de erro vermelha para o usuário, logo, pede-se para o usuário digitar novamente.