from pymongo import MongoClient

def cargar_manual():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["PF_Informatica1"]
    coleccion = db["manuales"]

    manual = {
        "manual_id": "man-EQ-0032-v1",
        "equipo_id": "EQ-ICU-0032",
        "nombre_equipo": "Puritan Bennett 980",
        "version": "1.2",
        "fecha_carga": "2024-05-10T13:00:00Z",
        "cargado_por": "admin_u",
        "file_path": "/uploads/manuals/pb980_manual_v1.2.pdf",
        "notas": "Versión en español. Incluye guía de calibración."
    }

    resultado = coleccion.insert_one(manual)
    print("Documento insertado en 'manuales' con _id:", resultado.inserted_id)
    

    
    


if __name__ == "__main__":
    cargar_manual()
