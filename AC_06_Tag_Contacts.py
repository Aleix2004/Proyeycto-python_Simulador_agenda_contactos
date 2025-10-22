import json
import os
from utils import mostrar_banner
import AC_json_2 as acjson  # usamos tus funciones para leer contactos


# === CREAR ETIQUETA ===
def crear_etiqueta_json():
    """Crea una nueva etiqueta (archivo JSON) con estructura inicial"""
    mostrar_banner("CREAR NUEVA ETIQUETA JSON")
    
    nombre_etiqueta = input("Nombre de la nueva etiqueta: ").strip()
    
    if not nombre_etiqueta:
        print("El nombre no puede estar vacío.")
        return None
    
    caracteres_invalidos = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in caracteres_invalidos:
        if char in nombre_etiqueta:
            print(f"El nombre no puede contener el carácter: {char}")
            return None
    
    nombre_archivo = nombre_etiqueta + ".json"
    
    if os.path.exists(nombre_archivo):
        print(f"La etiqueta '{nombre_etiqueta}' ya existe.")
        return None
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4, ensure_ascii=False)
        
        print(f"Etiqueta '{nombre_etiqueta}' creada exitosamente.")
        return nombre_archivo
        
    except Exception as e:
        print(f"Error al crear la etiqueta: {e}")
        return None


# === MOSTRAR ETIQUETAS EXISTENTES ===
def listar_etiquetas():
    """Muestra las etiquetas JSON disponibles en el directorio"""
    archivos = [f for f in os.listdir() if f.endswith(".json") and f != "contactos.json"]
    if not archivos:
        print("No hay etiquetas creadas todavía.")
        return []
    
    print("\n📂 Etiquetas disponibles:")
    for i, archivo in enumerate(archivos, start=1):
        print(f"  {i}. {archivo.replace('.json', '')}")
    
    return archivos


# === AÑADIR CONTACTO A ETIQUETA ===
def agregar_contacto_a_etiqueta():
    """Agrega un contacto existente del archivo contactos.json a una etiqueta"""
    mostrar_banner("AÑADIR CONTACTO A ETIQUETA")

    contactos = acjson.cargar_contactos()
    if not contactos:
        print("No hay contactos en el archivo principal (contactos.json).")
        return

    print("\n👥 Lista de contactos:")
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c.get('nombre')} {c.get('apellido')} - {c.get('correo')}")

    try:
        seleccion = int(input("\nSelecciona el número del contacto a añadir: "))
        if seleccion < 1 or seleccion > len(contactos):
            print("Número no válido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    contacto = contactos[seleccion - 1]

    etiquetas = listar_etiquetas()
    if not etiquetas:
        print("\nNo hay etiquetas. Crea una primero.")
        return

    try:
        seleccion_etiqueta = int(input("\nSelecciona el número de la etiqueta: "))
        if seleccion_etiqueta < 1 or seleccion_etiqueta > len(etiquetas):
            print("Número no válido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    nombre_archivo = etiquetas[seleccion_etiqueta - 1]

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contactos_etiqueta = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        contactos_etiqueta = []

    if any(c.get("correo") == contacto.get("correo") for c in contactos_etiqueta):
        print("⚠️ El contacto ya está en esta etiqueta.")
        return

    contactos_etiqueta.append(contacto)

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(contactos_etiqueta, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Contacto '{contacto['nombre']} {contacto['apellido']}' añadido a la etiqueta '{nombre_archivo.replace('.json', '')}'.")


# === VER ETIQUETAS Y SUS CONTACTOS ===
def mostrar_etiquetas_y_contactos():
    """Muestra todas las etiquetas con los contactos asociados"""
    mostrar_banner("ETIQUETAS Y CONTACTOS")

    etiquetas = [f for f in os.listdir() if f.endswith(".json") and f != "contactos.json"]
    if not etiquetas:
        print("No hay etiquetas creadas.")
        return

    for archivo in etiquetas:
        nombre_etiqueta = archivo.replace(".json", "")
        print(f"\n📁 {nombre_etiqueta.upper()}")
        print("-" * 60)

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contactos = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            contactos = []

        if not contactos:
            print("  (Sin contactos asignados)")
        else:
            for i, c in enumerate(contactos, start=1):
                print(f"  {i}. {c.get('nombre', '')} {c.get('apellido', '')} - {c.get('correo', '')}")

    print("\n" + "=" * 60)


# === MENÚ PRINCIPAL DE ETIQUETAS ===
def gestionar_etiquetas():
    """Menú principal de gestión de etiquetas"""
    while True:
        mostrar_banner("GESTIÓN DE ETIQUETAS JSON")
        print("   1. Crear nueva etiqueta vacía")
        print("   2. Ver etiquetas existentes")
        print("   3. Agregar contacto a una etiqueta")
        print("   4. Ver etiquetas con sus contactos")
        print("   0. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción (0-4): ").strip()
        
        if opcion == "0":
            break
        elif opcion == "1":
            crear_etiqueta_json()
        elif opcion == "2":
            listar_etiquetas()
        elif opcion == "3":
            agregar_contacto_a_etiqueta()
        elif opcion == "4":
            mostrar_etiquetas_y_contactos()
        else:
            print("Opción no válida.")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    gestionar_etiquetas()
