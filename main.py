from tabula import read_pdf
import json
from azureBD import *

#Acessando o arquivo de configuração
with open('config/config.json') as config_file:
    config = json.load(config_file)

file_pdf = config['file']['pdf']
pages = config['file']['pages']

# Coletando os dados do arquivo PDF
data = read_pdf(file_pdf, pages=pages)

# Setando nome da tabela 
table_name = file_pdf.replace('.pdf', '')

#Pegando o valor dos campos
values = data[0].values.tolist()

#Pegando tipo dos campos 
type_data = data[0].dtypes

#Pegando o nome das colunas
cols = []
for index, item in type_data.items():
    cols.append(index)

#Criando a tabela caso ela não exista    
createDatabase(table_name, cols, type_data)

#Inserindo valores na tabela
insertData(table_name, cols, values)
