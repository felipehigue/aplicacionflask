import backend.db as db
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Usuarios(db.Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=True)
    apellido = Column(String, nullable=True)
    correo = Column(String, nullable=True)
    rol = Column(String, nullable=True)
    usuario = Column(String, nullable=True)
    contraseña = Column(String, nullable=True)

    def __init__(self, id_usuario, nombre, apellido, correo, rol, usuario, contraseña):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.rol = rol
        self.usuario = usuario
        self.contraseña = contraseña

    def __repr__(self):
        return f'Usuarios({self.id_usuario}, {self.nombre}, {self.apellido}, {self.correo}, {self.rol}, {self.usuario}, {self.contraseña})'
    def __str__(self):
        return self.nombre
    def toDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Camisetas(db.Base):
    __tablename__ = 'camisetas'
    id_camiseta = Column(Integer, primary_key=True)
    talla = Column(String, nullable=False)
    color = Column(String, nullable=False)
    material = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    def __init__(self, id_camiseta, talla, color, material, precio):
        self.id_camiseta = id_camiseta
        self.talla = talla
        self.color = color
        self.material = material
        self.precio = precio

    def __repr__(self):
        return f'Camisetas({self.id_camiseta}, {self.talla}, {self.color}, {self.material}, {self.precio})'

    def toDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   

class Ordenes(db.Base):
    __tablename__ = 'ordenes'
    idOrden = Column(Integer, primary_key=True)
    idCliente = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    total = Column(Float, nullable=False)
    estado = Column(String, nullable=False)

    cliente = relationship("Usuarios", back_populates="ordenes")

    def __init__(self, idOrden, idCliente, total, estado):
        self.idOrden = idOrden
        self.idCliente = idCliente
        self.total = total
        self.estado = estado

    def __repr__(self):
        return f'Orden({self.idOrden}, {self.idCliente}, {self.total}, {self.estado})'
    
    def toDict(self):
        return {
            'idOrden': self.idOrden,
            'idCliente': self.idCliente,
            'total': self.total,
            'estado': self.estado
        }


Usuarios.ordenes = relationship("Ordenes", order_by=Ordenes.idOrden, back_populates="cliente")