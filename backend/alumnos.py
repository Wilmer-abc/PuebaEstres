from backend.db import conectar_bd


def agregar_alumno(carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nac):
    conexion = conectar_bd()
    if not conexion:
        print("Error: No se pudo conectar a la base de datos.")
        return  
    
    cursor = conexion.cursor()
    sql = """
    INSERT INTO alumnos (carnet1, carnet2, carnet3, PrimerNombre, SegundoNombre, PrimerApellido, SegundoApellido, Telefono, Correoelectronico, Pagado, FechaNacimiento)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nac)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()


def actualizar_alumno(carnet1, carnet2, carnet3, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nac):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = """
    UPDATE alumnos 
    SET PrimerNombre=%s, SegundoNombre=%s, PrimerApellido=%s, SegundoApellido=%s, Telefono=%s, Correoelectronico=%s, Pagado=%s, FechaNacimiento=%s 
    WHERE carnet1=%s AND carnet2=%s AND carnet3=%s
    """
    valores = (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, pagado, fecha_nac, carnet1, carnet2, carnet3)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()


def eliminar_alumno(carnet1, carnet2, carnet3):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = "DELETE FROM alumnos WHERE carnet1=%s AND carnet2=%s AND carnet3=%s"
    cursor.execute(sql, (carnet1, carnet2, carnet3))
    conexion.commit()
    conexion.close()


import mysql.connector

def obtener_alumno(carnet1, carnet2, carnet3):
    try:
        conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ingenieria"
        )
        cursor = conexion.cursor(dictionary=True)

        sql = """
            SELECT * FROM alumnos 
            WHERE carnet1=%s AND carnet2=%s AND carnet3=%s
        """
        valores = (carnet1, carnet2, carnet3)

        cursor.execute(sql, valores)
        alumno = cursor.fetchone()  

        cursor.close()
        conexion.close()

        return alumno  

    except mysql.connector.Error as err:
        print("Error al obtener alumno:", err)
        return None


import mysql.connector

def eliminar_alumno(carnet1, carnet2, carnet3):
    try:
        conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ingenieria"
        )
        cursor = conexion.cursor()

        sql = """
            DELETE FROM alumnos 
            WHERE carnet1=%s AND carnet2=%s AND carnet3=%s
        """
        valores = (carnet1, carnet2, carnet3)

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        print("Error al eliminar alumno:", err)
