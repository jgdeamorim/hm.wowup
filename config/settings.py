from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME: str = "Hub Mercado"
    API_VERSION: str = "v1"

    # Banco de Dados
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7  # Refresh token agora disponível

    # Configuração de Redis (Cache e Filas)
    REDIS_URL: str

    # Chaves de API externas (Bling e Mercado Livre)
    BLING_API_KEY: str
    MERCADOLIVRE_ACCESS_TOKEN: str

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
