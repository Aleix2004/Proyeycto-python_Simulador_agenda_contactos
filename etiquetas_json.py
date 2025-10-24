import json
import os
from utils import limpiar_pantalla, mostrar_banner

def crear_etiqueta_json():
    """Crea una nueva etiqueta (archivo JSON) con estructura inicial"""
    limpiar_pantalla()  # Limpiar la pantalla de la terminal
    mostrar_banner("CREAR NUEVA ETIQUETA JSON")  # Mostrar título con formato
    
    # Solicitar nombre de la nueva etiqueta al usuario
    nombre_etiqueta = input("Nombre de la nueva etiqueta: ").strip()  # Eliminar espacios en blanco
    
    # Validar que el nombre no esté vacío
    if not nombre_etiqueta:
        print("El nombre no puede estar vacio.")
        input("\nPresiona Enter para continuar...")
        return None  # Retornar None indicando que no se creó la etiqueta
    
    # Validar caracteres no permitidos en nombres de archivo
    caracteres_invalidos = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in caracteres_invalidos:
        if char in nombre_etiqueta:
            print(f"El nombre no puede contener el caracter: {char}")
            input("\nPresiona Enter para continuar...")
            return None  # Retornar None si hay caracteres inválidos
    
    # Construir el nombre completo del archivo con extensión .json
    nombre_archivo = nombre_etiqueta + ".json"
    
    # Verificar si el archivo ya existe para evitar sobrescribir
    if os.path.exists(nombre_archivo):
        print(f"La etiqueta '{nombre_etiqueta}' ya existe.")
        input("\nPresiona Enter para continuar...")
        return None  # Retornar None si el archivo ya existe
    
    try:
        # Crear archivo JSON con array vacío
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            # Escribir estructura JSON inicial con array vacío
            json.dump([], archivo, indent=4, ensure_ascii=False)
            # json.dump parameters:
            # - []: array vacío como estructura inicial
            # - indent=4: formato legible con indentación de 4 espacios
            # - ensure_ascii=False: permitir caracteres no ASCII (tildes, ñ, etc.)
        
        print(f"Etiqueta '{nombre_etiqueta}' creada exitosamente.")
        input("\nPresiona Enter para continuar...")
        return nombre_archivo  # Retornar el nombre del archivo creado
        
    except Exception as e:
        # Manejar cualquier error durante la creación del archivo
        print(f"Error al crear la etiqueta: {e}")
        input("\nPresiona Enter para continuar...")
        return None  # Retornar None en caso de error

def gestionar_etiquetas():
    """Menu principal de gestion de etiquetas"""
    while True:  # Bucle infinito para mantener el menú activo
        limpiar_pantalla()  # Limpiar pantalla en cada iteración
        mostrar_banner("GESTION DE ETIQUETAS JSON")  # Mostrar título del menú
        print("   1. Crear nueva etiqueta vacia")  # Opción para crear etiqueta
        print("   0. Volver al menu principal")    # Opción para salir
        
        # Solicitar opción al usuario
        opcion = input("\nSelecciona una opcion (0-1): ").strip()  # strip() elimina espacios
        
        if opcion == "0":
            break  # Romper el bucle y volver al menú principal
        elif opcion == "1":
            crear_etiqueta_json()  # Llamar función para crear nueva etiqueta
        else:
            print("Opcion no valida.")  # Manejar opción inválida
            input("\nPresiona Enter para continuar...")  # Pausa para que usuario vea el mensaje

if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el archivo se ejecuta directamente
    # No se ejecuta cuando el archivo se importa como módulo
    gestionar_etiquetas()  # Iniciar el menú de gestión de etiquetas