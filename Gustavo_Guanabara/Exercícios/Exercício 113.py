from Utilities.Utilidades_CV import leiaint, leiafloat
from Utilities.Mensagem_Personalizada import mensagem_com_linhas

valor_int = leiaint("Digite um número inteiro: ")
valor_float = leiafloat("Digite um número decimal: ")
mensagem_com_linhas(f"Você acabou de digitar o número inteiro {valor_int}! ")
mensagem_com_linhas(f"Você acabou de digitar o número decimal {valor_float}! ")
print("<<Programa finalizado>> ")