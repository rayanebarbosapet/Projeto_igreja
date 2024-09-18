import pandas as pd
from db_connection import conectar

def carregar_dados():
    conn = conectar()
    df = pd.read_sql_query('SELECT * FROM visitantes', conn)
    conn.close()
    return df

def gerar_relatorio():
    df = carregar_dados()
    relatorio = df.groupby('data_visita').size().reset_index(name='total_visitas')
    print(relatorio)
