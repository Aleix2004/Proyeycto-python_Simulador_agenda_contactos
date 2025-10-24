import json
import os
from utils import limpiar_pantalla, mostrar_banner, mostrar_etiquetas

def crear_datos():
    """Solicita datos al usuario."""
    limpiar_pantalla()
    mostrar_banner("CREAR NUEVO REGISTRO")
    print(" Deja vacio y presiona Enter para volver al menu principal ")
    print("=" * 60)
    
    # Solicitar nombre - si está vacío, cancelar toda la operación
    nombre = input("Nombre: ")
    if nombre == "":
        return None  # Retorna None para indicar que se canceló la operación
        
    # Solicitar apellido - misma validación
    apellido = input("Apellido: ")
    if apellido == "":
        return None
        
    # Solicitar teléfono
    telefono = input("Telefono: ")
    if telefono == "":
        return None
        
    # Solicitar correo electrónico
    correo = input("Correo: ")
    if correo == "":
        return None

    # Retornar diccionario con todos los datos recolectados
    return {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
    }

def guardar_datos_en_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    try:
        # Verificar si el archivo ya existe
        if os.path.exists(nombre_archivo):
            # Si existe, leer el contenido actual
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                try:
                    # Intentar cargar el JSON existente
                    contenido = json.load(archivo)
                    # Asegurarse de que el contenido sea una lista
                    if not isinstance(contenido, list):
                        contenido = [contenido]  # Convertir a lista si es un solo diccionario
                except json.JSONDecodeError:
                    # Si el archivo está corrupto o vacío, empezar con lista vacía
                    contenido = []
        else:
            # Si el archivo no existe, crear una lista vacía
            contenido = []

        # Agregar los nuevos datos a la lista existente
        contenido.append(datos)

        # Escribir la lista actualizada de vuelta al archivo
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)
            # Parámetros de json.dump:
            # - indent=4: formato legible con indentación
            # - ensure_ascii=False: permite caracteres especiales (tildes, ñ, etc.)

        print(f"Datos guardados correctamente en '{nombre_archivo}'.")
        
    except Exception as e:
        # Manejar cualquier error durante el proceso de guardado
        print(f"Error al guardar datos: {e}")

def poner_datos_json():
    """Funcion principal para agregar datos a etiquetas"""
    limpiar_pantalla()
    # Obtener lista de etiquetas disponibles
    etiquetas = mostrar_etiquetas()
    mostrar_banner("AGREGAR DATOS A ETIQUETAS")
    print("Etiquetas existentes:")
    
    # Mostrar etiquetas disponibles o mensaje si no hay ninguna
    if etiquetas:
        for i, et in enumerate(etiquetas, 1):  # Enumerar desde 1
            print(f"   {i}. {et}")
    else:
        print("   No hay etiquetas aun")
    
    print("   0. Volver al menu principal")
    
    # Obtener selección del usuario
    eleccion = input("\nElige una etiqueta (numero): ").strip().lower()

    # Si elige 0, volver al menú principal
    if eleccion == "0":
        return
    
    try:
        # Convertir la entrada a número y validar
        eleccion_num = int(eleccion)
        if eleccion_num < 1 or eleccion_num > len(etiquetas):
            print("Opcion invalida.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Obtener el nombre de la etiqueta seleccionada
        nombre_etiqueta = etiquetas[eleccion_num-1]  # -1 porque la lista empieza en 0
        nombre_archivo = nombre_etiqueta + ".json"   # Agregar extensión .json
        
    except ValueError:
        # Manejar caso donde la entrada no es un número
        print("Opcion invalida.")
        input("\nPresiona Enter para continuar...")
        return

    # Crear nuevos datos (solicita información al usuario)
    datos = crear_datos()
    
    # Si se crearon datos exitosamente (no se canceló), guardarlos
    if datos is not None:
        guardar_datos_en_json(nombre_archivo, datos)

if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el archivo se ejecuta directamente
    poner_datos_json()  # Iniciar la función principal