import requests
import time
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models import CredenciaisAPI
from config.settings import settings

def obter_credenciais_bling(cliente_id: int, db: Session):
    credenciais = db.query(CredenciaisAPI).filter(CredenciaisAPI.cliente_id == cliente_id).first()
    if not credenciais or not credenciais.bling_api_key:
        raise HTTPException(status_code=400, detail="Chave de API do Bling não encontrada")
    return credenciais.bling_api_key

def listar_produtos_bling(cliente_id: int, db: Session):
    api_key = obter_credenciais_bling(cliente_id, db)
    url = f"https://bling.com.br/api/v3/produtos?apikey={api_key}"

    for tentativa in range(3):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 429:
                print("⚠️ Limite de requisições atingido. Aguardando...")
                time.sleep(5)  # Espera antes de tentar novamente
                continue
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao acessar Bling API (Tentativa {tentativa+1}): {e}")
            if tentativa == 2:
                raise HTTPException(status_code=500, detail=f"Erro ao acessar Bling API: {e}")
