# 🚀 Usando uma imagem otimizada para Python
FROM python:3.11

# 🚀 Definir diretório de trabalho
WORKDIR /app

# 🚀 Copiar os arquivos do projeto
COPY . .

# 🚀 Instalar dependências do projeto
RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt

# 🚀 Variáveis de ambiente para PostgreSQL na Railway
ENV DATABASE_URL="postgresql://usuario:senha@db_host:5432/nome_do_banco"

# 🚀 Expor a porta do FastAPI
EXPOSE 8000

# 🚀 Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
