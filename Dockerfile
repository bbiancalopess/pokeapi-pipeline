FROM python:3.13-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . .

# Instala as dependências no container
RUN pip install --no-cache-dir -r requirements.txt

# Expõe o diretório de logs e dados
VOLUME ["/app/logs", "/app/data"]

# Executa o script principal
CMD ["python", "main.py"]