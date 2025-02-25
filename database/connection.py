from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import settings

# 🔹 Criação do Engine otimizado para Railway e PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,          # 🔹 Máximo de 10 conexões abertas simultaneamente
    max_overflow=20,       # 🔹 Permite 20 conexões extras temporárias se o pool estiver cheio
    pool_pre_ping=True,    # 🔹 Mantém a conexão ativa, evitando problemas de timeout
    connect_args={"options": "-c timezone=utc"}  # 🔹 Força o PostgreSQL a trabalhar em UTC
)

# 🔹 Criando SessionLocal para Gerenciamento de Sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔹 Base para os Modelos SQLAlchemy
Base = declarative_base()

# 🔹 Função para Obter a Sessão do Banco de Dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
