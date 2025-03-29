import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establece conexión con la base de datos MySQL a través de PHPMyAdmin"""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # Normalmente 'localhost' si PHPMyAdmin está local
            database='ingenieria', # Nombre de tu base de datos
            user='root',           # Usuario común en XAMPP/WAMP (o el que hayas configurado)
            password='',           # Contraseña (vacía por defecto en XAMPP)
            port='3306'            # Puerto default de MySQL
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL/phpMyAdmin: {e}")
        return None