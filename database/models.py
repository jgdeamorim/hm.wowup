from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.connection import Base

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    produtos = relationship("Produto", back_populates="cliente")
    credenciais = relationship("CredenciaisAPI", back_populates="cliente")

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
