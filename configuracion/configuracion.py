import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    def iniciar(self):
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.USER = os.getenv('USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.ITOP_URL = os.getenv('ITOP_URL')       
        self.PORT = os.getenv('PORT') 
