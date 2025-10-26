from Utilities.Mensagem_Personalizada import mensagem_com_linhas


def leiaint(num_inteiro="Digite um número inteiro: "):
    while True:
        try:
            num = input(num_inteiro).strip()
            return int(num)
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m ")
        except KeyboardInterrupt:
            print("\n\033[0;31mO usuário preferiu não digitar esse número.\033[m ")
            return 0


def leiafloat(num_decimal="Digite um número decimal: "):
    while True:
        try:
            num_convertido = input(num_decimal).strip().replace(",",".")
            return float(num_convertido)
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Por favor, digite um número decimal válido.\033[m ")
        except KeyboardInterrupt:
            print("\n\033[0;31mO usuário preferiu não digitar esse número.\033[m ")
            return 0