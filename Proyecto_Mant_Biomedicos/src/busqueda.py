from src.conexion_mysql import conectar_mysql
from src.conexion_mongo import conectar_mongo

def menu_busqueda():
    while True:
        print("""
        --- Submenú de Búsqueda ---
        1. Buscar equipo por ID (con historial y reportes)
        2. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("Funcionalidad en desarrollo")
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")
