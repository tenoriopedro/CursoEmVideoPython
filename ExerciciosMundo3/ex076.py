lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
print('-' *40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
#print(f'{lista[0]}............................R$    {lista[9]}')
#print(f'{lista[1]}.........................R$    {lista[10]:.2f}')
#print(f'{lista[2]}..........................R$   {lista[11]:.2f}')
#print(f'{lista[3]}...........................R$   {lista[12]:.2f}')
#print(f'{lista[4]}.....................R$    {lista[13]:.2f}')
#print(f'{lista[5]}.........................R$    {lista[14]:.2f}')
#print(f'{lista[6]}..........................R$  {lista[15]:.2f}')
#print(f'{lista[7]}..........................R$   {lista[16]:.2f}')
#print(f'{lista[8]}...........................R$   {lista[17]:.2f}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' *40)