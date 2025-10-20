from uteis import numeros # Como se pode observar, importei uma bliblioteca do meu próprio arquivo "numeros". Vale-se ressaltar que o uso do "from uteis import numeros" pode-se ser útil e ágil, poupando tempo do código.
número = int(input("Digite um número: ").strip())
fatorial = numeros.fatorial_de_um_número(número)
print(f"O fatorial de {número} é {fatorial}! ")
print(f"O dobro de {número} é {numeros.dobro(número)}! ")
print(f"O triplo de {número} é {numeros.triplo(número)}! ")
#Com isso, posso economizar linhas dos meus códigos. Colocar várias linhas de códigos no mesmo lugar é bagunçado e nem um pouco didático. Chamando-se assim, modularização.
#Posso criar pacotes para organizar minhas modularizações, para isso, é necessário que tenha o "__init__.py" criado, pois determina que uma determinada pasta é do tipo python(.py)
#Vale ressaltar que o __init__.py inicializa o código primeiro, utiliza-se muito para colocar/importar blibliotecas dentro dele para simplificação.
