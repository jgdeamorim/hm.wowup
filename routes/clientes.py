from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from database.schemas import ClienteCreate, ClienteResponse
from backend.services.cliente_service import criar_cliente, listar_clientes

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteResponse)
def criar_cliente_route(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return criar_cliente(cliente, db)

@router.get("/", response_model=list[ClienteResponse])
def listar_clientes_route(db: Session = Depends(get_db)):
    return listar_clientes(db)