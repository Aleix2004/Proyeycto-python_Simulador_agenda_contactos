import json
import os
from utils import mostrar_banner

def crear_etiqueta_json():
    """Crea una nueva etiqueta (archivo JSON) con estructura inicial"""
    mostrar_banner("CREAR NUEVA ETIQUETA JSON")
    
    nombre_etiqueta = input("Nombre de la nueva etiqueta: ").strip()
    
    if not nombre_etiqueta:
        print("El nombre no puede estar vacio.")
        return None
    
    # Validar caracteres no permitidos en nombres de archivo
    caracteres_invalidos = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in caracteres_invalidos:
        if char in nombre_etiqueta:
            print(f"El nombre no puede contener el caracter: {char}")
            return None
    
    nombre_archivo = nombre_etiqueta + ".json"
    
    # Verificar si ya existe
    if os.path.exists(nombre_archivo):
        print(f"La etiqueta '{nombre_etiqueta}' ya existe.")
        return None
    
    try:
        # Crear archivo JSON con array vacio
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)
        
        print(f"Etiqueta '{nombre_etiqueta}' creada exitosamente.")
        return nombre_archivo
        
    except Exception as e:
        print(f"Error al crear la etiqueta: {e}")
        return None

def gestionar_etiquetas():
    """Menu principal de gestion de etiquetas"""
    while True:
        mostrar_banner("GESTION DE ETIQUETAS JSON")
        print("   1. Crear nueva etiqueta vacia")
        print("   0. Volver al menu principal")
        
        opcion = input("\nSelecciona una opcion (0-1): ").strip()
        
        if opcion == "0":
            break
        elif opcion == "1":
            crear_etiqueta_json()
        else:
            print("Opcion no valida.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    gestionar_etiquetas()