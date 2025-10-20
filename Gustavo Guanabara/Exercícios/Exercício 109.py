import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Utilities.Utilidades_CV import moeda
from Utilities.Mensagem_Personalizada import personalização

preço = float(input("Digite o preço: R$").strip())
personalização.mensagem_com_linhas(f"O dobro de R${moeda.moeda(preço)} é R${moeda.dobro_do_número(preço, True)}! ")
personalização.mensagem_com_linhas(f"A metade de R${moeda.moeda(preço)} é R${moeda.metade_do_número(preço, True)}! ")
personalização.mensagem_com_linhas(f"O valor R${moeda.moeda(preço)} aumentado em 10% do seu valor é R${moeda.aumento_porcentagem(preço, 10, True)}! ")
personalização.mensagem_com_linhas(f"O valor R${moeda.moeda(preço)} diminuído em 13% do seu valor é R%{moeda.diminuição_porcentagem(preço, 13, True)}! ")