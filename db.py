from ast import If, Try
from cmath import e
from logging import exception
from msilib.schema import Error
from app import app
# from flask_mysqldb import MySQL
import pycouchdb
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# # Mysql Settings
# app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'gsgcorp_kevindev'
# app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'b;yhD@U4a&H6'
# app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'gsgcorppe.com' # localhost
# app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'gsgcorp_prueba_ing'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# # MySQL Connection
# mysql = MySQL(app)
# server = couchdb2.Server() 
# db = server.create("test")
server = pycouchdb.Server("http://eddy:Madara75437029@localhost:5984/")


# couchdb = server.create("python-tests")
couchdb = server.database("python-tests")

try:
    print("Conectado!!")
    
except  e:
    print(e)
    
    
# doc= {"type":"Person","name":"Jhon Doe"}
# doc_rev = db.save(doc)
# db.delete("6386867113334782bc1cd0109a21ec60")
# doc_get = db.query("docidname/viewname","Content-Type – application/json")
# try:
#     print("Obtener!!")
#     print(doc_get)
# except  e:
#     print(e)
    
# if(server):{
#     print("Conectado")
# }
