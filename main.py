import os
import a_c_1
import show_list
import Delete_contact
import AC_json_2 as acjson
import AC_05
import AC_06_Tag_Contacts
import send_email  # tu archivo send_email.py


def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("📇 SISTEMA DE GESTIÓN DE CONTACTOS")
        print("=" * 60)
        print("1. Crear nuevo contacto (guardar en JSON)")
        print("2. Ver o filtrar contactos (desde JSON)")
        print("3. Borrar contactos del archivo JSON")
        print("4. Modificar contacto / etiqueta")
        print("5. Gestionar etiquetas")
        print("6. Salir")
        print("=" * 60)

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            crear_contacto_json()
        elif opcion == "2":
            submenu_ver_contactos_json()
        elif opcion == "3":
            borrar_contactos_json()
        elif opcion == "4":
            AC_05.gestionar_modificar()
        elif opcion == "5":
            AC_06_Tag_Contacts.gestionar_etiquetas()
        elif opcion == "6":
            print("\nGracias por usar el sistema de contactos. ¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


# === OPCIÓN 1: CREAR Y GUARDAR CONTACTOS ===
def crear_contacto_json():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 60)
    print("📝 CREAR NUEVO CONTACTO (se guarda en JSON)")
    print("=" * 60)
    nombre = input("* Nombre: ").strip()
    apellido = input("* Apellido: ").strip()
    telefono = input("* Teléfono: ").strip()
    correo = input("* Correo: ").strip()
    user = input("* User: ").strip()

    nuevo_contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo": correo,
        "user": user
    }

    ok = acjson.save_contact(nuevo_contacto)
    if ok:
        print(f"\n✓ Contacto de {nombre} {apellido} guardado exitosamente en JSON.")

        # === Enviar correo al contacto nuevo (modo prueba) ===
        print("📧 Simulando envío de correo de bienvenida...")
        send_email.enviar_notificacion(correo, nombre, modo="console")

    else:
        print("\n⚠️ No se pudo guardar el contacto.")

    input("Presiona Enter para continuar...")


# === OPCIÓN 2: VER Y FILTRAR CONTACTOS ===
def submenu_ver_contactos_json():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("👁️  VER / FILTRAR CONTACTOS (desde JSON)")
        print("=" * 60)
        print("1. Ver todos los contactos")
        print("2. Filtrar contactos por criterio")
        print("3. Volver al menú principal")
        print("=" * 60)
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            contactos = acjson.cargar_contactos()
            if contactos:
                show_list.contactos = contactos
                show_list.ver_contactos()
            else:
                print("\nNo hay contactos guardados en el archivo JSON.")
                input("Presiona Enter para continuar...")

        elif opcion == "2":
            contactos = acjson.cargar_contactos()
            if contactos:
                show_list.contactos = contactos
                show_list.filtrar_contactos()
            else:
                print("\nNo hay contactos guardados en el archivo JSON.")
                input("Presiona Enter para continuar...")

        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida.")
            input("Presiona Enter para continuar...")


# === OPCIÓN 3: BORRAR CONTACTOS DEL JSON ===
def borrar_contactos_json():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 60)
    print("🗑️  BORRAR CONTACTOS DESDE ARCHIVO JSON")
    print("=" * 60)

    nombre_archivo = acjson.DEFAULT_JSON
    contactos = Delete_contact.cargar_contactos(nombre_archivo)
    if not contactos:
        print("No hay contactos para borrar.")
        input("Presiona Enter para continuar...")
        return

    Delete_contact.mostrar_contactos(contactos)
    contactos = Delete_contact.borrar_contacto(contactos)
    Delete_contact.guardar_contactos(nombre_archivo, contactos)
    input("Presiona Enter para continuar...")


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    menu_principal()
