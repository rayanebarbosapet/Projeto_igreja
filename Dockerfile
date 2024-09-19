# Usar uma imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Expor a porta que será usada pela aplicação Flask
EXPOSE 3000

# Definir as variáveis de ambiente necessárias
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
