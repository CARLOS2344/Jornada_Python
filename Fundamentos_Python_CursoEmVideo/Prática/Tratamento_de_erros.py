try: # Utiliza-se o "try" para colocar toda a codificação do código, ou seja, ele vai tentar realizar a ação.
    #Programa principal
    número_um = float(input("Digite o primeiro número: ").strip())
    número_dois = float(input("Digite o segundo número: ").strip())
    divisão_de_dois_números = número_um / número_dois
except(ValueError, TypeError): # O "except" é utilizado para substituir a mensagem de erro para algo mais amigável e personalizado. Logo, se o usuário não digitar nada ou um valor que não seja numérico, fará os seguintes passos...
    print("Tivemos um problema com os tipos de dados que você digitou! ") # Mensagem substituindo o "ValueError" e "TypeError"
except ZeroDivisionError: # Aqui segue a mesma lógica do "except" anterior, porém, se o usuário colocar zero na divisão, fará os seguintes passos...
    print("Não é possível dividir um número por zero! ") # Mensagem substituindo o "ZeroDivisionError".
except KeyboardInterrupt: # Aqui segue a mesma lógica dos "except" anteriores, porém, se o usuário digitar o primeiro número e deixar vázio o outro, fará os seguintes passos...
    print("O usuário preferiu não informar os dados! ") # Mensagem substituindo o "KeyboardInterrupt".
else: # O "else" nessa situação, serve para caso o programa dá tudo certo, ou seja, não deu nenhum erro, logo, imprimirá os seguintes passos...
    print(f"O resultado da divisão entre {número_um} e {número_dois} é {divisão_de_dois_números:.1f}! ") # Mostrará o resultado da divisão.
finally: # O "finally" é sempre colocado no final, ou seja, dando erro ou não, irá fazer os seguintes passos...
    print("<<Volte sempre ao programa >>") # Mensagem de encerramento do programa.

#Vale ressaltar que existem outros tipos de "except", como por exemplo, o "except Exception as error", logo, poderá ser imprimido o tipo de erro para auxiliar o programador.