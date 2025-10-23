from Utilities.Utilidades_CV import leiadinheiro # Da pasta "Utilities", dentro dela, a pasta "Utilidades_CV", importei o arquivo "dado.py" que já está importado no "__init__.py" da pasta "Utilidades_CV".
from Utilities.Utilidades_CV import resumo # Da pasta "Utilities", dentro dela, a pasta "Utilidades_CV", importei o arquivo "moeda2.py" que já está importado no "__init__.py" da pasta "Utilidades_CV".

preço = leiadinheiro("Digite o preço: R$") # Com a função "input()", mando o usuário digitar o preço do produto. Porém, essa ação vai diretamente para a função "leiadinheiro" do arquivo "dado.py".
resumo(preço, 35, 22) # Chamo a função "resumo" através do "__init__.py" da pasta "Utilidades_CV" e coloco o preço, aumento percentual e diminuição percentual.