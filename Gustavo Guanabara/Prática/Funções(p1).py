def mensagem(msg): # Aqui temos uma função "def" que dentro dela terá um parâmetro "msg"
    print('=' * len(msg)) # Estou falando para ele imprimir "=" de acordo com o número de caracteres da frase
    print(msg) # Nesse momento, ele irá fazer toda essa estrutura de acordo com à mensagem que deverá ser declarada!
    print('=' * len(msg)) # Estou falando para ele imprimir "=" de acordo com o número de caracteres do parâmetro "msg"


mensagem("Olá Mundo, meu nome é Carlos Alberto da Silva Neto. ") # Nessa linha foi declarada à função "def" e o parâmetro "msg" deverá ter o conteúdo colocado.
mensagem("Python é muito ARRETADO! ") # Nessa linha foi declarada à função "def"...
mensagem("A IA é a minha melhor companheira! ") # Nessa linha foi declara à função "def"...


def soma_de_números(a, b): # Nessa linha, coloquei outra função "def" o qual tem os parâmetros "a" e "b"
    soma_total = a + b # Criei uma variável local "soma_total" dentro da função "def" e atribuí um valor de soma
    print(f"O valor de A é {a} e o valor de B é {b}. ") # Toda vez que for uma operação nova, mostrará quem é os parâmetros "a" e "b"
    print(f"O resultado da soma entre {a} e {b} é {soma_total} ") # Toda vez que for realizado uma soma será mostrado no terminal


soma_de_números(10, 20) # Chamo a função "def" e coloco nos parâmetros a = 10 e b = 20. Logo, 10 + 20 = 30
soma_de_números(100, 200) # Chamo a função "def" e coloco nos parâmetros a = 100 e b = 200. Logo, 100 + 200 = 300
soma_de_números(20, -40) # Chamo a função "def" e coloco nos parâmetros a = 20 e b = -40. Logo, 20 + (-40) = -20
soma_de_números(1000, -10) # Chamo a função "def" e coloco nos parâmetros a = 1000 e b = -10. Logo, 1000 + (-10) = 990

def subtração_de_números(a, b): # Nessa linha, coloquei outra função "def" o qual tem os parâmetros "a" e "b"
    subtração_total = a - b # Criei uma variável local "subração_total" dentro da função "def" e atribuí um valor de subtração
    print(f"O valor de A é {a} e o valor de B é {b}. ") # Toda vez que for uma operação nova, mostrará quem é os parâmetros "a" e "b"
    print(f"O resultado da subtração entre {a} e {b} é {subtração_total} ") # Toda. vez que for realizado uma subtração será mostrado no terminal


subtração_de_números(-10, 20) # Chamo a função "def" e coloco nos parâmetros a = -10 e b = 20. Logo, (-10) + (-20) = -30
subtração_de_números(b=-100, a=20) # Aqui acontece diferente, em vez de a = -100 e b = 20, os valores foram trocados. Logo, 20 - (-100) = 120
subtração_de_números(20, -40) # Chamo a função "def" e coloco nos parâmetros a = 20 e b = -40; Logo, 20 - (-40) = 60

def multiplicação_de_números(a, b): # Nessa linha, coloquei outra função "def" o qual tem os parâmetros "a" e "b"
    multiplicação_total = a * b # Criei uma variável local "multiplicação_total" dentro da função "def" e atribuí um valor de multiplicação
    print(f"O valor de A é {a} e o valor de B é {b}. ") # Toda vez que for uma operação nova, mostrará quem é os parâmetros "a" e "b"
    print(f"O resultado da multiplicação entre {a} e {b} é {multiplicação_total} ") # Toda vez que for realizado uma multiplicação será mostrado no terminal


multiplicação_de_números(10, 20) # Chamo a função "def" e coloco nos parâmetros a = 10 e b = 20. Logo, 10 * 20 = 200
multiplicação_de_números(100, -20) # Chamo a função "def" e coloco nos parâmetros a = 100 e b = -20. Logo, 100 * (-20) = -2000

def divisão_de_números(a, b): # Nessa linha, coloquei outra função "def" o qual tem os parâmetros "a" e "b"
    divisão_total = a / b # Criei uma variável local "divisão_total" dentro da função "def" e atribuí um valor de divisão
    print(f"O valor de A é {a} e o valor de B é {b}. ") # Toda vez que for uma operação nova, mostrará quem é os parâmetros "a" e "b"
    print(f"O resultado da divisão entre {a} e {b} é {divisão_total} ") # Toda vez que for realizado uma divisão será mostrado no terminal


divisão_de_números(10, 20) # Chamo a função "def" e coloco nos parâmetros a = 10 b = 20. Logo, 10 / 20 = 0.5


def contagem_de_números(* num): # Aqui, eu crio uma função "def" que tem como o parâmetro "* num", ou seja, vai pegar desempacotar a quantidade de valores, não se tornando limitado a uma quantidade fixa.
    print(f"Essa tupla tem os seguintes números: {num} e possui {len(num)} elementos. ") # Nesse momento, imprime-se os valores da contagem e mostra a quantidade de elementos.


contagem_de_números(1, 2, 3, 5, 7, 10, 40) # Chamo a função "def" e vai mostrar os resultados
contagem_de_números(10, 30, 0, 3, 5, 6, 7, 9, 5, 2, 1, 6) # Chamo a função "def" e vai mostrar os resultados


def dobrando_valores(lst): # Aqui, eu crio uma função "def" que tem como o parâmetro "lst", logo, todo valor que for entrar dentro da função "dobrando_valores" será conhecido como "lst"
    posição = 0 # Eu crio uma variável local chamado "posição" e atribuo o valor "0"
    while posição < len(lst): # Enquanto a posição for menor que a quantidade de elementos da lista, ele continuará a ação
        lst[posição] *= 2 # Vai pegar atribuir no parâmetro "lst" a posição e em seguida, vai multiplicar por 2
        posição += 1 # Aumenta a posição em um a cada vez que o looping acaba.


lista_de_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Criei uma variável global e atribuí o valor de uma lista com vários valores dentro dela
dobrando_valores(lista_de_valores) # É aqui que entra a parte importante de tudo, ela chama a função "dobrando_valores" e coloca à variável "lista_de_valores" dentro da função
print(lista_de_valores) # Vai mostrar o resultado final