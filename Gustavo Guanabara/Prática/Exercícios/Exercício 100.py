from random import randint
from time import sleep
números = []
def sorteia(lst_de_números_aleatórios):
  for c in range(5):
    random_numbers = randint(0, 10)
    números.append(random_numbers)
  print("+=" * 25)
  print("Sorteando 5 números aleatórios: ")
  for e in lst_de_números_aleatórios:
    print(e, end = " ", flush=True)
    sleep(0.5)
  print("Fim!")
  print("+=" * 25)


def somaPAR(lst_somando_pares):
  soma_de_pares = 0
  for e in lst_somando_pares:
    if e % 2 == 0:
      soma_de_pares += e
  print("+=" * 35)
  print(f"[ {lst_somando_pares} ] É a lista completa tendo o total de {len(lst_somando_pares)} elementos.")
  print("=" * 45)
  print(f"[ {soma_de_pares } ] É a soma total dos pares que a lista tem!")
  print("+=" * 35)


sorteia(números)
somaPAR(números)
