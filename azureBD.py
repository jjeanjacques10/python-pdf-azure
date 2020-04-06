import pyodbc, json
from datetime import datetime
import numpy as np

#Acessando o arquivo de configuração
with open('config/config.json') as config_file:
    data = json.load(config_file)

server = data['Azure']['Server']
database = data['Azure']['Database']
query = data['Azure']['Query']

#Fazendo a conexão com o SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                    f'Server={server};'
                    f'Database={database};'
                    'Trusted_Connection=yes;')

#Fazeendo o SELECT na tabela selecionada
cursor = conn.cursor()
cursor.execute(query)

def insertData(table_name,cols,rows):
    columns = ','.join([str(elem) for elem in cols]) 
    items = ','.join(str('?') for elem in range(len(cols)+1))
    columns = columns + ', dateRegister'
    string = f"insert into [dbo].[{table_name}]({columns}) values({items})"
    
    for values in rows:
        values.append(str(datetime.now()))
        cursor.execute(string, values)
        conn.commit()
    print("Values inserted!")
  
#Criando um tabela no banco de dados
def createDatabase(table_name, columns, types):
    #Verificando se a tabela existe
    if cursor.tables(table=table_name, tableType='TABLE').fetchone():
        print("Table exists")
    else:
        string = f"CREATE TABLE [dbo].[{table_name}]("
        for item in columns:
            if(types[item] == object):
                string = string + f"{item} NVARCHAR(100),"
            elif(types[item] == np.int64):
                string = string + f"{item} INT," 
            elif(types[item] == float):
                string = string + f"{item} NUMERIC,"
        string = string + "dateRegister NVARCHAR(100));"
        
        print(string)   
        cursor.execute(string)
        cursor.commit()
        print("Table created!")
        