from src.conexion_mysql import conectar_mysql

def crear_usuario():
    conn = conectar_mysql()
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
    cursor = conn.cursor()
    cursor.execute("SELECT usuario_id, nombre_usuario, rol FROM usuarios")
    usuarios = cursor.fetchall()
    print("\nLista de usuarios:")
    for usuario in usuarios:
        print(usuario)
    cursor.close()
    conn.close()

def modificar_usuario():
    conn = conectar_mysql()
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
