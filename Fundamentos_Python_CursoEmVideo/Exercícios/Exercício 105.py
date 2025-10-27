def notas(*n, sit=False): # Criei uma função "def" que é chamada "notas" o qual tem os parâmetros "*n" e "sit" com o valor opcional "False".
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    notas_dos_alunos = {} # Dentro da função, criei uma variável com escopo local chamado "notas_dos_alunos" e atribui um valor de dicionário.
    notas_dos_alunos["total"] = len(n) # Aqui eu pego o total de notas e coloco dentro do dicionário.
    notas_dos_alunos["maior"] = max(n) # Aqui eu pego o maior valor e coloco no dicionário.
    notas_dos_alunos["menor"] = min(n) # Aqui eu pego o menor valor e coloco no dicionário.
    notas_dos_alunos["média"] = sum(n) / len(n) # Aqui eu pego a média das notas e coloco no dicionário.
    if sit == True: # Utilizo uma estrutura de condição "if", logo, se "Sit" for colocado como "True", fará os seguintes passos.
        if notas_dos_alunos["média"] >= 7: # Dentro da estrutura de condição "if", coloco outro "if" o qual se a média for maior ou igual a "7" fará os seguintes passos...
            notas_dos_alunos["situação"] = "BOA" # Colocará uma situação no dicionário o qual será "BOA".
        elif notas_dos_alunos["média"] >= 5: # Dentro da estrutura de condição "if", coloco um "elif", ou seja, se a média for maior ou igual a "5", fará os seguintes passos...
            notas_dos_alunos["situação"] = "RAZOÁVEL" # Colocará uma situação no dicionário o qual será "RAZOÁVEL".
        else: # Dentro da estrutura de condição "if", coloco um "else", ou seja, se não for maior ou igual a "7", fará os seguintes passos...
            notas_dos_alunos["situação"] = "RUIM" # Colocará uma situação no dicionário o qual será "RUIM".
    return notas_dos_alunos # Vai retornar o dicionário para o usuário.


resp = notas(5.5, 9.5, 10, 6.5, sit=True) # Chamo a função "def" que é "notas" e coloco as notas e mando mostrar a situação do indivíduo.
print(resp) # Imprime-se o resultado final.