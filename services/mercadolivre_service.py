import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

# 🔹 URLs e Configurações
ML_CLIENT_ID = os.getenv("ML_CLIENT_ID")
ML_CLIENT_SECRET = os.getenv("ML_CLIENT_SECRET")
ML_ACCESS_TOKEN = os.getenv("ML_ACCESS_TOKEN")
ML_REFRESH_TOKEN = os.getenv("ML_REFRESH_TOKEN")
ML_TOKEN_EXPIRATION = float(os.getenv("ML_TOKEN_EXPIRATION", 0))
ML_TOKEN_URL = "https://api.mercadolibre.com/oauth/token"

def salvar_tokens(access_token: str, refresh_token: str, expires_in: int):
    """ Atualiza os tokens na variável de ambiente para persistência """
    global ML_ACCESS_TOKEN, ML_REFRESH_TOKEN, ML_TOKEN_EXPIRATION

    ML_ACCESS_TOKEN = access_token
    ML_REFRESH_TOKEN = refresh_token
    ML_TOKEN_EXPIRATION = time.time() + expires_in

    print("✅ Tokens renovados com sucesso!")

def renovar_token():
    """ Verifica se o token está próximo da expiração e renova se necessário """
    global ML_ACCESS_TOKEN, ML_REFRESH_TOKEN, ML_TOKEN_EXPIRATION

    print("🔄 Verificando necessidade de renovação do token...")

    if time.time() < ML_TOKEN_EXPIRATION - 300:
        print("✅ Token ainda é válido, não precisa renovar.")
        return ML_ACCESS_TOKEN

    if not ML_REFRESH_TOKEN:
        print("❌ ERRO: Nenhum `refresh_token` disponível para renovação.")
        return None

    print("⚠️ Token expirado ou próximo de expirar. Renovando...")

    payload = {
        "grant_type": "refresh_token",
        "client_id": ML_CLIENT_ID,
        "client_secret": ML_CLIENT_SECRET,
        "refresh_token": ML_REFRESH_TOKEN,
    }

    try:
        resposta = requests.post(ML_TOKEN_URL, data=payload, timeout=10)
        resposta.raise_for_status()  # 🔹 Lança um erro se a resposta não for 200 OK
        dados = resposta.json()

        if "access_token" in dados:
            salvar_tokens(dados["access_token"], dados["refresh_token"], dados["expires_in"])
            return dados["access_token"]
        else:
            print("❌ Erro ao renovar token:", dados)
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na solicitação ao Mercado Livre: {e}")
        return None
