from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

def conectar():
    conn = psycopg2.connect(
        dbname='projeto_igreja',
        user='postgres',
        password='123456',
        host='localhost',
        port='5432'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar_visitante():
    foto = request.form['foto']
    nome_completo = request.form['nome_completo']
    idade_geracional = request.form['idade_geracional']
    telefone = request.form['telefone']
    data_visita = request.form['data_visita']

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO visitantes (foto, nome_completo, idade_geracional, telefone, data_visita)
    VALUES (%s, %s, %s, %s, %s)
    ''', (foto, nome_completo, idade_geracional, telefone, data_visita))
    conn.commit()
    conn.close()

    return 'Visitante adicionado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
