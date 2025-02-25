import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_info(mensagem: str):
    logging.info(mensagem)

def log_erro(mensagem: str):
    logging.error(mensagem)

def log_debug(mensagem: str):
    logging.debug(mensagem)
