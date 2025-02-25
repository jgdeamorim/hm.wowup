# Use uma imagem leve do Python
FROM python:3.11

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY . /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 8000 para comunicação
EXPOSE 8000

# Comando para iniciar a aplicação no Railway
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
