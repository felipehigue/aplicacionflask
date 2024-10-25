import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

# Cargar las variables del archivo .env
load_dotenv()

# Configuración de la URL de la base de datos para SQLAlchemy
MYSQL_USER = os.getenv('MYSQLUSER')
MYSQL_PASSWORD = os.getenv('MYSQLPASSWORD')
MYSQL_HOST = os.getenv('MYSQLHOST')
MYSQL_PORT = int(os.getenv('MYSQLPORT', 3306))  # Asegurarse de que sea un entero
MYSQL_DATABASE = os.getenv('MYSQLDATABASE')
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# Inicializar SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('camiseta'):
            db.create_all()
