from app.autenticacion import autenticacion

def register_routes(app):
    app.register_blueprint(autenticacion, url_prefix='/auth')
