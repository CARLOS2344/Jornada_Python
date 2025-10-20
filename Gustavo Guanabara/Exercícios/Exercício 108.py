import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utilities.Utilidades_CV import moeda
from Utilities.Mensagem_Personalizada import personalização

preço = float(input("Digite o valor: R$").strip())
personalização.mensagem_com_linhas(f"O dobro de R${moeda.moeda(preço)} é o valor R${moeda.moeda(moeda.dobro_do_número(preço))}! ")
personalização.mensagem_com_linhas(f"O metade do valor R${moeda.moeda(preço)} é o valor R${moeda.moeda(moeda.metade_do_número(preço))}! ")
personalização.mensagem_com_linhas(f"O valor R${moeda.moeda(preço)} com 10% de aumento é o valor R${moeda.moeda(moeda.aumento_porcentagem(preço, 10))}! ")
personalização.mensagem_com_linhas(f"O valor R${moeda.moeda(preço)} com 13% de desconto é o valor R${moeda.moeda(moeda.diminuição_porcentagem(preço, 13))}! ")