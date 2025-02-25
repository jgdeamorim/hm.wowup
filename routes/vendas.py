from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from database.schemas import VendaCreate, VendaResponse
from services.vendas_service import registrar_venda, listar_vendas
from database.models import Venda

router = APIRouter(prefix="/vendas", tags=["Vendas"])

@router.post("/", response_model=VendaResponse)
def criar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    return registrar_venda(venda, db)

@router.get("/", response_model=list[VendaResponse])
def obter_vendas(db: Session = Depends(get_db)):
    return listar_vendas(db)

@router.get("/relatorios")
def obter_relatorio_vendas(db: Session = Depends(get_db)):
    vendas = db.query(Venda).all()
    total_vendas = sum(v.valor_total for v in vendas)
    return {"total_vendas": total_vendas, "quantidade": len(vendas)}