import psycopg2

def conectar():
    conn = psycopg2.connect(
        dbname='railway',
        user='postgres',
        password='PTHHOstJuOVkPhtSIlfboNjVeWwyvNSa',
        host='autorack.proxy.rlwy.net',
        port='36405'
    )
    return conn
