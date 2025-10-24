import json
import os
from utils import limpiar_pantalla, mostrar_banner, mostrar_subtitulo, mostrar_etiquetas, guardar_cambios
from visualizar import crear_tabla_combinada

def modificar_etiqueta():
    """Permite cambiar el nombre de una etiqueta (archivo JSON)."""
    limpiar_pantalla()
    mostrar_banner("MODIFICAR NOMBRE DE ETIQUETA")
    
    # Obtener lista de etiquetas disponibles
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        input("\nPresiona Enter para continuar...")
        return
    
    # Mostrar menú de etiquetas disponibles
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")
    
    try:
        # Obtener selección del usuario
        eleccion = int(input("\nSelecciona la etiqueta a modificar (numero): "))
        if eleccion == 0:
            return  # Salir si el usuario elige volver
        
        # Validar que la opción esté en rango válido
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Construir nombres de archivo
        archivo_viejo = etiquetas[eleccion-1] + ".json"  # Nombre actual
        nuevo_nombre = input("Nuevo nombre para la etiqueta (deja vacio para volver): ").strip()
        
        # Validar que se ingresó un nombre
        if nuevo_nombre == "":
            print("Operacion cancelada.")
            input("\nPresiona Enter para continuar...")
            return
            
        nuevo_nombre_archivo = nuevo_nombre + ".json"  # Nuevo nombre con extensión
        
        # Verificar si el nombre es el mismo (no hay cambios)
        if nuevo_nombre_archivo == archivo_viejo:
            print("El nombre es el mismo. No se realizaron cambios.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Verificar que no exista ya una etiqueta con el nuevo nombre
        if os.path.exists(nuevo_nombre_archivo):
            print("Ya existe una etiqueta con ese nombre.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Renombrar el archivo físicamente en el sistema
        os.rename(archivo_viejo, nuevo_nombre_archivo)
        print(f"Etiqueta renombrada de '{archivo_viejo}' a '{nuevo_nombre_archivo}'")
        input("\nPresiona Enter para continuar...")
        
    except Exception as e:
        # Manejar errores durante el proceso de renombrado
        print(f"Error al modificar la etiqueta: {e}")
        input("\nPresiona Enter para continuar...")

def modificar_contenido_etiqueta():
    """Permite modificar el contenido de una etiqueta especifica."""
    limpiar_pantalla()
    mostrar_banner("MODIFICAR CONTENIDO DE ETIQUETA")
    
    # Obtener lista de etiquetas disponibles
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        input("\nPresiona Enter para continuar...")
        return
    
    # Mostrar menú de etiquetas
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")
    
    try:
        # Obtener selección de etiqueta
        eleccion = int(input("\nSelecciona la etiqueta a modificar (numero): "))
        if eleccion == 0:
            return
        
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            input("\nPresiona Enter para continuar...")
            return
        
        archivo_seleccionado = etiquetas[eleccion-1] + ".json"
        
        # Mostrar el contenido actual de la etiqueta en formato de tabla
        print(f"\nContenido actual de '{archivo_seleccionado}':")
        datos_completos = crear_tabla_combinada(filtro=archivo_seleccionado)
        if not datos_completos:
            input("\nPresiona Enter para continuar...")
            return
        
        # Convertir índice mostrado a índice interno
        indice_mostrado = int(input("\nIngresa el numero de indice del registro a modificar (o 0 para volver): "))
        if indice_mostrado == 0:
            return
        
        indice = indice_mostrado - 1  # Convertir base 1 a base 0
            
        # Validar que el índice esté en rango válido
        if indice < 0 or indice >= len(datos_completos):
            print("Indice invalido.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Obtener el registro seleccionado
        registro = datos_completos[indice]
        
        # Mostrar detalles del registro seleccionado
        limpiar_pantalla()
        mostrar_banner("REGISTRO SELECCIONADO")
        print(f"Nombre: {registro.get('nombre', '')}")
        print(f"Apellido: {registro.get('apellido', '')}")
        print(f"Telefono: {registro.get('telefono', '')}")
        print(f"Correo: {registro.get('correo', '')}")
        print("=" * 60)
        
        # Cargar el archivo original para encontrar el índice real
        with open(archivo_seleccionado, "r", encoding="utf-8") as f:
            datos_archivo = json.load(f)  # Cargar datos desde JSON
        
        # Encontrar el índice real dentro del archivo original
        indice_archivo = None
        if isinstance(datos_archivo, list):  # Si es una lista de registros
            for i, item in enumerate(datos_archivo):
                # Buscar coincidencia exacta en todos los campos clave
                if (item.get('nombre') == registro.get('nombre') and 
                    item.get('apellido') == registro.get('apellido') and
                    item.get('correo') == registro.get('correo')):
                    indice_archivo = i  # Guardar índice real
                    break
        else:
            # Si es un solo diccionario, convertirlo a lista
            datos_archivo = [datos_archivo]
            indice_archivo = 0  # Único registro tiene índice 0
        
        # Si no se encontró el registro, mostrar error
        if indice_archivo is None:
            print("No se pudo encontrar el registro en el archivo.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Menú para seleccionar qué campo modificar
        while True:
            limpiar_pantalla()
            mostrar_subtitulo("CAMPOS DISPONIBLES PARA MODIFICAR")
            print("   1. Modificar nombre")      # Modificar solo el nombre
            print("   2. Modificar apellido")    # Modificar solo el apellido
            print("   3. Modificar telefono")    # Modificar solo el teléfono
            print("   4. Modificar correo")      # Modificar solo el correo
            print("   5. Modificar todos los campos")  # Modificar todos los campos a la vez
            print("   0. Volver al menu principal")    # Salir
            
            opcion = int(input("\nSelecciona una opcion (0-5): "))
            
            if opcion == 0:
                return  # Salir al menú principal
            elif opcion == 1:
                # Modificar solo el nombre
                nuevo_valor = input("Nuevo nombre: ")
                datos_archivo[indice_archivo]['nombre'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)  # Guardar cambios en archivo
                print("Nombre modificado correctamente.")
                
            elif opcion == 2:
                # Modificar solo el apellido
                nuevo_valor = input("Nuevo apellido: ")
                datos_archivo[indice_archivo]['apellido'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Apellido modificado correctamente.")
                
            elif opcion == 3:
                # Modificar solo el teléfono
                nuevo_valor = input("Nuevo telefono: ")
                datos_archivo[indice_archivo]['telefono'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Telefono modificado correctamente.")
                
            elif opcion == 4:
                # Modificar solo el correo
                nuevo_valor = input("Nuevo correo: ")
                datos_archivo[indice_archivo]['correo'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Correo modificado correctamente.")
                
            elif opcion == 5:
                # Modificar todos los campos a la vez
                limpiar_pantalla()
                mostrar_banner("MODIFICAR TODOS LOS CAMPOS")
                datos_archivo[indice_archivo]['nombre'] = input("Nuevo nombre: ")
                datos_archivo[indice_archivo]['apellido'] = input("Nuevo apellido: ")
                datos_archivo[indice_archivo]['telefono'] = input("Nuevo telefono: ")
                datos_archivo[indice_archivo]['correo'] = input("Nuevo correo: ")
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Todos los campos modificados correctamente.")
                
            else:
                print("Opcion invalida. Intenta de nuevo.")
                input("\nPresiona Enter para continuar...")
                continue  # Volver al menú de campos
            
            # Preguntar si quiere seguir modificando otros campos del mismo registro
            continuar = input("\nDeseas modificar otro campo de este registro? (s/n): ").lower()
            if continuar != 's':
                break  # Salir del bucle de modificación de campos
        
    except Exception as e:
        # Manejar errores durante el proceso de modificación
        print(f"Error al modificar datos: {e}")
        input("\nPresiona Enter para continuar...")

def gestionar_modificar():
    """Menu principal para modificar"""
    while True:  # Bucle infinito para el menú de modificación
        limpiar_pantalla()
        mostrar_banner("MODIFICAR DATOS")
        print("   1. Modificar nombre de etiqueta")    # Renombrar archivo completo
        print("   2. Modificar contenido de etiqueta") # Editar registros específicos
        print("   0. Volver al menu principal")        # Salir al menú principal
        
        opcion = input("\nSelecciona una opcion (0-2): ").strip()
        
        if opcion == "0":
            break  # Salir del bucle y volver al menú principal
        elif opcion == "1":
            modificar_etiqueta()  # Llamar función para renombrar etiqueta
        elif opcion == "2":
            modificar_contenido_etiqueta()  # Llamar función para modificar registros
        else:
            print("Opcion no valida, intenta de nuevo.")  # Manejar opción inválida
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el archivo se ejecuta directamente
    gestionar_modificar()  # Iniciar el menú de modificación