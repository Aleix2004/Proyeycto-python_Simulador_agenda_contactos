import json
import os

def cargar_contactos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contactos = json.load(f)
            if not isinstance(contactos, list):
                print(f"El archivo '{nombre_archivo}' no contiene una lista de contactos.")
                return None
            return contactos
    except json.JSONDecodeError:
        print(f"Error: el archivo '{nombre_archivo}' no contiene un JSON válido.")
        return None

def guardar_contactos(nombre_archivo, contactos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(contactos, f, indent=4, ensure_ascii=False)
        print("Archivo guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
        return

    print(f"\n{'#':<3} {'Nombre':<15} {'Apellido':<15} {'Teléfono':<15} {'Correo':<25} {'User':<15}")
    print("-" * 90)
    for i, c in enumerate(contactos, 1):
        print(f"{i:<3} {c.get('nombre', ''):<15} {c.get('apellido', ''):<15} {c.get('telefono', ''):<15} {c.get('correo', ''):<25} {c.get('user', ''):<15}")

def borrar_contacto(contactos):
    mostrar_contactos(contactos)
    if not contactos:
        return contactos

    try:
        indice = int(input("\nIngresa el número del contacto a borrar: "))
        if 1 <= indice <= len(contactos):
            eliminado = contactos.pop(indice - 1)
            print(f"Contacto '{eliminado.get('nombre', '')} {eliminado.get('apellido', '')}' borrado exitosamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes ingresar un número válido.")
    return contactos

def main():
    print("=== BORRAR CONTACTO EN ARCHIVO JSON ===")
    nombre_archivo = input("Nombre del archivo JSON (con extensión .json): ").strip()

    contactos = cargar_contactos(nombre_archivo)
    if contactos is None:
        return

    while True:
        print("\nOpciones:")
        print("1. Mostrar contactos")
        print("2. Borrar contacto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_contactos(contactos)
        elif opcion == "2":
            contactos = borrar_contacto(contactos)
            guardar_contactos(nombre_archivo, contactos)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
