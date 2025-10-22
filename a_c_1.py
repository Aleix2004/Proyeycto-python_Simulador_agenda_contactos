import os
import AC_json_2 as acjson  # usamos el módulo que gestiona el JSON

# Nota: mantenemos una pequeña lista local para uso inmediato visual,
# pero la fuente de verdad será el JSON gestionado por acjson.contactos
contactos = acjson.contactos  # referencia a la lista cargada desde JSON

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
    
    nombre = input("* Nombre: ").strip()
    apellido = input("* Apellido: ").strip()
    telefono = input("* Teléfono: ").strip()
    correo = input("* Correo: ").strip()
    user = input("* User: ").strip()
    
    nuevo_contacto = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
        'user': user
    }

    # Guardar en JSON usando AC_json_2.save_contact
    ok = acjson.save_contact(nuevo_contacto)
    if ok:
        print(f"\n✓ Contacto de {nombre} {apellido} guardado exitosamente en el JSON.")
    else:
        # Si falla guardar, también lo añadimos a la lista en memoria para no perderlo
        contactos.append(nuevo_contacto)
        print("\n⚠️ No se pudo guardar en el JSON. Contacto añadido sólo en memoria.")
    input("Presiona Enter para continuar...")

def ver_contactos():
    print("\n" + "="*50)
    print("LISTA DE CONTACTOS")
    print("="*50)
    
    # Refrescamos la lista en memoria desde el JSON por si cambiaron
    global contactos
    contactos = acjson.cargar_contactos()  

    if not contactos:
        print("No hay contactos guardados.")
    else:
        print(f"{'#':<3} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'CORREO':<20} {'USER':<15}")
        print("-" * 80)
        
        for i, contacto in enumerate(contactos, 1):
            print(f"{i:<3} {contacto.get('nombre',''):<15} {contacto.get('apellido',''):<15} {contacto.get('telefono',''):<15} {contacto.get('correo',''):<20} {contacto.get('user',''):<15}")
    
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
            print("\n¡Gracias por usar el Sistema de Contactos! Hasta luego.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, selecciona 1, 2 o 3.")
            input("Presiona Enter para continuar...")

if __name__ == '__main__':
    main()
