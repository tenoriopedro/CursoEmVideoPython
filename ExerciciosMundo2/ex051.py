print('*' *25)
print('  PROGRESSÃO ARITMÉTICA')
print('*' *25)
primtermo = int(input('Digite o primeiro termo dessa progreção: '))
razao = int(input('Digite a razão dessa progreção: '))
n = 10
ultimo = primtermo + (n-1)*razao
ultimo = ultimo + 1
for c in range(primtermo, ultimo, razao):
    print(c, end=' - ' )
print('FIM')