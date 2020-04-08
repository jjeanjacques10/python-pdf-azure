from tabula import read_pdf
import json
from azureBD import *

# Acessando o arquivo de configuração
with open('config/config.json') as config_file:
    config = json.load(config_file)

file_pdf = config['file']['pdf']
pages = config['file']['pages']
server = config['azure']['Server']
database = config['azure']['Database']

#  Coletando os dados do arquivo PDF
data = read_pdf(file_pdf, pages=pages)
table_name = file_pdf.replace('.pdf', '')
values = data[0].values.tolist()

# Coletando tipo dos campos 
type_data = data[0].dtypes

# Coletando nome das colunas
cols = []
for index, item in type_data.items():
    cols.append(index)

# Criando a conecção
conn = createConnection(server, database)

# Criando a tabela caso ela não exista    
createDatabase(conn, table_name, cols, type_data)

# Inserindo valores na tabela
insertData(conn, table_name, cols, values)
