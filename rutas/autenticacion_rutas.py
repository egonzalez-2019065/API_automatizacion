from flask import Blueprint

# Define el Blueprint
autenticacion = Blueprint('autenticacion', __name__)

# Define rutas dentro del Blueprint
@autenticacion.route('/login')
def login():
    return 'Ruta de login'

@autenticacion.route('/register')
def register():
    return 'Ruta de registro'
