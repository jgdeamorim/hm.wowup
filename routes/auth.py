from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
from database.connection import get_db
from database.models import Cliente
from database.schemas import ClienteBase
from security.jwt import criar_access_token, criar_refresh_token, verificar_access_token
from security.password import verificar_senha
from config.settings import settings

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login")
def login(cliente_data: ClienteBase, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.email == cliente_data.email).first()
    if not cliente or not verificar_senha(cliente_data.senha, cliente.senha):
        raise HTTPException(status_code=400, detail="E-mail ou senha inválidos")

    access_token = criar_access_token(data={"sub": cliente.email})
    refresh_token = criar_refresh_token(data={"sub": cliente.email})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/logout")
def logout(token: str = Depends(verificar_access_token)):
    return {"message": "Usuário deslogado com sucesso"}