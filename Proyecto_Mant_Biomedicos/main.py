from src.login import login

def menu_admin():
    print("""
    1. CRUD Equipos
    2. Registrar usuarios
    3. Asignar roles
    4. Ver mantenimientos
    5. Cargar manuales técnicos
    6. Gestionar bitácoras y reportes
    7. Cerrar sesión
    """)

def menu_ingeniero():
    print("""
    1. Ver equipos
    2. Consultar historial de mantenimientos
    3. Ver reportes técnicos
    4. Descargar manuales y bitácoras
    5. Buscar por palabra clave
    6. Cerrar sesión
    """)

def menu_tecnico():
    print("""
    1. Ver equipos asignados
    2. Registrar mantenimiento preventivo
    3. Registrar mantenimiento correctivo
    4. Subir reporte técnico
    5. Consultar reportes anteriores
    6. Cerrar sesión
    """)

if __name__ == "__main__":
    rol = login()
    if rol == "Administrador":
        menu_admin()
    elif rol == "Ingeniero":
        menu_ingeniero()
    elif rol == "Tecnico":
        menu_tecnico()
    else:
        print("No tiene acceso al sistema.")
