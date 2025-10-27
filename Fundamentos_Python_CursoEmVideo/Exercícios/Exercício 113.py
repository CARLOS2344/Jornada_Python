from Utilities.Utilidades_CV import leiaint, leiafloat # Da pasta Utilities, dentro dela, a pasta Utilidades_CV, importa-se dento do "__init__.py" as funções "leiaint" e "leiafloat".
from Utilities.Mensagem_Personalizada import mensagem_com_linhas # Da pasta Utilities, dentro dela, a pasta Mensagem_Personalizada, importa-se dentro do "__init__.py" a função "mensagem_com_linhas".

valor_int = leiaint("Digite um número inteiro: ") # Peço para o usuário com o "input()" digitar um número inteiro, logo, vai direto para a função "leiaint".
valor_float = leiafloat("Digite um número decimal: ") # Peço para o usuário com "input()" digitar um número decimal, logo, vai direto para função "leiafloat".
mensagem_com_linhas(f"Você acabou de digitar o número inteiro {valor_int}! ") # Aqui, chamo a função "mensagem_com_linhas" e crio uma mensagem personalizada com linhas o qual chama a variável "valor_int".
mensagem_com_linhas(f"Você acabou de digitar o número decimal {valor_float}! ") # Aqui, chamo a função "mensagem_com_linhas" e crio uma mensagem personalizada com linhas o qual chama a variável "valor_float".
print("<<Programa finalizado>> ") # Imprime-se a mensagem de encerramento do programa.
