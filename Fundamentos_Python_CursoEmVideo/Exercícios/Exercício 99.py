from time import sleep # Pego a função "time" da bliblioteca "time".


def maior(* num): # Crio uma função "def" chamada "maior" que tem um parâmetro de desempacotamento, ou seja, vai pegar todos os números de para cada vez que a função for declarada.
    if num == (): # Utilizo uma estrutura de condição "if" que por sua vez, se o parâmetro "num" for vazio, ou seja, não tiver nada "()", irá fazer a seguinte sequência...
        print("Nenhum valor foi passado! ") # Imprime-se uma mensagem de nenhum valor foi passado.
        print("Logo o valor será 0! ") # Imprime-se uma mensagem de valor 0.
    else: # Utilizo uma estrutura de condição "else" que por sua vez, se o parâmetro "num" não for vazio, seguirá com os seguintes passos...
        tupla_transformada_em_lista = [] # Crio uma variável local chamado "tupla_transformada_em_lista" e atribuo o valor dela em uma lista.
        print("+=" * 30) # Imprime-se "+=" trinta vezes.
        print("Analisando os valores passados... ") # Imprime-se uma mensagem de analisar os valores passados.
        for valor in num: # Utilizo uma estrutura de repetição "for", logo, a cada "valor" que estiver em "num", irá fazer esses seguintes passos em looping até acabar...
            tupla_transformada_em_lista.append(valor) # Vai adicionar os valores na lista "tupla_transformada_em_lista".
            print(valor, end = " ", flush=True) # Imprime-se o "valor" e para cada número, tem um espaçamento. Utiliza-se o "end = ' ' " e o "Flush=True" para a bliblioteca "time".
            sleep(0.5) # Utilizo a função "Sleep" da bliblioteca "time" para cada looping feito, terá uma espera de meio segundo.
        print(f"Foram informados {len(tupla_transformada_em_lista)} valores ao todo.") # Imprime-se uma mensagem que vai falar a quantidade de elementos.
        print(f"O maior valor encontrado foi {max(tupla_transformada_em_lista)}! ") # Imprime-se o maior valor.
        print("+=" * 30) # Imprime-se "+=" trinta vezes.


maior(1, 2, 4, 6, 10, 100, -2 , 4) # Chama/Declara a função "def" que é chamada "maior" e terá os valores "1, 2, 4, 6, 10, 100, -2, 4".
maior(10, 2, 4, 5, 99) # Chama/Declara a função "def" que é chamada "maior" e terá os valores "10, 2, 4, 5, 99".
maior(1, 2) # Chama/Declara a função "def" que é chamada "maior" e terá os valores "1, 2".
maior(6) # Chama/Declara a função "def" que é chamada "maior" e terá o valor "6".
maior() # Chama/Declara a função "def" que é chamada "maior" e não tem nenhum valor.
