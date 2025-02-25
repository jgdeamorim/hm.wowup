from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, clientes, produtos, bling, mercadolivre, vendas, notificacoes
from dependencies import create_tables

app = FastAPI(
    title="Sistema de Gestão",
    description="API para integração de clientes, produtos e vendas",
    version="1.0.0"
)

# Configuração do CORS (permite chamadas do frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode ser ajustado para domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar Rotas
app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(produtos.router)
app.include_router(bling.router)
app.include_router(mercadolivre.router)
app.include_router(vendas.router)
app.include_router(notificacoes.router)

# Criar tabelas automaticamente no banco de dados
@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def home():
    return {"message": "API Online"}
