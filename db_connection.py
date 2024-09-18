import psycopg2

def conectar():
    conn = psycopg2.connect(
        dbname='nome_do_banco',
        user='seu_usuario',
        password='sua_senha',
        host='localhost',
        port='5432'
    )
    return conn
