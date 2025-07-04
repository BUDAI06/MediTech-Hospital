import mysql.connector

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="info2025_2",
            database="PF_Informatica1"
        )
        print("Conexión a MySQL exitosa")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión a MySQL: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    conn = conectar_mysql()
    if conn:
        conn.close()