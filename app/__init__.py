from flask import Flask
from flask_cors import CORS
from configuracion.configuracion import Config
from rutas import register_routes

def create_app(): 
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object(Config)


    # Configuración de cors, para que acepte todas las rutas
    CORS(app)

    # Configuración de las rutas 
    register_routes(app)

    return app 