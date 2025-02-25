import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "backend.log")
log_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)  # 🔹 Rotação de logs
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

def log_info(mensagem: str):
    logger.info(mensagem)

def log_erro(mensagem: str):
    logger.error(mensagem)

def log_debug(mensagem: str):
    logger.debug(mensagem)
