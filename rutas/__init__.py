from flask import Blueprint
from .autenticacion_rutas import autenticacion
from .itop_rutas import itop

def register_routes(app):
    
    app.register_blueprint(autenticacion, url_prefix='/auth')
    app.register_blueprint(itop, url_prefix='/itop')