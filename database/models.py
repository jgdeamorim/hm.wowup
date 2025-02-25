from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# 🔹 Definição correta da Base
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    produtos = relationship("Produto", back_populates="cliente")
    credenciais = relationship("CredenciaisAPI", back_populates="cliente")
    vendas = relationship("Venda", back_populates="cliente")  # 🔹 Adicionando relacionamento com Venda

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    categoria = Column(String)
    preco = Column(Integer)
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

# 🔹 Adicionando a classe Venda ao models.py
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
