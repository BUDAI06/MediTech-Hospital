from pymongo import MongoClient

def cargar_bitacora():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["PF_Informatica1"]
    coleccion = db["bitacoras"]

    bitacora = {
        "bitacora_id": "bf-EQ-0032-20240610",
        "equipo_id": "EQ-ICU-0032",
        "fecha": "2024-06-10",
        "entradas": [
            {
                "fecha": "2024-06-10T08:15:00Z",
                "evento": "Reinicio inesperado durante prueba funcional"
            },
            {
                "fecha": "2024-06-10T10:40:00Z",
                "evento": "Falla intermitente en sensor de presión"
            }
        ],
        "registro_por": "tech789"
    }

    resultado = coleccion.insert_one(bitacora)
    print("Documento insertado en 'bitacoras' con _id:", resultado.inserted_id)

if __name__ == "__main__":
    cargar_bitacora()
