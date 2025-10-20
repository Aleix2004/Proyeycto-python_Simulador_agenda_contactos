import json
import os
from utils import mostrar_banner, mostrar_subtitulo, input_validado, mostrar_etiquetas, guardar_cambios
from visualizar import crear_tabla_combinada

def modificar_etiqueta():
    """Permite cambiar el nombre de una etiqueta (archivo JSON)."""
    mostrar_banner("MODIFICAR ETIQUETA")
    
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return
    
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")
    
    try:
        eleccion = input_validado("\nSelecciona la etiqueta a modificar (numero): ", "numero")
        if eleccion is None or eleccion == 0:
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
        
    except ValueError:
        print("Por favor, ingresa un numero valido.")
    except Exception as e:
        print(f"Error al modificar la etiqueta: {e}")

def modificar_contenido_etiqueta():
    """Permite modificar el contenido de una etiqueta específica."""
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
        eleccion = input_validado("\nSelecciona la etiqueta a modificar (numero): ", "numero")
        if eleccion is None or eleccion == 0:
            return
        
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            return
        
        archivo_seleccionado = etiquetas[eleccion-1] + ".json"
        
        # Mostrar el contenido actual de la etiqueta (ordenado por nombre)
        print(f"\nContenido actual de '{archivo_seleccionado}':")
        datos_completos = crear_tabla_combinada(filtro=archivo_seleccionado)
        if not datos_completos:
            return
        
        # Seleccionar registro a modificar
        indice = input_validado("\nIngresa el numero de indice del registro a modificar (o 0 para volver): ", "numero")
        if indice is None or indice == 0:
            return
            
        if indice < 0 or indice >= len(datos_completos):
            print("Indice invalido.")
            return
        
        registro = datos_completos[indice]
        
        mostrar_banner("REGISTRO SELECCIONADO")
        print(f"Nombre: {registro.get('nombre', '')}")
        print(f"Apellido: {registro.get('apellido', '')}")
        print(f"Telefono: {registro.get('telefono', '')}")
        print(f"Correo: {registro.get('correo', '')}")
        print("=" * 60)
        
        # Cargar el archivo original
        with open(archivo_seleccionado, "r", encoding="utf-8") as f:
            datos_archivo = json.load(f)
        
        # Encontrar el índice dentro del archivo
        indice_archivo = None
        if isinstance(datos_archivo, list):
            for i, item in enumerate(datos_archivo):
                if (item.get('nombre') == registro.get('nombre') and 
                    item.get('apellido') == registro.get('apellido') and
                    item.get('correo') == registro.get('correo')):
                    indice_archivo = i
                    break
        else:
            # Si es un solo diccionario
            datos_archivo = [datos_archivo]
            indice_archivo = 0
        
        if indice_archivo is None:
            print("No se pudo encontrar el registro en el archivo.")
            return
        
        while True:
            mostrar_subtitulo("CAMPOS DISPONIBLES PARA MODIFICAR")
            print("   1. Modificar nombre")
            print("   2. Modificar apellido")
            print("   3. Modificar telefono")
            print("   4. Modificar correo")
            print("   5. Modificar todos los campos")
            print("   0. Volver al menu principal")
            
            opcion = input_validado("\nSelecciona una opcion (0-5): ", "numero")
            
            if opcion is None or opcion == 0:
                return
            elif opcion == 1:
                nuevo_valor = input("Nuevo nombre: ")
                datos_archivo[indice_archivo]['nombre'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Nombre modificado correctamente.")
                
            elif opcion == 2:
                nuevo_valor = input("Nuevo apellido: ")
                datos_archivo[indice_archivo]['apellido'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Apellido modificado correctamente.")
                
            elif opcion == 3:
                nuevo_valor = input("Nuevo telefono: ")
                datos_archivo[indice_archivo]['telefono'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Telefono modificado correctamente.")
                
            elif opcion == 4:
                nuevo_valor = input("Nuevo correo: ")
                datos_archivo[indice_archivo]['correo'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Correo modificado correctamente.")
                
            elif opcion == 5:
                mostrar_banner("MODIFICAR TODOS LOS CAMPOS")
                datos_archivo[indice_archivo]['nombre'] = input("Nuevo nombre: ")
                datos_archivo[indice_archivo]['apellido'] = input("Nuevo apellido: ")
                datos_archivo[indice_archivo]['telefono'] = input("Nuevo telefono: ")
                datos_archivo[indice_archivo]['correo'] = input("Nuevo correo: ")
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Todos los campos modificados correctamente.")
                
            else:
                print("Opcion invalida. Intenta de nuevo.")
            
            # Preguntar si quiere seguir modificando
            continuar = input("\n¿Deseas modificar otro campo de este registro? (s/n): ").lower()
            if continuar != 's':
                break
        
    except Exception as e:
        print(f"Error al modificar datos: {e}")