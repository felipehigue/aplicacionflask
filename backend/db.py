import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine(mysql.connector.connect(user="root", password="123456789", host="localhost", database="policamisetas", port="3307"))
connection_string = "mysql+mysqlconnector://root:123456789@localhost:3307/policamisetas?charset=utf8mb4&collation=utf8mb4_general_ci"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()