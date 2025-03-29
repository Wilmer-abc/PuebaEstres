from flask import Flask, jsonify, request
from db import get_db_connection
import sys
import random
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Sistema de Alumnos</h1>
    <p>API endpoints:</p>
    <ul>
        <li><a href="/api/alumnos">/api/alumnos</a> (GET)</li>
        <li>/api/alumnos (POST)</li>
        <li>/api/alumnos/generar-masivos (POST)</li>
    </ul>
    """

@app.route('/api/alumnos', methods=['GET'])
def get_alumnos():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id, PrimerNombre, SegundoNombre, primerApellido, segundoApellido, 
                   CONCAT(PrimerNombre, ' ', COALESCE(SegundoNombre, '')) AS NombreCompleto, 
                   CONCAT(primerApellido, ' ', COALESCE(segundoApellido, '')) AS ApellidoCompleto, 
                   CONCAT(carnet1, '-', carnet2, '-', carnet3) AS Carnet, Pagado 
            FROM alumnos
        """)
        alumnos = cursor.fetchall()
        return jsonify(alumnos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
        

@app.route('/api/alumnos/generar-masivos', methods=['POST'])
def generar_alumnos_masivos():
    try:
        data = request.get_json()
        if not data or 'cantidad' not in data:
            return jsonify({"error": "Debe proporcionar la cantidad de registros a generar"}), 400
            
        cantidad = int(data['cantidad'])
        if cantidad <= 0 or cantidad > 5000:
            return jsonify({"error": "La cantidad debe ser mayor a 0 y menor o igual a 5000"}), 400
            
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Error de conexión a la base de datos"}), 500
        
        cursor = conn.cursor()
        start_time = time.time()
        
        batch_size = 100
        registros_insertados = 0
        nombres = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Fernanda']
        apellidos = ['Perez', 'Gomez', 'Rodriguez', 'Gonzalez', 'Lopez']
        
        for i in range(cantidad):
            carnet1 = f"{random.randint(1000, 9999)}"
            carnet2 = f"{random.randint(10, 99)}"
            carnet3 = f"{random.randint(10000, 99999)}"
            primer_nombre = random.choice(nombres)
            segundo_nombre = random.choice(nombres) if random.random() > 0.5 else ''
            primer_apellido = random.choice(apellidos)
            segundo_apellido = random.choice(apellidos) if random.random() > 0.5 else ''
            telefono = f"7{random.randint(1000000, 9999999)}"
            correo = f"{primer_nombre.lower()}.{primer_apellido.lower()}{i}@example.com"
            pagado = random.choice(['Sí', 'No'])
            fecha_nac = f"{random.randint(1980, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            
            cursor.execute(
                """INSERT INTO alumnos 
                (carnet1, carnet2, carnet3, PrimerNombre, SegundoNombre, primerApellido, segundoApellido, Telefono, CorreoElectronico, Pagado, FechaNacimiento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nac)
            )
            
            registros_insertados += 1
            if i % batch_size == 0:
                conn.commit()
        
        conn.commit()
        tiempo_total = time.time() - start_time
        
        return jsonify({
            "success": True,
            "message": f"{registros_insertados} registros generados exitosamente",
            "tiempo_total": round(tiempo_total, 2),
            "registros_por_segundo": round(registros_insertados/tiempo_total, 2)
        })
        
    except ValueError:
        return jsonify({"error": "La cantidad debe ser un número válido"}), 400
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"Error al generar registros: {str(e)}"}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    try:
        test_conn = get_db_connection()
        if test_conn:
            test_conn.close()
            print("✅ Conexión a la base de datos verificada")
        else:
            print("❌ Error en la conexión a la base de datos")
        
        app.run(debug=True, port=5000)
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)
