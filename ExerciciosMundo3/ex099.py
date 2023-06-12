from time import sleep
def l():
    print('~' *30)

def maior(*num):
    higher = 0
    sleep(0.5)
    print('Analisando os valores passados...')
    sleep(2)
    if len(num) == 0:
        print('Não foi passado nenhum valor')
    else:
        print(f'Foram passados {len(num)} numeros e são eles:')
        for c in num:
            print(c, end=', ')
            if c == [0]:
                higher = c
            else:
                if c > higher:
                    higher = c
        print(f'e o maior número é o {higher}')
    l()
    sleep(4)
maior(1, 2, 4, 5)
maior(1, 9, 5,)
maior(1, 3)
maior()





