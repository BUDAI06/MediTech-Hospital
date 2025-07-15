from src.usuarios import menu_usuarios
from src.tecnicos import menu_tecnicos
from src.equipos import menu_equipos
from src.mantenimientos import menu_mantenimientos
from src.reportes_mongo import menu_reportes_tecnicos
from src.busqueda import menu_busqueda

def menu_admin():
    while True:
        print("""
=== Menú Administrador ===

1. CRUD Usuarios
2. CRUD Técnicos
3. CRUD Equipos
4. CRUD Mantenimientos
5. Gestión de reportes técnicos (MongoDB)
6. Submenú de búsqueda
7. Cerrar sesión
""")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_tecnicos()
        elif opcion == "3":
            menu_equipos()
        elif opcion == "4":
            menu_mantenimientos()
        elif opcion == "5":
            menu_reportes_tecnicos()
        elif opcion == "6":
            menu_busqueda()
        elif opcion == "7":
            print("Sesión cerrada. Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
