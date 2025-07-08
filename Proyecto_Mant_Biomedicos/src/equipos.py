from src.conexion_mysql import conectar_mysql

def crear_equipo():
    conn = conectar_mysql()
    cursor = conn.cursor()
    equipo_id = input("ID del equipo (ej: EQ-ICU-0032): ")
    nombre_equipo = input("Nombre del equipo: ")
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ubicacion = input("Ubicación: ")
    fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ")
    estado_actual = input("Estado actual: ")

    sql = """INSERT INTO equipos 
    (equipo_id, nombre_equipo, tipo, marca, modelo, ubicacion, fecha_ingreso, estado_actual)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    valores = (equipo_id, nombre_equipo, tipo, marca, modelo, ubicacion, fecha_ingreso, estado_actual)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Equipo creado exitosamente.")
    except Exception as e:
        print(f"Error al crear equipo: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_equipos():
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT equipo_id, nombre_equipo, tipo, marca, modelo, ubicacion, fecha_ingreso, estado_actual FROM equipos")
    equipos = cursor.fetchall()
    print("\nLista de equipos:")
    for equipo in equipos:
        print(equipo)
    cursor.close()
    conn.close()

def modificar_equipo():
    conn = conectar_mysql()
    cursor = conn.cursor()
    equipo_id = input("ID del equipo a modificar: ")
    nombre_equipo = input("Nuevo nombre del equipo: ")
    tipo = input("Nuevo tipo: ")
    marca = input("Nueva marca: ")
    modelo = input("Nuevo modelo: ")
    ubicacion = input("Nueva ubicación: ")
    fecha_ingreso = input("Nueva fecha de ingreso (YYYY-MM-DD): ")
    estado_actual = input("Nuevo estado actual: ")

    sql = """UPDATE equipos SET 
    nombre_equipo=%s, tipo=%s, marca=%s, modelo=%s, ubicacion=%s, fecha_ingreso=%s, estado_actual=%s
    WHERE equipo_id=%s"""
    valores = (nombre_equipo, tipo, marca, modelo, ubicacion, fecha_ingreso, estado_actual, equipo_id)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Equipo modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar equipo: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_equipo():
    conn = conectar_mysql()
    cursor = conn.cursor()
    equipo_id = input("ID del equipo a eliminar: ")
    try:
        cursor.execute("DELETE FROM equipos WHERE equipo_id=%s", (equipo_id,))
        conn.commit()
        print("Equipo eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar equipo: {e}")
    finally:
        cursor.close()
        conn.close()

def menu_equipos():
    while True:
        print("""
        --- CRUD Equipos ---
        1. Crear equipo
        2. Listar equipos
        3. Modificar equipo
        4. Eliminar equipo
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            modificar_equipo()
        elif opcion == "4":
            eliminar_equipo()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
