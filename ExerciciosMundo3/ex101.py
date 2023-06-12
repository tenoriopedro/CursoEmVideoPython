def voto(ano):
    """
    Verifica a idade de uma pessoa e mostra o resultado com mensagem de
    votação obrigatoria, opcional ou não vota
    :param ano: ano de nascimento da pessoa
    :return: VOTO OBRIGATORIO, VOTO OPCIONAL, NÃO VOTA, ERROS
    """
    from datetime import date
    if ano.isnumeric():
        ano = int(ano)
        ano_atual = date.today().year
        idade_pessoa = ano_atual - ano
        print(f'Você tem {idade_pessoa} anos, portanto ',end='')
        if idade_pessoa >= 18 and idade_pessoa < 65:
            return 'VOTO OBRIGATÓRIO'
        if idade_pessoa < 18 and idade_pessoa >= 16 or idade_pessoa >= 65:
            return 'VOTO OPCIONAL'
        if idade_pessoa >= 0 and idade_pessoa < 16:
            return 'NÃO VOTA'
        if idade_pessoa < 0:
            return'ERRO!!! Você digitou seu ano corretamente?'
    else:
        return 'ERRO!!! Digite apenas números.'

nascimento = input('Digite aqui o ano do seu nascimento: ')
print(voto(nascimento))