

from flask import Flask, jsonify, request
from models import Camiseta
from database import db, init_db

# Configuración de la aplicación Flask
app = Flask(__name__)
init_db(app)

# Ruta para leer todas las camisetas
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
