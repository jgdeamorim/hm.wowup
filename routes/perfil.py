from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import Usuario
from security.jwt import obter_usuario_autenticado

router = APIRouter(prefix="/perfil", tags=["Perfil"])

@router.get("/")
def obter_perfil(usuario: dict = Depends(obter_usuario_autenticado), db: Session = Depends(get_db)):
    perfil = db.query(Usuario).filter(Usuario.email == usuario["sub"]).first()
    return {"nome": perfil.nome, "email": perfil.email} if perfil else {}
