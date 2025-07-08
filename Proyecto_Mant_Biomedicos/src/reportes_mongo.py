from src.conexion_mongo import conectar_mongo

def crear_reporte_tecnico():
    db = conectar_mongo()
    coleccion = db["reportes_tecnicos"]

    reporte = {
        "reporte_id": input("ID del reporte: "),
        "mmto_id": int(input("ID de mantenimiento (mmto_id): ")),
        "equipo_id": input("ID del equipo: "),
        "nombre_equipo": input("Nombre del equipo: "),
        "tipo_reporte": input("Tipo de reporte (Preventivo/Correctivo): "),
        "reporte_fecha": input("Fecha del reporte (YYYY-MM-DDTHH:MM:SSZ): "),
        "tecnico_id": input("ID del técnico: "),
        "tecnico_nombre": input("Nombre del técnico: "),
        "resumen": input("Resumen del trabajo realizado: "),
        "notas_tecnicas": input("Notas técnicas (separadas por punto y coma): ").split(";"),
        "estado": input("Estado final (Reparado, Pendiente, etc.): "),
        "rutas": {
            "imagen_antes": input("Ruta imagen antes: "),
            "imagen_despues": input("Ruta imagen después: "),
            "reporte_pdf": input("Ruta PDF del reporte: "),
            "guia_pdf": input("Ruta PDF de la guía: "),
            "manual_pdf": input("Ruta PDF del manual: ")
        }
    }

    resultado = coleccion.insert_one(reporte)
    print("Reporte técnico guardado con _id:", resultado.inserted_id)

def listar_reportes():
    db = conectar_mongo()
    coleccion = db["reportes_tecnicos"]

    for doc in coleccion.find():
        print(doc)

def buscar_reportes_por_equipo():
    db = conectar_mongo()
    coleccion = db["reportes_tecnicos"]
    equipo_id = input("Ingrese el ID del equipo: ")
    for doc in coleccion.find({"equipo_id": equipo_id}):
        print(doc)

def eliminar_reporte():
    db = conectar_mongo()
    coleccion = db["reportes_tecnicos"]
    reporte_id = input("Ingrese el ID del reporte a eliminar: ")
    resultado = coleccion.delete_one({"reporte_id": reporte_id})
    if resultado.deleted_count:
        print("Reporte eliminado.")
    else:
        print("No se encontró el reporte.")

def menu_reportes_tecnicos():
    while True:
        print("""
        --- Gestión de Reportes Técnicos (MongoDB) ---
        1. Crear reporte técnico
        2. Listar todos los reportes
        3. Buscar reportes por equipo
        4. Eliminar reporte técnico
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_reporte_tecnico()
        elif opcion == "2":
            listar_reportes()
        elif opcion == "3":
            buscar_reportes_por_equipo()
        elif opcion == "4":
            eliminar_reporte()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


# Puedes agregar modificar_reporte si quieres.
