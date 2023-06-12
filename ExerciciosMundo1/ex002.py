nome = input('Qual seu nome? ')
cores = {'verde':'\033[32m', 'limpa':'\033[m'}
print('Prazer em te conhecer {}{}{}, deseja alguma coisa?'.format(cores['verde'], nome, cores['limpa']))
print('Voce {}{}{} esta bem?' .format(cores['verde'], nome, cores['limpa']))
