from flask import Flask, jsonify, request  # Importa Flask y funciones necesarias para crear la API
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy para manejar la base de datos

# Crea una instancia de la aplicación Flask
app = Flask(__name__)
# Configura la URI de la base de datos, en este caso usando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autos.db'
# Desactiva el seguimiento de modificaciones para mejorar el rendimiento
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Crea una instancia de SQLAlchemy para interactuar con la base de datos
db = SQLAlchemy(app)
