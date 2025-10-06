import os

# Lista en memoria para almacenar contactos (volátil)
contactos = []

def mostrar_menu():
    print("\n" + "="*50)
    print("SISTEMA DE CONTACTOS")
    print("="*50)
    print("1. Crear nuevo contacto")
    print("2. Ver lista de contactos")
    print("3. Salir")
    print("="*50)

def crear_contacto():
    print("\n" + "="*50)
    print("CREAR NUEVO CONTACTO")
    print("="*50)
    print("Rellena estos campos. Los campos marcados con * son obligatorios.")
    
    # Campos obligatorios
    nombre = input("* Nombre: ")
    apellido = input("* Apellido: ")
    telefono = input("* Teléfono: ")
    correo = input("* Correo: ")
    user = input("* User: ")
    
    # Guardar contacto en memoria (lista)
    nuevo_contacto = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
        'user': user
    }
    contactos.append(nuevo_contacto)
    
    print(f"\n✓ Contacto de {nombre} {apellido} guardado exitosamente!")
    input("Presiona Enter para continuar...")

def ver_contactos():
    print("\n" + "="*50)
    print("LISTA DE CONTACTOS")
    print("="*50)
    
    if not contactos:
        print("No hay contactos guardados.")
    else:
        print(f"{'#':<3} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'CORREO':<20} {'USER':<15}")
        print("-" * 80)
        
        for i, contacto in enumerate(contactos, 1):
            print(f"{i:<3} {contacto['nombre']:<15} {contacto['apellido']:<15} {contacto['telefono']:<15} {contacto['correo']:<20} {contacto['user']:<15}")
    
    print("="*50)
    input("Presiona Enter para continuar...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            crear_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            print("\n¡Gracias por usar el Sistema de Contactos!")
            print("Todos los contactos se han eliminado de la memoria.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, selecciona 1, 2 o 3.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()