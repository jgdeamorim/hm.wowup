# Use uma imagem leve do Python
FROM python:3.11

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos para dentro do contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar o FastAPI (caso o main.py esteja na raiz do projeto)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
