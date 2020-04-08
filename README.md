
# Usando Python para extrair informações de arquivos PDF + Banco de Dados SQL do Azure

As vezes temos dificuldade em conseguir os dados que precisamos, seja para fazer uma análise encima deles ou para utilizar em nosso aplicativo, vou mostrar como extrair informações de um PDF e também como enviar o que foi adquirido para o Azure!

### Artigo
Link para o arquivo no Medium: [https://medium.com/p/2e6bed309629/edit](https://medium.com/p/2e6bed309629/edit)
 
## Requisitos

- tabula-py
> pip install tabula-py==1.3.1

- pyodbc
> pip install pyodbc

### Azure 

Criei um conta grátis aqui: [https://azure.microsoft.com/pt-br/free/](https://azure.microsoft.com/pt-br/free/)

## Config
Exemplo:

```
{
    "file": {
        "pdf": "animes.pdf",
        "pages": 1
    },
    "Azure": {
        "Server": "DESKTOP-0TP05S2",
        "Database": "PythonDB"
    }
}
```

## Referências

[https://docs.microsoft.com/pt-br/azure/sql-database/sql-database-connect-query-python?tabs=windows](https://docs.microsoft.com/pt-br/azure/sql-database/sql-database-connect-query-python?tabs=windows)