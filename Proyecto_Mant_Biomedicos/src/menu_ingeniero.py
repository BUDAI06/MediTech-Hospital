from src.equipos import listar_equipos
from src.mantenimientos import historial_mantenimientos
from src.consultas_mongo import ver_reportes_tecnicos, descargar_manuales, buscar_reporte_por_palabra
from src.conexion_mysql import conectar_mysql
def menu_ingeniero():
    while True:
        print("""
        === Menú Ingeniero ===
        1. Ver todos los equipos
        2. Consultar historial de mantenimientos
        3. Ver reportes técnicos
        4. Descargar manuales y bitácoras
        5. Buscar reporte por palabra clave
        6. Salir / Cerrar sesión
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_equipos()
        elif opcion == "2":
            historial_mantenimientos()
        elif opcion == "3":
            ver_reportes_tecnicos()
        elif opcion == "4":
            descargar_manuales()
        elif opcion == "5":
            buscar_reporte_por_palabra()
        elif opcion == "6":
            print("Sesión cerrada. Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

