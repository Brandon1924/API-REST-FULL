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

# Define el modelo 'Auto' que representa la tabla en la base de datos
class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Columna para el ID del auto, clave primaria
    marca = db.Column(db.String(50), nullable=False)  # Columna para la marca, no puede ser nula
    modelo = db.Column(db.String(50), nullable=False)  # Columna para el modelo, no puede ser nula

# Crea la base de datos y las tablas definidas por los modelos
with app.app_context():  # Aquí se inicia el contexto de la aplicación para realizar operaciones de base de datos
    db.create_all()  # Crea todas las tablas en la base de datos según los modelos definidos

# Ruta para crear un nuevo auto
@app.route('/autos', methods=['POST'])
def crear_auto():
    data = request.get_json()  # Obtiene los datos JSON de la solicitud
    # Crea un nuevo objeto Auto con los datos recibidos
    nuevo_auto = Auto(marca=data['marca'], modelo=data['modelo'])
    db.session.add(nuevo_auto)  # Agrega el nuevo auto a la sesión de la base de datos
    db.session.commit()  # Confirma los cambios en la base de datos
    return jsonify({'message': 'Auto creado'}), 201  # Devuelve un mensaje de éxito

# Ruta para obtener todos los autos
@app.route('/autos', methods=['GET'])
def obtener_autos():
    autos = Auto.query.all()  # Consulta todos los registros de la tabla Auto
    # Devuelve una lista de autos en formato JSON
    return jsonify([{'id': auto.id, 'marca': auto.marca, 'modelo': auto.modelo} for auto in autos])

# Ruta para obtener un auto específico por ID
@app.route('/autos/<int:id>', methods=['GET'])
def obtener_auto(id):
    auto = Auto.query.get(id)  # Busca el auto por ID
    if auto:
        # Si se encuentra, devuelve sus detalles en formato JSON
        return jsonify({'id': auto.id, 'marca': auto.marca, 'modelo': auto.modelo})
    return jsonify({'message': 'Auto no encontrado'}), 404  # Devuelve un mensaje de error si no se encuentra

# Ruta para actualizar un auto existente
@app.route('/autos/<int:id>', methods=['PUT'])
def actualizar_auto(id):
    data = request.get_json()  # Obtiene los datos JSON de la solicitud
    auto = Auto.query.get(id)  # Busca el auto por ID
    if auto:
        # Actualiza los atributos del auto con los nuevos datos
        auto.marca = data['marca']
        auto.modelo = data['modelo']
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Auto actualizado'})  # Devuelve un mensaje de éxito
    return jsonify({'message': 'Auto no encontrado'}), 404  # Mensaje de error si no se encuentra

# Ruta para eliminar un auto
@app.route('/autos/<int:id>', methods=['DELETE'])
def eliminar_auto(id):
    auto = Auto.query.get(id)  # Busca el auto por ID
    if auto:
        db.session.delete(auto)  # Elimina el auto de la sesión
        db.session.commit()  # Confirma la eliminación en la base de datos
        return jsonify({'message': 'Auto eliminado'})  # Devuelve un mensaje de éxito
    return jsonify({'message': 'Auto no encontrado'}), 404  # Mensaje de error si no se encuentra

# Inicia la aplicación Flask si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración
