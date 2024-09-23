import psycopg2

def conectar():
    conn = psycopg2.connect(
        dbname='projeto_igreja',
        user='postgres',
        password='123456',
        host='postgresql://postgres:********@autorack.proxy.rlwy.net:36405/railway',
        port='36405'
    )
    return conn
