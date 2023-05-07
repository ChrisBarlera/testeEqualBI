nomeArquivo = input('Insira o nome do arquivo (Ex: teste.csv): ')
nColunas = int(input('Insira o número de colunas da tabela: '))

def postarLinha(novaLinha):
    existe = False
    try: 
        with open('new_'+nomeArquivo,'r') as arquivo:
            existe = True
    except:
        pass

    if existe:
        with open('new_'+nomeArquivo,'a') as arquivo:
            arquivo.write(novaLinha)
    else:
        with open('new_'+nomeArquivo,'w') as arquivo:
            arquivo.write(novaLinha)


with open(nomeArquivo,'r') as arquivo:
    for linha in arquivo.readlines():
        cLinha = linha.split(',')
        if len(cLinha) > nColunas:
            inicioLinha = linha[:linha.index('\"')]
            meioLinha = linha[linha.index('\"')+1:linha.index('\"',linha.index('\"')+1)].replace(',','.')
            finalLinha = linha[linha.index('\"',linha.index('\"')+1)+1:]
            cLinha = (inicioLinha+meioLinha+finalLinha).split(',')
            postarLinha((inicioLinha+meioLinha+finalLinha))
        else:
            postarLinha(linha.replace('\"',''))