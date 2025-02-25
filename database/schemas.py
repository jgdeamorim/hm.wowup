from pydantic import BaseModel, EmailStr
from typing import Optional

class VendaBase(BaseModel):
    produto_id: int
    quantidade: int
    valor_total: float

class VendaCreate(VendaBase):
    pass

class VendaResponse(VendaBase):
    id: int

    class Config:
        from_attributes = True

class ClienteBase(BaseModel):
    nome: str
    email: EmailStr

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True  # Atualizado para Pydantic V2

class ProdutoBase(BaseModel):
    nome: str
    categoria: Optional[str] = None
    preco: int
    estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

class CredenciaisAPIBase(BaseModel):
    bling_api_key: Optional[str] = None
    mercadolivre_access_token: Optional[str] = None

class CredenciaisAPIResponse(CredenciaisAPIBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

# ✅ Correção: Adicionando `NotificacaoBase` e `NotificacaoResponse`
class NotificacaoBase(BaseModel):
    mensagem: str
    tipo: str

class NotificacaoResponse(NotificacaoBase):
    id: int

    class Config:
        from_attributes = True
