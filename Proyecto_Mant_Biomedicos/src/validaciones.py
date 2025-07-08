def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_alfabetico(valor):
    return valor.replace(" ", "").isalpha()

def es_email(valor):
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", valor))
