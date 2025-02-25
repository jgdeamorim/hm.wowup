# Usa uma imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000 para comunicação externa
EXPOSE 8000

# Define o comando de execução
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
