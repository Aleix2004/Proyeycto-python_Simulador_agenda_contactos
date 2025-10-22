import os
import json

# Archivo JSON por defecto (puedes cambiar el nombre si quieres)
DEFAULT_JSON = "contactos.json"

# Lista en memoria (se inicializa desde el JSON si existe)
contactos = []

def cargar_contactos(nombre_archivo=DEFAULT_JSON):
    """
    Carga contactos desde el archivo JSON.
    Devuelve lista o [] si no existe o está vacío.
    """
    if not os.path.exists(nombre_archivo):
        return []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if isinstance(datos, list):
                return datos
            else:
                # si el contenido no es lista, devolvemos vacía
                return []
    except (json.JSONDecodeError, IOError):
        return []

def guardar_contactos(contactos_a_guardar, nombre_archivo=DEFAULT_JSON):
    """
    Guarda la lista de contactos en el archivo JSON.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(contactos_a_guardar, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
        return False

def save_contact(contacto, nombre_archivo=DEFAULT_JSON):
    """
    Añade un contacto al archivo JSON (lo crea si no existe).
    Devuelve True si se guardó correctamente.
    """
    actuales = cargar_contactos(nombre_archivo)
    actuales.append(contacto)
    ok = guardar_contactos(actuales, nombre_archivo)
    # mantener lista en memoria sincronizada
    global contactos
    contactos = actuales
    return ok

# Al importar el módulo, inicializamos contacts desde el fichero (si existe)
contactos = cargar_contactos(DEFAULT_JSON)


# Funciones auxiliares para mostrar (opcionalmente usadas por el main)
def mostrar_contactos_en_memoria():
    if not contactos:
        print("No hay contactos guardados en JSON.")
        return
    print(f"\n{'#':<3} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'CORREO':<20} {'USER':<15}")
    print("-" * 80)
    for i, c in enumerate(contactos, 1):
        print(f"{i:<3} {c.get('nombre',''):<15} {c.get('apellido',''):<15} {c.get('telefono',''):<15} {c.get('correo',''):<20} {c.get('user',''):<15}")
