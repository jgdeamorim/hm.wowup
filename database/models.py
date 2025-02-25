from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# 🔹 Definição da Base para os modelos
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    # 🔹 Relacionamentos
    produtos = relationship("Produto", back_populates="cliente")
    credenciais = relationship("CredenciaisAPI", back_populates="cliente")
    vendas = relationship("Venda", back_populates="cliente")
    notificacoes = relationship("Notificacao", back_populates="cliente")  # 🔹 Novo relacionamento com Notificação

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    categoria = Column(String)
    preco = Column(Float, nullable=False)  # 🔹 Alterado para Float para garantir precisão em preços
    estoque = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="produtos")

class CredenciaisAPI(Base):
    __tablename__ = "credenciais_api"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), unique=True)
    bling_api_key = Column(String, nullable=True)
    mercadolivre_access_token = Column(String, nullable=True)

    cliente = relationship("Cliente", back_populates="credenciais")

class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)
    data_venda = Column(DateTime, default=datetime.utcnow)

    cliente = relationship("Cliente", back_populates="vendas")
    produto = relationship("Produto")

# 🔹 Adicionando a classe Notificacao para corrigir erro de importação
class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)
    mensagem = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="notificacoes")
