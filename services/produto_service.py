from sqlalchemy.orm import Session
from fastapi import HTTPException
from database.models import Produto
from database.schemas import ProdutoCreate
from utils.logger import log_info, log_erro

def criar_produto(produto_data: ProdutoCreate, db: Session):
    produto_existente = db.query(Produto).filter(Produto.nome == produto_data.nome).first()
    if produto_existente:
        raise HTTPException(status_code=400, detail="Produto já cadastrado")

    novo_produto = Produto(**produto_data.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    log_info(f"Produto criado: {novo_produto.nome}")
    return novo_produto

def listar_produtos(db: Session):
    produtos = db.query(Produto).all()
    log_info("Listando todos os produtos")
    return produtos

def obter_produto(produto_id: int, db: Session):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        log_erro(f"Produto ID {produto_id} não encontrado")
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
