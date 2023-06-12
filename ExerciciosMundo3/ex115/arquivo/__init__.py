def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler aquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:<3}anos')
    finally:
        a.close()


def adicionar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Houve um erro ao abrir o arquivo, {erro.args} ')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao adicionar o nome.')
        else:
            print('Registro feito com sucesso.')
            a.close()