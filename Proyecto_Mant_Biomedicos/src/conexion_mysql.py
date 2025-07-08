import mysql.connector

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",             # O "127.0.0.1"
            port=3306,                    # Cambia si tienes otro puerto configurado
            user="root",          # Usuario de tu base de datos
            password= "",          # Contraseña
            database="PF_Informatica1"    # Nombre de la base de datos
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión a MySQL: {e}")
        return None

