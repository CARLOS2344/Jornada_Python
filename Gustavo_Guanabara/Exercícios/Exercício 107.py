from Gustavo_Guanabara.Utilities.Utilidades_CV import moeda
from Gustavo_Guanabara.Utilities.Mensagem_Personalizada import personalização


preço = float(input("Digite o preço: R$").strip())
personalização.mensagem_com_linhas(f"A metade de R${preço} é R${moeda.metade_do_número(preço)}! ")
personalização.mensagem_com_linhas(f"O dobro de R${preço} é R${moeda.dobro_do_número(preço)}! ")
personalização.mensagem_com_linhas(f"O valor aumentado em 10% é R${moeda.aumento_porcentagem(preço, 10)}! ")
personalização.mensagem_com_linhas(f"O valor diminuido em 13% é R${moeda.diminuição_porcentagem(preço, 13)}! ")
