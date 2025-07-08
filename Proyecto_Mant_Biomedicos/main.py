from src.login import login
from src.menu_admin import menu_admin
from src.menu_ingeniero import menu_ingeniero
from src.menu_tecnico import menu_tecnico

def main():
    rol = login()
    if rol == "Administrador":
        menu_admin()
    elif rol == "Ingeniero":
        menu_ingeniero()
    elif rol == "Tecnico":
        menu_tecnico()
    else:
        print("Acceso denegado.")

if __name__ == "__main__":
    main()
