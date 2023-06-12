import random
n1 = input('Nome do aluno: ')
n2 = input('Do segundo: ')
n3 = input('Do terceiro: ')
n4 = input('Do quarto: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno sorteado é {}'.format(escolhido))
