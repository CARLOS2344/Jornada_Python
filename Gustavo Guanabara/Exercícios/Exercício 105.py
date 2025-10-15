def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    notas_dos_alunos = {}
    notas_dos_alunos["total"] = len(n)
    notas_dos_alunos["maior"] = max(n)
    notas_dos_alunos["menor"] = min(n)
    notas_dos_alunos["média"] = sum(n) / len(n)
    if sit == True:
        if notas_dos_alunos["média"] >= 7:
            notas_dos_alunos["situação"] = "BOA"
        else:
            notas_dos_alunos["situação"] = "RUIM"
    return notas_dos_alunos


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)