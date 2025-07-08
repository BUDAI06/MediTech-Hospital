from pymongo import MongoClient

def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["PF_Informatica1"]
        return db
    except Exception as e:
        print(f"Error de conexión a MongoDB: {e}")
        return None

