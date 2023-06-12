count = 0
soma = 0
opção = ''
maior = 0
menor = 0
while opção != 'n':
    numero = int(input('Digite um numero: '))
    soma += numero
    count += 1
    if count == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    opção = str(input('Quer continuar [S/N]: ')).strip().lower()
media = soma / count
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
print(f'Você digitou {count} números e media deles é {media:.2f}')

