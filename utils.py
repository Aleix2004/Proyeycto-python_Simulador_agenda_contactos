# utils.py
import json
import os

def mostrar_banner(texto):
    print("\n" + "="*50)
    print(f"   {texto}")
    print("="*50)

def mostrar_subtitulo(texto):
    print("\n" + "-"*50)
    print(f"   {texto}")
    print("-"*50)

def mostrar_etiquetas():
    """
    Devuelve la lista de archivos JSON en la carpeta actual como etiquetas.
    Solo archivos .json que no sean contactos.json
    """
    return [f.replace(".json","") for f in os.listdir() if f.endswith(".json") and f != "contactos.json"]

def guardar_cambios(nombre_archivo, datos):
    """Guarda una lista de diccionarios en un archivo JSON"""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("✅ Cambios guardados correctamente.")
    except Exception as e:
        print(f"⚠️ Error al guardar cambios: {e}")
