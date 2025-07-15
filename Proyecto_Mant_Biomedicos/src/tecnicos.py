from src.conexion_mysql import conectar_mysql

def crear_tecnico():
    conn = conectar_mysql()
    cursor = conn.cursor()
    nombre = input("Nombre del técnico: ")
    especialidad = input("Especialidad: ")
    cedula_profesional = input("Cédula profesional: ")
    contacto = input("Datos de contacto: ")

    sql = "INSERT INTO tecnicos (nombre, especialidad, cedula_profesional, contacto) VALUES (%s, %s, %s, %s)"
    valores = (nombre, especialidad, cedula_profesional, contacto)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Técnico creado exitosamente.")
    except Exception as e:
        print(f"Error al crear técnico: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_tecnicos():
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT tecnico_id, nombre, especialidad, cedula_profesional, contacto FROM tecnicos")
    tecnicos = cursor.fetchall()
    print("\nLista de técnicos:")
    for tecnico in tecnicos:
        print(tecnico)
    cursor.close()
    conn.close()

def modificar_tecnico():
    conn = conectar_mysql()
    cursor = conn.cursor()
    tecnico_id = input("ID del técnico a modificar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nueva_especialidad = input("Nueva especialidad: ")
    nueva_cedula = input("Nueva cédula profesional: ")
    nuevo_contacto = input("Nuevos datos de contacto: ")

    sql = "UPDATE tecnicos SET nombre=%s, especialidad=%s, cedula_profesional=%s, contacto=%s WHERE tecnico_id=%s"
    valores = (nuevo_nombre, nueva_especialidad, nueva_cedula, nuevo_contacto, tecnico_id)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Técnico modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar técnico: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_tecnico():
    conn = conectar_mysql()
    cursor = conn.cursor()
    tecnico_id = input("ID del técnico a eliminar: ")
    try:
        cursor.execute("DELETE FROM tecnicos WHERE tecnico_id=%s", (tecnico_id,))
        conn.commit()
        print("Técnico eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar técnico: {e}")
    finally:
        cursor.close()
        conn.close()

def menu_tecnicos():
    while True:
        print("""
        --- CRUD Técnicos ---
        1. Crear técnico
        2. Listar técnicos
        3. Modificar técnico
        4. Eliminar técnico
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_tecnico()
        elif opcion == "2":
            listar_tecnicos()
        elif opcion == "3":
            modificar_tecnico()
        elif opcion == "4":
            eliminar_tecnico()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

