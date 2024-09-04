import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    def iniciar(self):
        SECRET_KEY = os.getenv('SECRET_KEY')
        USER = os.getenv('USER')
        PASSWORD = os.getenv('PASSWORD')
        ITOP_URL = os.getenv('ITOP_URL')

