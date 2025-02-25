from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def criar_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verificar_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

def obter_usuario_autenticado(token: str = Depends(oauth2_scheme)):
    payload = verificar_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    return payload
