import os
import AC_json_2 as acjson
from utils import mostrar_banner, mostrar_subtitulo, mostrar_etiquetas, guardar_cambios
from AC_06_Tag_Contacts import crear_etiqueta_json  # si necesitas crear nuevas etiquetas


def modificar_etiqueta():
    """Permite cambiar el nombre de una etiqueta (archivo JSON)."""
    mostrar_banner("MODIFICAR NOMBRE DE ETIQUETA")
    
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return
    
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")
    
    try:
        eleccion = int(input("\nSelecciona la etiqueta a modificar (numero): "))
        if eleccion == 0:
            return
        
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            return
        
        archivo_viejo = etiquetas[eleccion-1] + ".json"
        nuevo_nombre = input("Nuevo nombre para la etiqueta (deja vacio para volver): ").strip()
        
        if nuevo_nombre == "":
            print("Operacion cancelada.")
            return
            
        nuevo_nombre_archivo = nuevo_nombre + ".json"
        
        if nuevo_nombre_archivo == archivo_viejo:
            print("El nombre es el mismo. No se realizaron cambios.")
            return
        
        if os.path.exists(nuevo_nombre_archivo):
            print("Ya existe una etiqueta con ese nombre.")
            return
        
        os.rename(archivo_viejo, nuevo_nombre_archivo)
        print(f"Etiqueta renombrada de '{archivo_viejo}' a '{nuevo_nombre_archivo}'")
        
    except Exception as e:
        print(f"Error al modificar la etiqueta: {e}")


def modificar_contenido_etiqueta():
    """Permite modificar el contenido de una etiqueta especifica."""
    mostrar_banner("MODIFICAR CONTENIDO DE ETIQUETA")
    
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return
    
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")
    
    try:
        eleccion = int(input("\nSelecciona la etiqueta a modificar (numero): "))
        if eleccion == 0:
            return
        
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            return
        
        archivo_seleccionado = etiquetas[eleccion-1] + ".json"
        
        # Cargar datos desde AC_json_2
        datos_archivo = acjson.cargar_contactos(archivo_seleccionado)
        if not datos_archivo:
            print("No hay registros en esta etiqueta.")
            return
        
        # Mostrar los registros disponibles
        print("\nRegistros disponibles:")
        for i, registro in enumerate(datos_archivo, 1):
            print(f"{i}. {registro.get('nombre','')} {registro.get('apellido','')} - {registro.get('correo','')}")
        
        indice = int(input("\nSelecciona el número del registro a modificar (0 para volver): "))
        if indice == 0:
            return
        if indice < 1 or indice > len(datos_archivo):
            print("Indice invalido.")
            return
        
        registro = datos_archivo[indice-1]
        
        mostrar_banner("REGISTRO SELECCIONADO")
        print(f"Nombre: {registro.get('nombre', '')}")
        print(f"Apellido: {registro.get('apellido', '')}")
        print(f"Telefono: {registro.get('telefono', '')}")
        print(f"Correo: {registro.get('correo', '')}")
        print("=" * 60)
        
        # Menú de modificación
        while True:
            mostrar_subtitulo("CAMPOS DISPONIBLES PARA MODIFICAR")
            print("   1. Modificar nombre")
            print("   2. Modificar apellido")
            print("   3. Modificar telefono")
            print("   4. Modificar correo")
            print("   5. Modificar todos los campos")
            print("   0. Volver al menu principal")
            
            opcion = int(input("\nSelecciona una opcion (0-5): "))
            
            if opcion == 0:
                break
            elif opcion == 1:
                registro['nombre'] = input("Nuevo nombre: ")
            elif opcion == 2:
                registro['apellido'] = input("Nuevo apellido: ")
            elif opcion == 3:
                registro['telefono'] = input("Nuevo telefono: ")
            elif opcion == 4:
                registro['correo'] = input("Nuevo correo: ")
            elif opcion == 5:
                registro['nombre'] = input("Nuevo nombre: ")
                registro['apellido'] = input("Nuevo apellido: ")
                registro['telefono'] = input("Nuevo telefono: ")
                registro['correo'] = input("Nuevo correo: ")
            else:
                print("Opcion invalida. Intenta de nuevo.")
                continue
            
            # Guardar cambios
            acjson.guardar_contactos(datos_archivo, archivo_seleccionado)
            print("Cambios guardados correctamente.")
            
            continuar = input("\nDeseas modificar otro campo de este registro? (s/n): ").lower()
            if continuar != 's':
                break
        
    except Exception as e:
        print(f"Error al modificar datos: {e}")


def gestionar_modificar():
    """Menu principal para modificar"""
    while True:
        mostrar_banner("MODIFICAR DATOS")
        print("   1. Modificar nombre de etiqueta")
        print("   2. Modificar contenido de etiqueta")
        print("   0. Volver al menu principal")
        
        opcion = input("\nSelecciona una opcion (0-2): ").strip()
        
        if opcion == "0":
            break
        elif opcion == "1":
            modificar_etiqueta()
        elif opcion == "2":
            modificar_contenido_etiqueta()
        else:
            print("Opcion no valida, intenta de nuevo.")

        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    gestionar_modificar()
