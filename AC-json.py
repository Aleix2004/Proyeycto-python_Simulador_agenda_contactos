import json
import os

def guardar_datos_en_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    # Si el archivo ya existe, cargamos los datos existentes
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            try:
                contenido = json.load(archivo)
            except json.JSONDecodeError:
                contenido = []
    else:
        contenido = []

    # Agregamos los nuevos datos
    contenido.append(datos)

    # Guardamos todo nuevamente
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)

    print(f"Datos guardados correctamente en '{nombre_archivo}'.")


def crear_datos():
    """Pide datos al usuario y los devuelve como diccionario."""
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")

    return {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }


def main():
    print("=== GESTOR DE DATOS JSON ===")
    while True:
        print("\nOpciones:")
        print("1. Agregar datos a un JSON")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_archivo = input("Nombre del archivo JSON (sin .json): ") + ".json"
            datos = crear_datos()
            guardar_datos_en_json(nombre_archivo, datos)

        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
