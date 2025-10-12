from random import randint # Importo a função "randint" da bliblioteca "random".
from time import sleep # Importo a função "sleep" da bliblioteca "time".
números = [] # Criei uma variável global chamada "números" e atribui o valor de uma lista.


def sorteia(lst_de_números_aleatórios): # Criei uma função "def" que é chamada "sorteia" e tem um parâmetro chamado "lst_de_números_aleatórios".
  for c in range(5): # Temos uma estrutura de repetição "for" e vai ter looping 5 vezes.
    random_numbers = randint(0, 10) # Criei uma variável local "random_numbers" e atribui o valor da função "randint" da bliblioteca "random". Ou seja, vai pegar números de 0 a 10 de forma aleatória.
    números.append(random_numbers) # Dos números sorteados, vai ser colocado na lista "números".
  print("+=" * 25) # Imprime-se "+=" vinte e cinco vezes.
  print("Sorteando 5 números aleatórios: ") # Imprime-se a mensagem "Sortenado 5 números aleatórios: "
  for e in lst_de_números_aleatórios: # Temos outra estrutura de repetição "for" o qual vai pegar a quantidade de elementos do parâmetro "lst_de_números_aleatórios".
    print(e, end = " ", flush=True) # Imprime-se o elemento do estrutura de repetição "for". Outrossim, para cada número digitado no terminal, coloca-se um espaço entre eles com o "end = ' ' " e tem o "flush=True" para a função "sleep" da bliblioteca "time".
    sleep(0.5) # Utilizo a função "sleep" da bliblioteca "time", logo, a cada looping terá uma pausa de 0.5 segundos.
  print("Fim!") # Imprime-se a mensagem "Fim!"
  print("+=" * 25) # Imprime-se "+=" vinte e cinco vezes.


def somaPAR(lst_somando_pares): # Criei uma função "def" que é chamda "somaPAR" e tem um parâmetro "lst_somando_pares".
  soma_de_pares = 0 # Criei uma variável local "soma_de_pares" e atribui o valor em "zero".
  for e in lst_somando_pares: # Temos uma estrutura de repetição "for", logo, pegará todos os elementos do parâmetro "lst_somando_pares".
    if e % 2 == 0: # Aqui, tem-se uma estrutura de condição "if", logo, para cada elemento do parâmetro "lst_somando_pares", se for par, irá fazer os seguintes passos...
      soma_de_pares += e # Da variável local "soma_de_pares" coloquei o valor de soma. Ou seja, para cada elemento do parâmetro "lst_somando_pares", ele vai ficar somando os números pares.
  print("+=" * 35) # Imprime-se "+=" trinta e cinco vezes.
  print(f"[ {lst_somando_pares} ] É a lista completa tendo o total de {len(lst_somando_pares)} elementos.") # Imprime-se a mensagem mostrando a lista completa e a quantidade de elementos.
  print("=" * 45) # Imprime-se "+=" quarenta e cinco vezes.
  print(f"[ {soma_de_pares } ] É a soma total dos pares que a lista tem!") # Imprime-se a mensagem mostrando a soma total dos números pares da lista.
  print("+=" * 35) # Imprime-se "+=" trinta e cinco vezes.


sorteia(números) # Chama/Declara a função "def" que é chamada de "sorteia". Logo, a lista "números" será colocada dentro de "sorteia".
somaPAR(números) # Chama/Declara a função "def" que é chamada de "somaPAR". Logo, a lista "números" será colocada dentro de "somaPAR".
