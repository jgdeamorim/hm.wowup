from sqlalchemy.orm import Session
from database.models import Cliente
from database.schemas import ClienteCreate

def criar_cliente(cliente_data: ClienteCreate, db: Session):
    print(f"📌 Tentando criar cliente: {cliente_data.dict()}")  # 🔥 ADICIONANDO LOG

    novo_cliente = Cliente(**cliente_data.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    print(f"✅ Cliente criado: {novo_cliente}")  # 🔥 LOG PARA CONFIRMAR QUE SALVOU
    return novo_cliente

def listar_clientes(db: Session):
    clientes = db.query(Cliente).all()
    print(f"📌 Retornando lista de clientes: {clientes}")  # 🔥 LOG PARA VERIFICAR O BANCO
    return clientes
