from pymongo import MongoClient

def cargar_datos_ejemplo():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["PF_Informatica1"]
    coleccion = db["reportes_tecnicos"]

    # Documento de ejemplo
    reporte = {
        "reporte_id": "rep-20240612-003",
        "mmto_id": 58,
        "equipo_id": "EQ-ICU-0032",
        "nombre_equipo": "Ventilador mecánico Puritan Bennett 980",
        "tipo_reporte": "Correctivo",
        "reporte_fecha": "2024-06-12T10:45:00Z",
        "tecnico_id": "tech789",
        "tecnico_nombre": "Carlos Ruiz",
        "resumen": "Se reemplazó el sensor de flujo principal tras falla intermitente. Se calibró y verificó funcionamiento.",
        "notas_tecnicas": [
            "Error detectado: alarma persistente de flujo bajo.",
            "Se inspeccionó el sensor de flujo y se detectó sulfatación en conectores.",
            "Se reemplazó el sensor de flujo y se realizó calibración de volumen.",
            "Prueba de validación realizada en modo de simulación pulmonar, parámetros dentro de rango."
        ],
        "estado": "Reparado",
        "rutas": {
            "imagen_antes": "/uploads/images/vent980_pre_mant.jpg",
            "imagen_despues": "/uploads/images/vent980_post_mant.jpg",
            "reporte_pdf": "/uploads/reports/vent980_mant_20240612.pdf",
            "guia_pdf": "/files/vents/guial0112.pdf",
            "manual_pdf": "/files/vents/Manual0112.pdf"
        }
    }

    resultado = coleccion.insert_one(reporte)
    print("Documento insertado con _id:", resultado.inserted_id)

if __name__ == "__main__":
    cargar_datos_ejemplo()
