import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import CredenciaisAPI

router = APIRouter(prefix="/mercadolivre", tags=["Mercado Livre"])

def obter_credenciais_ml(cliente_id: int, db: Session):
    credenciais = db.query(CredenciaisAPI).filter(CredenciaisAPI.cliente_id == cliente_id).first()
    if not credenciais or not credenciais.mercadolivre_access_token:
        raise HTTPException(status_code=400, detail="Token de API do Mercado Livre não encontrado")
    return credenciais.mercadolivre_access_token

@router.get("/produtos/{cliente_id}")
def listar_produtos_ml(cliente_id: int, db: Session = Depends(get_db)):
    access_token = obter_credenciais_ml(cliente_id, db)
    url = "https://api.mercadolibre.com/users/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar Mercado Livre API: {str(e)}")
