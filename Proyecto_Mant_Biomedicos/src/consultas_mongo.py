from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["PF_Informatica1"]

def ver_reportes_tecnicos():
    reportes = db["reportes_tecnicos"].find()
    print("\n📑 Reportes técnicos:")
    for r in reportes:
        print(f"- {r['reporte_id']} | {r['nombre_equipo']} ({r['tipo_reporte']})")
        print(f"  Técnico: {r['tecnico_nombre']} | Estado: {r['estado']}")
        print(f"  Resumen: {r['resumen']}\n")

def descargar_manuales():
    manuales = db["manuales"].find()
    for m in manuales:
        nombre = m["nombre_equipo"].replace(" ", "_")
        with open(f"./descargas/{nombre}_manual.txt", "w", encoding="utf-8") as f:
            f.write(f"Manual ID: {m['manual_id']}\nNotas: {m['notas']}")
        print(f"📥 Manual descargado: {nombre}_manual.txt")

def ver_bitacoras():
    bitacoras = db["bitacoras"].find()
    print("\n📘 Bitácoras registradas:")
    for b in bitacoras:
        print(f"- Bitácora: {b['bitacora_id']} | Equipo: {b['equipo_id']} | Fecha: {b['fecha']}")
        for entrada in b["entradas"]:
            print(f"  [{entrada['fecha']}] → {entrada['evento']}")

def buscar_reporte_por_palabra():
    palabra = input("🔍 Palabra clave: ")
    reportes = db["reportes_tecnicos"].find({
        "resumen": {"$regex": palabra, "$options": "i"}
    })

    print("\n🔎 Resultados de búsqueda:")
    for r in reportes:
        print(f"- {r['reporte_id']}: {r['nombre_equipo']} | {r['resumen']}")
