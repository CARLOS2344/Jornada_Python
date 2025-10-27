from Utilities.Utilidades_CV import situação_site # Da pasta Utilities, dentro dela, a pasta Utilidades_CV, importa-se dento do "__init__.py" a função "situação_site".
from Utilities.Mensagem_Personalizada import mensagem_com_linhas # Da pasta Utilities, dentro dela, a pasta Mensagem_Personalizada, importa-se dento do "__init__.py" as função "mensagem_com_linhas".

url = situação_site("Digite o link do site: ").strip() # Aqui, com o "input()" mando o usuário digitar o link do site que deseja verificar a situação. Logo, quando a ação é feita, manda-se para a função "situação_site".
print(url) # Imprime-se a situação do site.
mensagem_com_linhas("<<Programa finalizado>>") # Imprime-se a finalização do programa.
