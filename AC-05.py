import json
import os

# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def crear_tabla_combinada(filtro=None):
    """Crea una tabla con los datos de todos o de un archivo JSON específico."""
    archivos_json = [archivo for archivo in os.listdir() if archivo.endswith('.json')]
    
    if not archivos_json:
        print("No hay archivos JSON (etiquetas) en el directorio actual.")
        return
    
    todos_los_datos = []
    
    for archivo in archivos_json:
        if filtro and archivo != filtro:
            continue
        
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                
            # Normaliza datos
            if isinstance(datos, list):
                for item in datos:
                    if isinstance(item, dict):
                        item['_archivo'] = archivo.replace('.json', '')
                        item['_indice'] = len(todos_los_datos)  # Índice global para modificación
                        todos_los_datos.append(item)
            elif isinstance(datos, dict):
                datos['_archivo'] = archivo.replace('.json', '')
                datos['_indice'] = len(todos_los_datos)
                todos_los_datos.append(datos)
                
        except json.JSONDecodeError:
            print(f"Error leyendo {archivo} - archivo corrupto")
        except Exception as e:
            print(f"Error leyendo {archivo}: {e}")
    
    if not todos_los_datos:
        print("No se encontraron datos para mostrar.")
        return
    
    return _crear_tabla_diccionarios(todos_los_datos)


def _crear_tabla_diccionarios(datos):
    """Crea tabla formateada para lista de diccionarios."""
    if not datos:
        return None
    
    # === Orden de columnas deseado ===
    claves = set()
    for item in datos:
        claves.update(item.keys())

    # Excluir campos internos de la visualización
    campos_internos = {'_archivo', '_indice'}
    orden_deseado = ["_indice", "_archivo", "nombre", "apellido", "correo", "telefono"]
    claves = [c for c in orden_deseado if c in claves] + [c for c in sorted(claves) if c not in orden_deseado and c not in campos_internos]
    
    # Calcular anchos
    anchos = {clave: len(str(clave)) for clave in claves}
    for item in datos:
        for clave in claves:
            valor = str(item.get(clave, ''))
            anchos[clave] = max(anchos[clave], len(valor))
    
    # Separador
    separador = "+"
    for clave in claves:
        separador += "-" * (anchos[clave] + 2) + "+"
    
    # Encabezado
    tabla = [separador]
    fila_encabezados = "|"
    for clave in claves:
        fila_encabezados += f" {clave:<{anchos[clave]}} |"
    tabla.append(fila_encabezados)
    tabla.append(separador)
    
    # Filas de datos
    for item in datos:
        fila = "|"
        for clave in claves:
            valor = str(item.get(clave, ''))
            fila += f" {valor:<{anchos[clave]}} |"
        tabla.append(fila)
    
    tabla.append(separador)
    
    # Imprimir
    print("\n" + "\n".join(tabla))
    print(f"\nTotal de registros: {len(datos)}")
    print(f"Etiquetas mostradas: {len(set(item.get('_archivo', '') for item in datos))}")
    
    return datos


def guardar_datos_en_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                try:
                    contenido = json.load(archivo)
                    if not isinstance(contenido, list):
                        contenido = [contenido]
                except json.JSONDecodeError:
                    contenido = []
        else:
            contenido = []

        contenido.append(datos)

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)

        print(f"Datos guardados correctamente en '{nombre_archivo}'.")
        
    except Exception as e:
        print(f"Error al guardar datos: {e}")


def crear_datos():
    """Solicita datos al usuario."""
    print("\nCrear nuevo registro (deja vacio y presiona Enter para volver al menu principal):")
    nombre = input("Nombre: ")
    if nombre == "":
        return None
        
    apellido = input("Apellido: ")
    if apellido == "":
        return None
        
    telefono = input("Telefono: ")
    if telefono == "":
        return None
        
    correo = input("Correo: ")
    if correo == "":
        return None

    return {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
    }


def modificar_etiqueta():
    """Permite cambiar el nombre de una etiqueta (archivo JSON)."""
    print("\nMODIFICAR ETIQUETA")
    
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return
    
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"{i}. {et.replace('.json', '')}")
    print("0. Volver al menu principal")
    
    try:
        eleccion = input("Selecciona la etiqueta a modificar (numero): ")
        if eleccion == "0":
            return
        
        eleccion = int(eleccion)
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            return
        
        archivo_viejo = etiquetas[eleccion-1]
        nuevo_nombre = input("Nuevo nombre para la etiqueta (deja vacio para volver): ").strip()
        
        if nuevo_nombre == "":
            print("Operacion cancelada.")
            return
            
        nuevo_nombre = nuevo_nombre + ".json"
        
        if nuevo_nombre == archivo_viejo:
            print("El nombre es el mismo. No se realizaron cambios.")
            return
        
        if os.path.exists(nuevo_nombre):
            print("Ya existe una etiqueta con ese nombre.")
            return
        
        os.rename(archivo_viejo, nuevo_nombre)
        print(f"Etiqueta renombrada de '{archivo_viejo}' a '{nuevo_nombre}'")
        
    except ValueError:
        print("Por favor, ingresa un numero valido.")
    except Exception as e:
        print(f"Error al modificar la etiqueta: {e}")


