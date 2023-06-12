parentesesABERTO = []
parentesesFECHADO = []
expressao = str(input('Digite sua expressão: ')).strip()
for caracter in expressao:
    print(caracter, end=' ')
    if caracter == '(':
        parentesesABERTO.append(caracter)
    elif caracter == ')':
        parentesesFECHADO.append(caracter)
if len(parentesesABERTO) == len(parentesesFECHADO):
    print('Sua expressão está CORRETA.')
else:
    print('Sua expressão está INCORRETA.')
    