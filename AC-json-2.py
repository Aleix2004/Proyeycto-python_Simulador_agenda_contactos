import json
import os

def crear_tabla_combinada():
    """Crea una tabla con todos los datos de todos los archivos JSON."""
    archivos_json = [archivo for archivo in os.listdir() if archivo.endswith('.json')]
    
    if not archivos_json:
        print("No hay archivos JSON en el directorio actual.")
        return
    
    todos_los_datos = []
    
    # Leer todos los archivos JSON
    for archivo in archivos_json:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                
            # Procesar datos según su estructura
            if isinstance(datos, list):
                for item in datos:
                    if isinstance(item, dict):
                        item['_archivo'] = archivo  # Agregar nombre del archivo
                        todos_los_datos.append(item)
            elif isinstance(datos, dict):
                datos['_archivo'] = archivo
                todos_los_datos.append(datos)
                
        except json.JSONDecodeError:
            print(f"Error leyendo {archivo} - archivo corrupto")
        except Exception as e:
            print(f"Error leyendo {archivo}: {e}")
    
    if not todos_los_datos:
        print("No se encontraron datos en los archivos JSON.")
        return
    
    # Crear la tabla
    _crear_tabla_diccionarios(todos_los_datos)

def _crear_tabla_diccionarios(datos):
    """Crea tabla para lista de diccionarios."""
    if not datos:
        return
    
    # Obtener todas las claves únicas
    claves = set()
    for item in datos:
        claves.update(item.keys())
    claves = sorted(list(claves))
    
    # Calcular anchos de columnas
    anchos = {clave: len(str(clave)) for clave in claves}
    for item in datos:
        for clave in claves:
            valor = str(item.get(clave, ''))
            anchos[clave] = max(anchos[clave], len(valor))
    
    # Crear línea separadora
    separador = "+"
    for clave in claves:
        separador += "-" * (anchos[clave] + 2) + "+"
    
    # Construir tabla
    tabla = [separador]
    
    # Encabezados
    fila_encabezados = "|"
    for clave in claves:
        fila_encabezados += f" {clave:<{anchos[clave]}} |"
    tabla.append(fila_encabezados)
    tabla.append(separador)
    
    # Datos
    for item in datos:
        fila = "|"
        for clave in claves:
            valor = str(item.get(clave, ''))
            fila += f" {valor:<{anchos[clave]}} |"
        tabla.append(fila)
    
    tabla.append(separador)
    
    # Imprimir tabla
    print("\n" + "\n".join(tabla))
    print(f"\nTotal de registros: {len(datos)}")
    print(f"Archivos leídos: {len(set(item.get('_archivo', '') for item in datos))}")

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
    """Pide datos al usuario y los devuelve como diccionario."""
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")

    return {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }

def main():
    print("=== GESTOR DE DATOS JSON ===")
    while True:
        print("\nOpciones:")
        print("1. Agregar datos a un JSON")
        print("2. Ver todos los datos de todos los JSON")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            nombre_archivo = input("Nombre del archivo JSON (sin .json): ") + ".json"
            datos = crear_datos()
            guardar_datos_en_json(nombre_archivo, datos)

        elif opcion == "2":
            crear_tabla_combinada()

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    main()