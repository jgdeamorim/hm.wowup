from pydantic import BaseModel, EmailStr
from typing import Optional

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
        from_attributes = True  # Corrigido para Pydantic V2
