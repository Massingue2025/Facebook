# Base com Python e apt
FROM python:3.10-slim

# Instalar ffmpeg e dependências
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean

# Diretório da aplicação
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Porta para Render expor
EXPOSE 10000

# Iniciar app
CMD ["python", "server.py"]
