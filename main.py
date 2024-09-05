from app import create_app
from configuracion.configuracion import Config


app = create_app()
config_instance = Config()
config_instance.iniciar()

if __name__ == "__main__":
    app.run(debug=True, port=config_instance.PORT)