from src.conexion_mysql import conectar_mysql

def crear_usuario():
    conn = conectar_mysql()
    if conn is None:
        print("No se pudo conectar a MySQL. Revisa usuario y contraseña.")
        return
    cursor = conn.cursor()
    nombre_usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    rol = input("Rol (Administrador, Ingeniero, Tecnico): ")
    sql = "INSERT INTO usuarios (nombre_usuario, password, rol) VALUES (%s, %s, %s)"
    valores = (nombre_usuario, password, rol)
    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Usuario creado exitosamente.")
    except Exception as e:
        print(f"Error al crear usuario: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_usuarios():
    conn = conectar_mysql()
    if conn is None:
        print("No se pudo conectar a MySQL. Revisa usuario y contraseña.")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT usuario_id, nombre_usuario, rol FROM usuarios")
    usuarios = cursor.fetchall()
    print("\nLista de usuarios:")
    print("ID\tUsuario\t\tRol")
    print("--\t-------\t\t---")
    for usuario in usuarios:
        print(f"{usuario[0]}\t{usuario[1]}\t\t{usuario[2]}")
    cursor.close()
    conn.close()

def modificar_usuario():
    conn = conectar_mysql()
    if conn is None:
        print("No se pudo conectar a MySQL. Revisa usuario y contraseña.")
        return
    cursor = conn.cursor()
    usuario_id = input("ID de usuario a modificar: ")
    nuevo_nombre = input("Nuevo nombre de usuario: ")
    nuevo_rol = input("Nuevo rol (Administrador, Ingeniero, Tecnico): ")
    sql = "UPDATE usuarios SET nombre_usuario=%s, rol=%s WHERE usuario_id=%s"
    valores = (nuevo_nombre, nuevo_rol, usuario_id)
    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Usuario modificado exitosamente.")
    except Exception as e:
        print(f"Error al modificar usuario: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_usuario():
    conn = conectar_mysql()
    if conn is None:
        print("No se pudo conectar a MySQL. Revisa usuario y contraseña.")
        return
    cursor = conn.cursor()
    usuario_id = input("ID de usuario a eliminar: ")
    try:
        cursor.execute("DELETE FROM usuarios WHERE usuario_id=%s", (usuario_id,))
        conn.commit()
        print("Usuario eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
    finally:
        cursor.close()
        conn.close()

def menu_usuarios():
    while True:
        print("""
--- CRUD Usuarios ---
1. Crear usuario
2. Listar usuarios
3. Modificar usuario
4. Eliminar usuario
5. Volver
""")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
