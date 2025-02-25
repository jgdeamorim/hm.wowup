from fastapi import APIRouter, Depends
from services.openai_service import gerar_descricao_produto
from pydantic import BaseModel

router = APIRouter(prefix="/openai", tags=["OpenAI"])

class ProdutoInfo(BaseModel):
    categoria: str
    especificacoes: str

@router.post("/descricao")
def obter_descricao_produto(produto: ProdutoInfo):
    descricao = gerar_descricao_produto(produto.categoria, produto.especificacoes)
    return {"descricao": descricao}
