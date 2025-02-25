from sqlalchemy.orm import Session
from database.models import Cliente
from database.schemas import ClienteCreate

def criar_cliente(cliente_data: ClienteCreate, db: Session):
    novo_cliente = Cliente(**cliente_data.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

def listar_clientes(db: Session):
    return db.query(Cliente).all()
