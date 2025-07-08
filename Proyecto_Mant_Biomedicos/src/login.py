import json
import os

def cargar_usuarios_json():
    ruta = os.path.join(os.path.dirname(__file__), "../base_datos/mysql/ejemplo_usuarios.json")
    with open(ruta, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    return usuarios

def login():
    usuarios = cargar_usuarios_json()
    print("=== Login ===")
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    for u in usuarios:
        if u["nombre_usuario"] == user and u["password"] == pwd:
            print(f"\nBienvenido, {user}. Rol: {u['rol']}")
            return u["rol"]
    print("Usuario o contraseña incorrectos.")
    return None
