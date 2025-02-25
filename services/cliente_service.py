from sqlalchemy.orm import Session
from database.models import Cliente
from database.schemas import ClienteCreate

def criar_cliente(cliente_data: ClienteCreate, db: Session):
    print(f"📌 [LOG] Tentando criar cliente: {cliente_data.dict()}")  # 🔥 LOG 1

    try:
        novo_cliente = Cliente(**cliente_data.dict())
        db.add(novo_cliente)
        db.commit()
        db.refresh(novo_cliente)

        print(f"✅ [LOG] Cliente criado com sucesso: {novo_cliente}")  # 🔥 LOG 2
        return novo_cliente
    except Exception as e:
        print(f"❌ [LOG] ERRO AO CRIAR CLIENTE: {e}")  # 🔥 LOG 3
        db.rollback()
        return None

def listar_clientes(db: Session):
    clientes = db.query(Cliente).all()
    print(f"📌 [LOG] Clientes cadastrados no banco: {clientes}")  # 🔥 LOG 4
    return clientes
