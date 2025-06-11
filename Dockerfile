# Imagem base com Python
FROM python:3.10-slim

# Instala FFmpeg e dependências básicas
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da aplicação
EXPOSE 10000

# Comando para iniciar o servidor
CMD ["python", "server.py"]
