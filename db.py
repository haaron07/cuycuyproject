from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'gsgcorp_kevindev'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'b;yhD@U4a&H6'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'gsgcorppe.com' # localhost
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'gsgcorp_prueba_ing'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
