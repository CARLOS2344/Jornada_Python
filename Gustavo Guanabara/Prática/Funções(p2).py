from time import sleep # Importo a função "sleep" da bliblioteca "time".
help(print) # Podemos pedir ajuda para o próprio Python sobre a funcionalidade de algum comando. 


def teste(b):
    global a # Aqui, temos um novo comando "global". Ele vai pegar a variável "a" e vai transformá-la em global. Não tendo apenas a função de uma variável local.
    a = 8 # O valor "5" da variável "a" irá ser 8 nesse momento.
    b += 4
    c = 2
    print(f"A dentro vale {a} ")
    print(f"B dentro vale {b} ")
    print(f"C dentro vale {c} ")


a = 5
teste(a)
print(f"A fora vale {a} ") # Será retornado o valor "8".


def contagem_de_números(i, f, p):
    """
    O parâmetro i é equivalente ao início da contagem...
    O parâmetro f é equivalente ao final da contagem...
    O parâmetro p é equivalente ao passo da contagem... """
    print("Contagem de números...")
    for c in range(i, f, p):
        print(c, end = " ", flush=True)
        sleep(0.5)


help(contagem_de_números) # Como pode-se observar, se eu colocar três aspas duplas em uma frase após colocar o comando "def", posso colocar uma mensagem para guiar o usuário que estará usando o programa.


def somatório_de_três_números(a=0, b=0, c=0): #Como vocês podem perceber, temos três parâmetros "a", "b" e "c". Porém, eles estão com "=0", ou seja, o valor deles serão opicionalmente zero se não for declarado.
    """
    O parâmetro a é equivalente ao primeiro valor dado do usuário...
    O parâmetro b é equivalente ao segundo valor dado do usuário...
    O parâmetro c é equivalente ao terceiro valor dado ao usuário... """
    soma_de_valores = a + b + c
    print(f"A soma dos valores {a} + {b} + {c} é {soma_de_valores}!")


somatório_de_três_números(a=2, c=4) # Não declarei o valor "b", se não tivesse o "=0" como valor opcional, daria erro por não ter definido, porém como eu defini um valor opcional, o valor de "b" será zero.


def fatorial_de_um_número(num=1): # No parâmetro atribuí o valor opcional de "1". Logo, se não for declarado nada, o valor será "1".
    valor_final = 1
    for c in range(num, 0, -1):
        valor_final *= c
    return valor_final # O "valor_final" será retornado, quando declarado, para a variável "valor". Sendo assim, a função do "return".


valor = int(input("Digite um número: ").strip()) # Peço para o usuário digitar um número para fazer o fatorial.
print(f"O fatorial de {valor} é igual a {fatorial_de_um_número(valor)} ") # No final, faço "fatorial_de_um_número(valor)". Ou seja, falo para o programa que a variável "valor" deverá entrar dentro da função def e me retornar o valor final através do "return".


def verificação_de_pares_e_ímpares(num):
    if num % 2 == 0:
        return True # Se o valor for par, irá retornar como "True".
    else:
        return False # Se o valor for ímpar, irá retornar como "False".


número = int(input("Digite um número: ").strip())
if verificação_de_pares_e_ímpares(número): #Aqui tem a verificação pela estrutura de condição "if", ele vai analisar se o valor é "True". Logo, fazerá os seguintes passos...
    print("O número é PAR! ") # Imprime-se a mensagem dizendo que o valor é PAR.
else: # Aqui tem a verificação pela estrutura de condição "else", ele vai analisar se o valor é "False". Logo, fazerá os seguintes passos...
    print("O número é IMPAR! ") # Imprime-se a mensagem dizendo que o valor é IMPAR.