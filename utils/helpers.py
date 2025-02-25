import datetime

def formatar_data(data: datetime.datetime) -> str:
    return data.strftime("%Y-%m-%d %H:%M:%S")

def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def limpar_texto(texto: str) -> str:
    return " ".join(texto.split()).strip()
