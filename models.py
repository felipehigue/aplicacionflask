from database import db

class Camiseta(db.Model):
    __tablename__ = 'camiseta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
