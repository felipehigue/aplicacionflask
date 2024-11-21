from flask import Flask, jsonify, request, session
from backend.models import Usuarios
from backend.models import Camisetas
from flask_cors import CORS

import backend.db as db



app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas
app.config['SECRET_KEY'] = '123456789'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/getUsuarios',methods=['GET'])
def usuarios():
   # misU = Usuario.query.all()
    misU = db.session.query(Usuarios).all()
    usuariosArr = []
    for p in misU:
        usuariosArr.append(p.toDict()) 
        return jsonify(usuariosArr)

@app.route('/insertUsuario',methods=['POST'])
def insertUsuario():
    data = request.get_json()
    print(data)
    try:
        id_usuario = request.json['id_usuario']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        correo = request.json['correo']
        rol = request.json['rol']
        usuario = request.json['usuario']
        contraseña = request.json['contraseña']
        print(id_usuario)
        p = Usuarios(id_usuario, nombre, apellido,correo, rol, usuario, contraseña)

        db.session.add(p)
        db.session.commit()
        return jsonify({'statusCode' : 200, 'message': 'Success'})
    except Exception as e:
        return jsonify({'statusCode' : 400, 'err' : True, 'message' : str(e)})

@app.route('/deleteUsuario/<int:id_usuario>', methods=['DELETE'])
def deleteUsuario(id_usuario):
    try:
        usuario = db.session.query(Usuarios).filter_by(id_usuario=id_usuario).first()
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'statusCode': 200, 'message': 'Usuario eliminado con éxito'})
        else:
            return jsonify({'statusCode': 404, 'err': True, 'message': 'Usuario no encontrado'})
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})
    

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    user = db.session.query(Usuarios).filter_by(usuario=usuario, contraseña=contraseña).first()
    if user:
        session['logged_in'] = True
        session['user_id'] = user.id_usuario
        return jsonify({'message': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401
    
    
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return jsonify({'message': 'Sesión cerrada con éxito'})


@app.route('/getCamiseta/<int:id_camiseta>', methods=['GET'])
def getCamiseta(id_camiseta):
    camiseta = db.session.query(Camisetas).filter_by(id_camiseta=id_camiseta).first()
    if camiseta:
        return jsonify(camiseta.toDict())
    else:
        return jsonify({'statusCode': 404, 'message': 'Camiseta no encontrada'})
    

@app.route('/insertCamiseta', methods=['POST'])
def insertCamiseta():
    try:
        data = request.get_json()
        camiseta = Camisetas(
            id_camiseta=data['id_camiseta'],
            talla=data['talla'],
            color=data['color'],
            material=data['material'],
            precio=data['precio']
        )
        db.session.add(camiseta)
        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Camiseta creada con éxito'})
    except Exception as e:
        return jsonify({'statusCode': 400, 'message': str(e)})


@app.route('/updateCamiseta/<int:id_camiseta>', methods=['PUT'])
def updateCamiseta(id_camiseta):
    try:
        camiseta = db.session.query(Camisetas).filter_by(id_camiseta=id_camiseta).first()
        if not camiseta:
            return jsonify({'statusCode': 404, 'message': 'Camiseta no encontrada'})
        
        data = request.get_json()
        camiseta.talla = data.get('talla', camiseta.talla)
        camiseta.color = data.get('color', camiseta.color)
        camiseta.material = data.get('material', camiseta.material)
        camiseta.precio = data.get('precio', camiseta.precio)

        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Camiseta actualizada con éxito'})
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})
    
   
@app.route('/deleteCamiseta/<int:id_camiseta>', methods=['DELETE'])
def deleteCamiseta(id_camiseta):
    try:
        camiseta = db.session.query(Camisetas).filter_by(id_camiseta=id_camiseta).first()
        if not camiseta:
            return jsonify({'statusCode': 404, 'message': 'Camiseta no encontrada'})
        
        db.session.delete(camiseta)
        db.session.commit()
        return jsonify({'statusCode': 200, 'message': 'Camiseta eliminada con éxito'})
    except Exception as e:
        return jsonify({'statusCode': 400, 'err': True, 'message': str(e)})



app.run("0.0.0.0",5000,debug=True)

