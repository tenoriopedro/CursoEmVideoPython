'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input('Qual salário do funcionário? '))
if salario > 1250:
    print('Seu salário é de {:.2f}€, então receberá um aumento de 10%'.format(salario))
    print('Seu salário passará a ser {:.2f}€'.format(salario * (1 + 0.10)))
else:
    print('Seu salário e de {:.2f}€, então receberá um aumento de 15%'.format(salario))
    print('Seu salário passará a ser {:.2f}'.format(salario * (1 + 0.15)))
