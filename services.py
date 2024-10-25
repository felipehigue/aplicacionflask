<<<<<<< Updated upstream:app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/mysql'
app.config['SECRET_KEY'] = 'secret_key'
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
=======
from flask import Flask, jsonify, request
from models import Camiseta
from database import db, init_db

# Configuración de la aplicación Flask
app = Flask(__name__)
init_db(app)

# Ruta para leer todas las camisetas
>>>>>>> Stashed changes:services.py
@app.route('/camisetas', methods=['GET'])
def get_camisetas():
    camisetas = Camiseta.query.all()
    camisetas_list = [{"id": camiseta.id, "talla": camiseta.talla, "color": camiseta.color, 
                       "material": camiseta.material, "precio": str(camiseta.precio)} for camiseta in camisetas]
    return jsonify(camisetas_list)

# Ruta para leer una camiseta por ID
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

# Ruta para crear una camiseta (datos ingresados por consola en Thunder Client)
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

# Ruta para actualizar una camiseta
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

# Ruta para eliminar una camiseta
@app.route('/camisetas/<int:id>', methods=['DELETE'])
def delete_camiseta(id):
    camiseta = Camiseta.query.get_or_404(id)
    db.session.delete(camiseta)
    db.session.commit()
    return jsonify({"message": "Camiseta eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)