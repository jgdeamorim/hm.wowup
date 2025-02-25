from sqlalchemy.orm import Session
from database.models import Notificacao
from database.schemas import NotificacaoBase
from utils.logger import log_info

def registrar_notificacao(notificacao_data: NotificacaoBase, db: Session):
    nova_notificacao = Notificacao(**notificacao_data.dict())
    db.add(nova_notificacao)
    db.commit()
    db.refresh(nova_notificacao)
    log_info(f"Nova notificação registrada: {nova_notificacao.mensagem}")
    return nova_notificacao

def listar_notificacoes(db: Session):
    notificacoes = db.query(Notificacao).order_by(Notificacao.timestamp.desc()).all()
    log_info("Listando notificações do sistema")
    return notificacoes
