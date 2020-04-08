import pyodbc
from datetime import datetime
import numpy as np

#Fazendo a conexão com o SQL Server
def createConnection(server, database):
    return pyodbc.connect('Driver={SQL Server};'
                        f'Server={server};'
                        f'Database={database};'
                        'Trusted_Connection=yes;')

def insertData(conn, table_name,cols,rows):
    cursor = conn.cursor()
    columns = ','.join([str(elem) for elem in cols]) 
    items = ','.join(str('?') for elem in range(len(cols)+1))
    columns = columns + ', dateRegister'
    string = f"insert into [dbo].[{table_name}]({columns}) values({items})"
    
    for values in rows:
        values.append(str(datetime.now()))
        cursor.execute(string, values)
        conn.commit()
    print("Values inserted!")
  

def createDatabase(conn, table_name, columns, types):
    cursor = conn.cursor()
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
          
        cursor.execute(string)
        cursor.commit()
        print("Table created!")
        