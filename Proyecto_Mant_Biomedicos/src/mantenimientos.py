from src.conexion_mysql import conectar_mysql

def crear_mantenimiento():
    conn = conectar_mysql()
    cursor = conn.cursor()
    equipo_id = input("ID del equipo: ")
    tecnico_id = input("ID del técnico: ")
    tipo_mmto = input("Tipo de mantenimiento (Preventivo/Correctivo): ")
    fecha_mmto = input("Fecha del mantenimiento (YYYY-MM-DD): ")
    duracion_mmto = input("Duración (en horas): ")
    observaciones = input("Observaciones: ")

    sql = """INSERT INTO mantenimientos 
    (equipo_id, tecnico_id, tipo_mmto, fecha_mmto, duracion_mmto, observaciones)
    VALUES (%s, %s, %s, %s, %s, %s)"""
    valores = (equipo_id, tecnico_id, tipo_mmto, fecha_mmto, duracion_mmto, observaciones)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Mantenimiento registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar mantenimiento: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_mantenimientos():
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("""SELECT mmto_id, equipo_id, tecnico_id, tipo_mmto, fecha_mmto, 
                      duracion_mmto, observaciones FROM mantenimientos""")
    mantenimientos = cursor.fetchall()
    print("\nLista de mantenimientos:")
    for mant in mantenimientos:
        print(mant)
    cursor.close()
    conn.close()

def modificar_mantenimiento():
    conn = conectar_mysql()
    cursor = conn.cursor()
    mmto_id = input("ID del mantenimiento a modificar: ")
    equipo_id = input("Nuevo ID de equipo: ")
    tecnico_id = input("Nuevo ID de técnico: ")
    tipo_mmto = input("Nuevo tipo de mantenimiento (Preventivo/Correctivo): ")
    fecha_mmto = input("Nueva fecha (YYYY-MM-DD): ")
    duracion_mmto = input("Nueva duración (en horas): ")
    observaciones = input("Nuevas observaciones: ")

    sql = """UPDATE mantenimientos SET 
    equipo_id=%s, tecnico_id=%s, tipo_mmto=%s, fecha_mmto=%s, duracion_mmto=%s, observaciones=%s
    WHERE mmto_id=%s"""
    valores = (equipo_id, tecnico_id, tipo_mmto, fecha_mmto, duracion_mmto, observaciones, mmto_id)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Mantenimiento modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar mantenimiento: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_mantenimiento():
    conn = conectar_mysql()
    cursor = conn.cursor()
    mmto_id = input("ID del mantenimiento a eliminar: ")
    try:
        cursor.execute("DELETE FROM mantenimientos WHERE mmto_id=%s", (mmto_id,))
        conn.commit()
        print("Mantenimiento eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar mantenimiento: {e}")
    finally:
        cursor.close()
        conn.close()

def menu_mantenimientos():
    while True:
        print("""
        --- CRUD Mantenimientos ---
        1. Crear mantenimiento
        2. Listar mantenimientos
        3. Modificar mantenimiento
        4. Eliminar mantenimiento
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_mantenimiento()
        elif opcion == "2":
            listar_mantenimientos()
        elif opcion == "3":
            modificar_mantenimiento()
        elif opcion == "4":
            eliminar_mantenimiento()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

