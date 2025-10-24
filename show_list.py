# Lista en memoria para almacenar contactos (volátil)
contactos = []

def ver_contactos():
    print("\n" + "="*50)
    print("LISTA DE CONTACTOS (ordenada por nombre)")
    print("="*50)

    if not contactos:
        print("No hay contactos guardados.")
    else:
        # Ordenar por nombre automáticamente
        contactos_ordenados = sorted(contactos, key=lambda x: x.get('nombre', '').lower())

        print(f"{'#':<3} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'CORREO':<20} {'USER':<15}")
        print("-" * 80)

        for i, contacto in enumerate(contactos_ordenados, 1):
            print(f"{i:<3} {contacto['nombre']:<15} {contacto['apellido']:<15} {contacto['telefono']:<15} {contacto['correo']:<20} {contacto['user']:<15}")

    print("="*50)
    input("Presiona Enter para continuar...")

def filtrar_contactos():
    print("\n" + "="*50)
    print("FILTRAR CONTACTOS")
    print("="*50)
    criterio = input("Ingresa el criterio de búsqueda (nombre, apellido, telefono, correo, user): ").lower()
    valor = input("Ingresa el valor a buscar: ").lower()

    resultados = [contacto for contacto in contactos if valor in contacto.get(criterio, '').lower()]

    if resultados:
        print(f"\n{'#':<3} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'CORREO':<20} {'USER':<15}")
        print("-" * 80)
        for i, contacto in enumerate(resultados, 1):
            print(f"{i:<3} {contacto['nombre']:<15} {contacto['apellido']:<15} {contacto['telefono']:<15} {contacto['correo']:<20} {contacto['user']:<15}")
    else:
        print("\nNo se encontraron contactos que coincidan con el criterio.")

    input("Presiona Enter para continuar...")

def menu():
    while True:
        print("\n" + "="*50)
        print("GESTOR DE CONTACTOS")
        print("="*50)
        print("1. Ver todos los contactos")
        print("2. Filtrar contactos por criterio")
        print("3. Salir")
        print("="*50)

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            ver_contactos()
        elif opcion == '2':
            filtrar_contactos()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

# Ejecutar menú principal
if __name__ == "__main__":
    menu()