from ex111.utilidadescev import moedas, dado

p = dado.leiaDinheiro("Digite o preço: €")
aumento = dado.leiaDinheiro('Aumento de porcentagem: ')
reduzir = dado.leiaDinheiro('Redução de porcentagem: ')
moedas.resumo(p, aumento, reduzir)