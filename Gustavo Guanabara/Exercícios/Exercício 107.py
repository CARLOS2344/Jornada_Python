import sys
import os

# Adiciona o diretório-pai (JORNADA_PYTHON) ao caminho
# Isso permite que o Python encontre a pasta "Utilities"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora sim a importação funciona
from Utilities.Utilidades_CV import moeda
from Utilities.Mensagem_Personalizada import personalização

# ... resto do seu código ...
preço = float(input("Digite o preço: R$").strip())
personalização.mensagem_com_linhas(f"A metade de R${preço} é R${moeda.metade_do_número(preço)}! ")
personalização.mensagem_com_linhas(f"O dobro de R${preço} é R${moeda.dobro_do_número(preço)}! ")
personalização.mensagem_com_linhas(f"O valor aumentado em 10% é R${moeda.aumento_porcentagem(preço, 10)}! ")
personalização.mensagem_com_linhas(f"O valor diminuido em 13% é R${moeda.diminuição_porcentagem(preço, 13)}! ")
