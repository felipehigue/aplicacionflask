import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

# Cargar las variables del archivo .env
load_dotenv()

# Configuración de la aplicación Flask
app = Flask(__name__)

# Variables de entorno para la conexión MySQL
MYSQL_USER = os.getenv('MYSQLUSER')
MYSQL_PASSWORD = os.getenv('MYSQLPASSWORD')
MYSQL_HOST = os.getenv('MYSQLHOST')
MYSQL_PORT = os.getenv('MYSQLPORT', 3306)
MYSQL_DATABASE = os.getenv('MYSQLDATABASE')

# Configuración de la URL de la base de datos para SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)


# Modelo Camiseta
class Camiseta(db.Model):
    __tablename__ = 'camiseta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)

# Condicional para verificar si la tabla ya existe
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table('camiseta'):
        db.create_all()

# Ruta para leer (Read) - Obtener todas las camisetas
@app.route('/camisetas', methods=['GET'])
def get_camisetas():
    camisetas = Camiseta.query.all()
    camisetas_list = [{"id": camiseta.id, "talla": camiseta.talla, "color": camiseta.color, 
                       "material": camiseta.material, "precio": str(camiseta.precio)} for camiseta in camisetas]
    return jsonify(camisetas_list)

# Ruta para leer (Read) - Obtener una camiseta por ID
@app.route('/camisetas/<int:id>', methods=['GET'])
def get_camiseta(id):
    camiseta = Camiseta.query.get_or_404(id)
    return jsonify({
        "id": camiseta.id,
        "talla": camiseta.talla,
        "color": camiseta.color,
        "material": camiseta.material,
        "precio": str(camiseta.precio)
    })

# Ruta para crear (Create)
@app.route('/camisetas', methods=['POST'])
def create_camiseta():
    data = request.get_json()
    new_camiseta = Camiseta(
        talla=data['talla'],
        color=data['color'],
        material=data['material'],
        precio=data['precio']
    )
    db.session.add(new_camiseta)
    db.session.commit()
    return jsonify({
        "message": "Camiseta creada exitosamente",
        "camiseta": {
            "id": new_camiseta.id,
            "talla": new_camiseta.talla,
            "color": new_camiseta.color,
            "material": new_camiseta.material,
            "precio": str(new_camiseta.precio)
        }
    }), 201

# Ruta para actualizar (Update)
@app.route('/camisetas/<int:id>', methods=['PUT'])
def update_camiseta(id):
    camiseta = Camiseta.query.get_or_404(id)
    data = request.get_json()

    camiseta.talla = data['talla']
    camiseta.color = data['color']
    camiseta.material = data['material']
    camiseta.precio = data['precio']

    db.session.commit()
    return jsonify({
        "message": "Camiseta actualizada exitosamente",
        "camiseta": {
            "id": camiseta.id,
            "talla": camiseta.talla,
            "color": camiseta.color,
            "material": camiseta.material,
            "precio": str(camiseta.precio)
        }
    })

# Ruta para eliminar (Delete)
@app.route('/camisetas/<int:id>', methods=['DELETE'])
def delete_camiseta(id):
    camiseta = Camiseta.query.get_or_404(id)
    db.session.delete(camiseta)
    db.session.commit()
    return jsonify({"message": "Camiseta eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