def modificar_contenido_etiqueta():
    """Permite modificar el contenido de una etiqueta específica."""
    print("\nMODIFICAR CONTENIDO DE ETIQUETA")
    
    etiquetas = mostrar_etiquetas()
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        return
    
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):
        print(f"{i}. {et.replace('.json', '')}")
    print("0. Volver al menu principal")
    
    try:
        eleccion = input("Selecciona la etiqueta a modificar (numero): ")
        if eleccion == "0":
            return
        
        eleccion = int(eleccion)
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            return
        
        archivo_seleccionado = etiquetas[eleccion-1]
        
        # Mostrar el contenido actual de la etiqueta
        print(f"\nContenido actual de '{archivo_seleccionado}':")
        datos_completos = crear_tabla_combinada(filtro=archivo_seleccionado)
        if not datos_completos:
            return
        
        # Seleccionar registro a modificar
        indice = input("\nIngresa el numero de indice del registro a modificar (o 0 para volver): ")
        if indice == "0":
            return
            
        indice = int(indice)
        if indice < 0 or indice >= len(datos_completos):
            print("Indice invalido.")
            return
        
        registro = datos_completos[indice]
        
        print(f"\nRegistro seleccionado:")
        print(f"Nombre: {registro.get('nombre', '')}")
        print(f"Apellido: {registro.get('apellido', '')}")
        print(f"Telefono: {registro.get('telefono', '')}")
        print(f"Correo: {registro.get('correo', '')}")
        
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
            print("\nCAMPOS DISPONIBLES PARA MODIFICAR:")
            print("1. Modificar nombre")
            print("2. Modificar apellido")
            print("3. Modificar telefono")
            print("4. Modificar correo")
            print("5. Modificar todos los campos")
            print("0. Volver al menu principal")
            
            opcion = input("\nSelecciona una opcion (0-5): ")
            
            if opcion == '0':
                return
            elif opcion == '1':
                nuevo_valor = input("Nuevo nombre: ")
                datos_archivo[indice_archivo]['nombre'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Nombre modificado correctamente.")
                
            elif opcion == '2':
                nuevo_valor = input("Nuevo apellido: ")
                datos_archivo[indice_archivo]['apellido'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Apellido modificado correctamente.")
                
            elif opcion == '3':
                nuevo_valor = input("Nuevo telefono: ")
                datos_archivo[indice_archivo]['telefono'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Telefono modificado correctamente.")
                
            elif opcion == '4':
                nuevo_valor = input("Nuevo correo: ")
                datos_archivo[indice_archivo]['correo'] = nuevo_valor
                guardar_cambios(archivo_seleccionado, datos_archivo)
                print("Correo modificado correctamente.")
                
            elif opcion == '5':
                print("\nModificar todos los campos:")
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
        
    except ValueError:
        print("Por favor, ingresa un numero valido.")
    except Exception as e:
        print(f"Error al modificar datos: {e}")


def guardar_cambios(nombre_archivo, datos):
    """Guarda los cambios en el archivo JSON."""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            if len(datos) == 1:
                json.dump(datos[0], f, indent=4, ensure_ascii=False)
            else:
                json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar cambios: {e}")


# ==============================
# MENU PRINCIPAL
# ==============================

def mostrar_etiquetas():
    """Devuelve una lista de archivos JSON (etiquetas)."""
    etiquetas = [f for f in os.listdir() if f.endswith('.json')]
    return etiquetas


def main():
    print("GESTOR DE DATOS JSON CON ETIQUETAS")
    
    while True:
        print("\nOpciones:")
        print("1. Agregar datos a una etiqueta (JSON)")
        print("2. Ver datos por etiqueta o todos")
        print("3. Modificar datos")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            etiquetas = mostrar_etiquetas()
            print("\nEtiquetas existentes:")
            if etiquetas:
                for i, et in enumerate(etiquetas, 1):
                    print(f"{i}. {et.replace('.json', '')}")
            else:
                print("No hay etiquetas aun")
            
            print("N. Crear nueva etiqueta")
            print("0. Volver al menu principal")
            
            eleccion = input("Elige una etiqueta (numero, 'N' o '0'): ").strip()

            if eleccion == "0":
                continue
            elif eleccion.lower() == 'n':
                nombre_archivo = input("Nombre de nueva etiqueta: ").strip() + ".json"
            else:
                try:
                    nombre_archivo = etiquetas[int(eleccion)-1]
                except:
                    print("Opcion invalida.")
                    continue

            datos = crear_datos()
            if datos is not None:
                guardar_datos_en_json(nombre_archivo, datos)

        elif opcion == "2":
            etiquetas = mostrar_etiquetas()
            if not etiquetas:
                print("No hay etiquetas disponibles.")
                continue
            
            print("\nEtiquetas disponibles:")
            for i, et in enumerate(etiquetas, 1):
                print(f"{i}. {et.replace('.json', '')}")
            print("T. Ver todas")
            print("0. Volver al menu principal")

            eleccion = input("Selecciona una etiqueta o 'T': ").strip()
            if eleccion == "0":
                continue
            elif eleccion.lower() == 't':
                crear_tabla_combinada()
            else:
                try:
                    archivo = etiquetas[int(eleccion)-1]
                    crear_tabla_combinada(filtro=archivo)
                except:
                    print("Opcion invalida.")
                    continue

        elif opcion == "3":
            while True:
                print("\nMODIFICAR DATOS:")
                print("1. Modificar etiqueta")
                print("2. Modificar el contenido de la etiqueta")
                print("0. Volver al menu principal")
                
                sub_opcion = input("Selecciona una opcion (0-2): ")
                
                if sub_opcion == "0":
                    break
                elif sub_opcion == "1":
                    modificar_etiqueta()
                elif sub_opcion == "2":
                    modificar_contenido_etiqueta()
                else:
                    print("Opcion no valida, intenta de nuevo.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")


if __name__ == "__main__":
    main()