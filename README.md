# testeEqualBI
Repositório contendo os arquivos utilizados para o processo seletivo da empresa EqualBI.

## Sobre o desafio
Trata-se do desenvolvimento de um *dashboard* a partir dos dados brutos de arquivos *.csv*. Era necessário também tratar os dados antes de usá-los.
Os requisitos do *dashboard* estão melhor descritos no [PDF](CASE%20PS%2023.1.pdf).

## Sobre o que foi desenvolvido
Para poder importar estes arquivos no ambiente de trabalho escolhido (*Google Looker Studio*), era necessário primeiramente tratar os dados brutos para que fossem aceitos pelo sistema Google. <br>
Para fazer isso, foi necessário escrever um [script em Python](limpaArquivoBI.py) para ler os arquivos, corrigir os problemas e então criar outros novos arquivos com os dados já tratados. <br>
Com os novos arquivos (localizados em [newFiles](./newFiles)), já foi possível desenvolver o [*dashboard*](https://lookerstudio.google.com/reporting/bdf2c213-3ee4-48ee-9177-a4c4e343a1d3) do desafio. 

## Execução
Neste tópico será abordado sobre a execução do script desenvolvido, detalhando quais são os pré-requisitos e os comandos a serem digitados no terminal.

### Pré-requisitos
- [Python](https://www.python.org/)
- Conexão à internet

### Comandos de terminal
Já se encontrando no diretório que contém o arquivo `limpaArquivosBI.py`, basta digitar o seguinte comando para executá-lo.
1. `python limpaArquivosBI.py`
