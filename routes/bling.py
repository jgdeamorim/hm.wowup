import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import CredenciaisAPI

router = APIRouter(prefix="/bling", tags=["Bling"])

def obter_credenciais_bling(cliente_id: int, db: Session):
    credenciais = db.query(CredenciaisAPI).filter(CredenciaisAPI.cliente_id == cliente_id).first()
    if not credenciais or not credenciais.bling_api_key:
        raise HTTPException(status_code=400, detail="Chave de API do Bling não encontrada")
    return credenciais.bling_api_key

@router.get("/produtos/{cliente_id}")
def listar_produtos_bling(cliente_id: int, db: Session = Depends(get_db)):
    api_key = obter_credenciais_bling(cliente_id, db)
    url = f"https://bling.com.br/api/v3/produtos?apikey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar Bling API: {str(e)}")
