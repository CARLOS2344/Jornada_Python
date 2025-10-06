from time import sleep 
def maior(* num):
    if num == ():
        print("Nenhum valor foi passado! ")
        print("Logo o valor será 0! ")
    else:
        tupla_transformada_em_lista = []
        print("+=" * 30)
        print("Analisando os valores passados... ")
        for valor in num:
            tupla_transformada_em_lista.append(valor)
            print(valor, end = " ", flush=True)
            sleep(0.5)
        print(f"Foram informados {len(tupla_transformada_em_lista)} valores ao todo.")
        print(f"O maior valor encontrado foi {max(tupla_transformada_em_lista)}! ")
        print("+=" * 30)

    

maior(1, 2, 4, 6, 10, 100, -2 , 4)
maior(10, 2, 4, 5, 99)
maior(1, 2)
maior(6)
maior()