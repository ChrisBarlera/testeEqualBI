# Checa se o arquivo existe ou não
# Decide o modo para "abrir" o arquivo
# Posta a linha
def postarLinha(novaLinha, nomeArquivo):
    existe = False
    try: 
        with open('newFiles/new_'+nomeArquivo,'r') as arquivo:
            existe = True
    except:
        pass

    if existe:
        with open('newFiles/new_'+nomeArquivo,'a') as arquivo:
            arquivo.write(novaLinha)
    else:
        with open('newFiles/new_'+nomeArquivo,'w') as arquivo:
            arquivo.write(novaLinha)

# Linhas que vinham com "" tinham problema pois eram linhas com , dentro de um campo e não exclusivamente para a divisão de colunas.
def limpar(nomeArquivo, nColunas):
    with open(nomeArquivo,'r') as arquivo:
        for linha in arquivo.readlines():
            cLinha = linha.split(',') # Separa uma linha por , atribuindo estes valores separados numa única lista
            if len(cLinha) > nColunas: # Checa se o número de itens da lista é maior que o número de colunas (pois linhas podem ter vírgulas a mais usadas erroneamente)
                # As linhas que tinham , extras tinham também "" usadas para delimitar a área da ,
                # Separo a linha pelas aspas duplas, removo a , e posto a linha
                inicioLinha = linha[:linha.index('\"')]
                meioLinha = linha[linha.index('\"')+1:linha.index('\"',linha.index('\"')+1)].replace(',','.')
                finalLinha = linha[linha.index('\"',linha.index('\"')+1)+1:]
                cLinha = (inicioLinha+meioLinha+finalLinha).split(',')
                postarLinha((inicioLinha+meioLinha+finalLinha),nomeArquivo)
            else:
                postarLinha(linha.replace('\"',''),nomeArquivo)

limpar('dim_familia_produtos.csv',2)
limpar('dim_produtos.csv',3)
limpar('dim_vendedores.csv',2)
limpar('fato_vendas.csv',7)