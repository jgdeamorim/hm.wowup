# 1️⃣ Use uma imagem leve do Python
FROM python:3.11-slim

# 2️⃣ Defina o diretório de trabalho para a raiz do projeto
WORKDIR /

# 3️⃣ Copie apenas o requirements.txt primeiro (para melhor aproveitamento do cache)
COPY requirements.txt ./

# 4️⃣ Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Agora copie todos os arquivos corretamente
COPY . .

# 6️⃣ Exponha a porta padrão do FastAPI
EXPOSE 8000

# 7️⃣ Execute o comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
