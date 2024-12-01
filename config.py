import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BACKEND_API_URL = os.getenv('BACKEND_API_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
ADMIN_ID = os.getenv('ADMIN_ID')
