from Utilities.Utilidades_CV import situação_site
from Utilities.Mensagem_Personalizada import mensagem_com_linhas

url = situação_site("Digite o link do site: ").strip()
print(url)
mensagem_com_linhas("<<Programa finalizado>>")
