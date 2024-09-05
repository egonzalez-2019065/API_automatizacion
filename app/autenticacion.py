from flask import Blueprint, jsonify
from configuracion.configuracion import Config
import jwt 
import datetime

# Define el Blueprint
autenticacion = Blueprint('autenticacion', __name__)

# Define la ruta dentro del Blueprint
@autenticacion.route('/generate', methods=['POST'])
def generate_token():
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