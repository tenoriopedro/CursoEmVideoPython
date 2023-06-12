from ex115 import menu
from ex115 import arquivo
from ex111.utilidadescev import dado


arq = 'cadastro.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    menu.titulo('CADASTRO DE PESSOAS')
    pergunta = menu.leiaOpcao('Sua opção: ')
    if pergunta == 1:
        arquivo.lerArquivo(arq)
    if pergunta == 2:
        nome = str(input('Nome: '))
        idade = dado.leiaInt('Idade: ')
        arquivo.adicionar(arq, nome, idade)
    if pergunta == 3:
        break