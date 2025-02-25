from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from database.schemas import ProdutoCreate, ProdutoResponse
from services.produto_service import criar_produto, listar_produtos

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoResponse)
def criar_produto_route(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return criar_produto(produto, db)

@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos_route(db: Session = Depends(get_db)):
    return listar_produtos(db)
