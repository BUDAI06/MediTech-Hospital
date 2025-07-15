import mysql.connector

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",            
            port=3306,                    
            user="root",          
            password= "",          
            database="PF_Informatica1"    
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión a MySQL: {e}")
        return None

