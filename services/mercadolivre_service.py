import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

ML_CLIENT_ID = os.getenv("ML_CLIENT_ID")
ML_CLIENT_SECRET = os.getenv("ML_CLIENT_SECRET")
ML_ACCESS_TOKEN = os.getenv("ML_ACCESS_TOKEN")
ML_REFRESH_TOKEN = os.getenv("ML_REFRESH_TOKEN")
ML_TOKEN_EXPIRATION = float(os.getenv("ML_TOKEN_EXPIRATION", 0))
ML_TOKEN_URL = "https://api.mercadolibre.com/oauth/token"

def salvar_tokens(access_token, refresh_token, expires_in):
    """ Salva os tokens no .env para persistência """
    global ML_ACCESS_TOKEN, ML_REFRESH_TOKEN, ML_TOKEN_EXPIRATION

    ML_ACCESS_TOKEN = access_token
    ML_REFRESH_TOKEN = refresh_token
    ML_TOKEN_EXPIRATION = time.time() + expires_in

    with open(".env", "r") as file:
        linhas = file.readlines()

    with open(".env", "w") as file:
        for linha in linhas:
            if linha.startswith("ML_ACCESS_TOKEN="):
                file.write(f"ML_ACCESS_TOKEN={ML_ACCESS_TOKEN}\n")
            elif linha.startswith("ML_REFRESH_TOKEN="):
                file.write(f"ML_REFRESH_TOKEN={ML_REFRESH_TOKEN}\n")
            elif linha.startswith("ML_TOKEN_EXPIRATION="):
                file.write(f"ML_TOKEN_EXPIRATION={ML_TOKEN_EXPIRATION}\n")
            else:
                file.write(linha)

    print("✅ Tokens atualizados no .env!")

def renovar_token():
    """ Usa o refresh_token para obter um novo access_token antes da expiração """
    global ML_ACCESS_TOKEN, ML_REFRESH_TOKEN, ML_TOKEN_EXPIRATION

    print("🔄 Verificando necessidade de renovação do token...")

    if time.time() < ML_TOKEN_EXPIRATION - 300:
        print("✅ Token ainda é válido, não precisa renovar.")
        return ML_ACCESS_TOKEN

    print("⚠️ Token expirado ou próximo de expirar. Renovando...")

    payload = {
        "grant_type": "refresh_token",
        "client_id": ML_CLIENT_ID,
        "client_secret": ML_CLIENT_SECRET,
        "refresh_token": ML_REFRESH_TOKEN,
    }
    
    resposta = requests.post(ML_TOKEN_URL, data=payload)
    dados = resposta.json()

    if "access_token" in dados:
        salvar_tokens(dados["access_token"], dados["refresh_token"], dados["expires_in"])
        return dados["access_token"]
    else:
        print("❌ Erro ao renovar token:", dados)
        return None
