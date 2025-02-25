import re
from fastapi import HTTPException

def validar_email(email: str):
    regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(regex, email):
        raise HTTPException(status_code=400, detail="E-mail inválido")
    return email

def validar_senha(senha: str):
    if len(senha) < 8:
        raise HTTPException(status_code=400, detail="A senha deve ter pelo menos 8 caracteres")
    return senha

def validar_preco(preco: float):
    if preco < 0:
        raise HTTPException(status_code=400, detail="O preço não pode ser negativo")
    return preco
