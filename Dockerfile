# 1️⃣ Use uma imagem leve do Python
FROM python:3.11-slim

# 2️⃣ Defina o diretório de trabalho
WORKDIR /app

# 3️⃣ Copie apenas o requirements.txt primeiro (aproveita cache do Docker)
COPY requirements.txt /app/

# 4️⃣ Instale dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copie todos os arquivos restantes **EXCETO arquivos indesejados**
COPY . /app/

# 6️⃣ Exponha a porta padrão do FastAPI
EXPOSE 8000

# 7️⃣ Execute o comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
