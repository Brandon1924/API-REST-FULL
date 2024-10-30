from flask import Flask
from app.models import db
from app.routes import api
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa la base de datos
    db.init_app(app)

    # Registra las rutas de la API
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    return app