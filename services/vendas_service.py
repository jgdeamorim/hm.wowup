from sqlalchemy.orm import Session
from fastapi import HTTPException
from database.models import Venda
from database.schemas import VendaCreate
from utils.logger import log_info, log_erro
import redis
from config.settings import settings

cache = redis.Redis.from_url(settings.REDIS_URL)

def registrar_venda(venda_data: VendaCreate, db: Session):
    nova_venda = Venda(**venda_data.dict())
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    cache.delete("vendas_relatorio")  # Invalida cache de relatórios
    log_info(f"Venda registrada: {nova_venda.id}")
    return nova_venda

def listar_vendas(db: Session):
    cache_key = "vendas_relatorio"
    
    if cache.exists(cache_key):
        return cache.get(cache_key)

    vendas = db.query(Venda).all()
    cache.setex(cache_key, 3600, vendas)  # Cache por 1 hora
    log_info("Listando todas as vendas")
    return vendas
