resp = {}

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situação dos alunos
    :param num: Recebe uma ou mais notas de um aluno
    :param sit: valor opcional, indicará se vai ou não mostrar a situação do aluno
    :return: Um dicionário com as informações do aluno
    """
    soma = 0
    tot = 0
    maior = menor = 0
    for c in range(0, len(num)):
        if c == 0 :
            maior = num[c]
            menor = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
            if num[c] < menor:
                menor = num[c]
        tot += 1
        soma += num[c]
    resp['total'] = tot
    resp['maior'] = maior
    resp['menor'] = menor
    resp['média'] = soma / tot
    # abaixo de 5 RUIM, entre 5 e 7 RAZOAVEL, acima de 7 BOA
    if sit:
        if resp['média'] >= 7.0:
            resp['situação'] = 'BOA'
        elif resp['média'] < 5.0:
            resp['situação'] = 'RUIM'
        else:
            resp['situação'] = 'RAZOAVEL'

notas(5.5, 8.5, 7.5, 7, sit=False)
print(resp)