import json
import os
from AC_json_2 import cargar_contactos, guardar_contactos
from utils import mostrar_banner


def modificar_contacto_principal():
    """Permite modificar los contactos del archivo principal contactos.json"""
    mostrar_banner("MODIFICAR CONTACTO PRINCIPAL")

    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos guardados en el archivo principal.")
        input("Presiona Enter para continuar...")
        return

    print("\nLista de contactos:")
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} {c['apellido']} - {c['correo']}")

    try:
        indice = int(input("\nSelecciona el número del contacto a modificar (0 para cancelar): ")) - 1
        if indice == -1:
            print("Operación cancelada.")
            return
        if indice < 0 or indice >= len(contactos):
            print("Opción inválida.")
            return

        contacto = contactos[indice]
        print("\nDeja vacío un campo para mantener su valor actual.\n")

        nuevo_nombre = input(f"Nuevo nombre [{contacto['nombre']}]: ").strip() or contacto['nombre']
        nuevo_apellido = input(f"Nuevo apellido [{contacto['apellido']}]: ").strip() or contacto['apellido']
        nuevo_telefono = input(f"Nuevo teléfono [{contacto['telefono']}]: ").strip() or contacto['telefono']
        nuevo_correo = input(f"Nuevo correo [{contacto['correo']}]: ").strip() or contacto['correo']
        nuevo_user = input(f"Nuevo user [{contacto['user']}]: ").strip() or contacto['user']

        contacto.update({
            "nombre": nuevo_nombre,
            "apellido": nuevo_apellido,
            "telefono": nuevo_telefono,
            "correo": nuevo_correo,
            "user": nuevo_user
        })

        guardar_contactos(contactos)
        print("\n✅ Contacto modificado correctamente.")
    except ValueError:
        print("❌ Entrada inválida. Debes ingresar un número.")
    except Exception as e:
        print(f"❌ Error al modificar el contacto: {e}")

    input("\nPresiona Enter para continuar...")


def modificar_nombre_etiqueta():
    """Permite cambiar el nombre de una etiqueta (archivo JSON)."""
    mostrar_banner("MODIFICAR NOMBRE DE ETIQUETA")

    etiquetas = [f[:-5] for f in os.listdir() if f.endswith(".json") and f != "contactos.json"]
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return

    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menú principal")

    try:
        eleccion = int(input("\nSelecciona la etiqueta a modificar (número): "))
        if eleccion == 0:
            return

        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opción inválida.")
            return

        archivo_viejo = etiquetas[eleccion - 1] + ".json"
        nuevo_nombre = input("Nuevo nombre para la etiqueta: ").strip()

        if not nuevo_nombre:
            print("Operación cancelada.")
            return

        nuevo_archivo = nuevo_nombre + ".json"
        if os.path.exists(nuevo_archivo):
            print("Ya existe una etiqueta con ese nombre.")
            return

        os.rename(archivo_viejo, nuevo_archivo)
        print(f"Etiqueta renombrada de '{archivo_viejo}' a '{nuevo_archivo}' correctamente.")

    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")
    except Exception as e:
        print(f"Error al modificar la etiqueta: {e}")

    input("\nPresiona Enter para continuar...")


def gestionar_modificar():
    """Menú principal de modificación."""
    while True:
        mostrar_banner("MENÚ DE MODIFICACIÓN")
        print("1. Modificar contacto del archivo principal (contactos.json)")
        print("2. Modificar nombre de etiqueta")
        print("0. Volver al menú principal")

        opcion = input("\nSelecciona una opción (0-2): ").strip()       

        if opcion == "0":
            break
        elif opcion == "1":
            modificar_contacto_principal()
        elif opcion == "2":
            modificar_nombre_etiqueta()
        else:
            print("❌ Opción no válida, intenta de nuevo.")
            input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    gestionar_modificar()
