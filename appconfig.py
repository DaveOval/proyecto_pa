from dotenv import load_dotenv
import os

load_dotenv()

LLAVE_SECRETA = os.getenv('LLAVE_SECRETA_JWT')
APP_NAME = os.getenv('APP_NAME', 'Mi Aplicación')
URL_POSTGRES_URL = os.getenv('URL_POSTGRES_URL')