import logging.config
from flask import Blueprint, jsonify
from configuracion.configuracion import Config
import jwt 
import datetime
import requests
import logging 

# Configuración para los logs (temporales)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define el Blueprint
autenticacion = Blueprint('autenticacion', __name__)

# Define la ruta dentro del Blueprint
@autenticacion.route('/generate', methods=['POST'])
def generate_token():
    try: 
        # Instancia a la clase Config
        config = Config() 
        config.iniciar()

        # Variables extraídas de la clase Config
        api_user = config.USER
        api_password = config.PASSWORD
        secret_key = config.SECRET_KEY

        # Payload - contenido del token al decodificarlo
        payload = {
                'user': api_user,
                'password': api_password,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            }
        # Codificación del token 
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        return jsonify({'token': token})
    except requests.exceptions.ConnectionError as e: 
        return f"Error al obtener el token o realizar la conexión entre APIS {e}"