from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from database.schemas import NotificacaoBase, NotificacaoResponse
from services.notificacao_service import registrar_notificacao, listar_notificacoes

router = APIRouter(prefix="/notificacoes", tags=["Notificações"])

@router.post("/", response_model=NotificacaoResponse)
def criar_notificacao(notificacao: NotificacaoBase, db: Session = Depends(get_db)):
    """ Cria uma nova notificação no banco de dados """
    return registrar_notificacao(notificacao, db)

@router.get("/", response_model=list[NotificacaoResponse])
def obter_notificacoes(db: Session = Depends(get_db)):
    """ Retorna todas as notificações registradas no banco de dados """
    return listar_notificacoes(db)
