# Aqui fica toda a codificação, ou seja, a parte funcional do código que serão exportados pelos "__init__.py".
def mensagem_com_linhas(msg): # Criei uma função "def" chamada "mensagem_com_linhas" que tem o parâmetro "msg".
    mais_quatro = len(msg) + 4 # Criei uma variável com escopo local chamada "mais_quatro". Logo, vai acrescentar mais quatro "=" de acordo com a quantidade de letras do parâmetro "msg".
    print("=" * mais_quatro) # Imprime-se "=" de acordo com a quantidade de letras que a variável local "mais_quatro" tiver.
    print(f"  {msg.title()}") # Imprime-se o parâmetro "msg" e terá uma formatação de "title()", ou seja, a cada início de frase, o primeiro caractére será maiúsculo.
    print("=" * mais_quatro) # Imprime-se "=" de acordo com a quantidade de letras que a variável local "mais_quatro" tiver.