import psycopg2

def conectar():
    conn = psycopg2.connect(
        dbname='projeto_igreja',
        user='postgres',
        password='123456',
        host='localhost',
        port='3000'
    )
    return conn
