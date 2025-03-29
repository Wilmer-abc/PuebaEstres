from backend.db import conectar_bd

def obtener_estadisticas_edad():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        sql = """
            SELECT TIMESTAMPDIFF(YEAR, FechaNacimiento, CURDATE()) AS edad, COUNT(*) 
            FROM alumnos 
            GROUP BY edad 
            ORDER BY edad;
        """
        cursor.execute(sql)
        estadisticas = cursor.fetchall()
        conexion.close()
        return estadisticas
