from flask import Blueprint

itop = Blueprint('itop', __name__)

@itop.route('/itop')
def config():
    return 'Ejemplo de itop'