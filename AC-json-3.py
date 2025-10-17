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
                        todos_los_datos.append(item)
            elif isinstance(datos, dict):
                datos['_archivo'] = archivo.replace('.json', '')
                todos_los_datos.append(datos)
                
        except json.JSONDecodeError:
            print(f"Error leyendo {archivo} - archivo corrupto")
        except Exception as e:
            print(f"Error leyendo {archivo}: {e}")
    
    if not todos_los_datos:
        print("No se encontraron datos para mostrar.")
        return
    
    _crear_tabla_diccionarios(todos_los_datos)


def _crear_tabla_diccionarios(datos):
    """Crea tabla formateada para lista de diccionarios."""
    if not datos:
        return
    
    # === Orden de columnas deseado ===
    claves = set()
    for item in datos:
        claves.update(item.keys())

    orden_deseado = ["_archivo", "nombre", "apellido", "correo", "telefono"]
    claves = [c for c in orden_deseado if c in claves] + [c for c in sorted(claves) if c not in orden_deseado]
    
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
    nombre = input("* Nombre: ")
    apellido = input("* Apellido: ")
    telefono = input("* Teléfono: ")
    correo = input("* Correo: ")

    return {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
    }

# ==============================
# MENÚ PRINCIPAL
# ==============================

def mostrar_etiquetas():
    """Devuelve una lista de archivos JSON (etiquetas)."""
    etiquetas = [f for f in os.listdir() if f.endswith('.json')]
    return etiquetas


def main():
    print("=== GESTOR DE DATOS JSON CON ETIQUETAS ===")
    
    while True:
        print("\nOpciones:")
        print("1. Agregar datos a una etiqueta (JSON)")
        print("2. Ver datos por etiqueta o todos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            etiquetas = mostrar_etiquetas()
            print("\nEtiquetas existentes:")
            if etiquetas:
                for i, et in enumerate(etiquetas, 1):
                    print(f"{i}. {et.replace('.json', '')}")
            else:
                print("— No hay etiquetas aún —")
            
            print("N. Crear nueva etiqueta")
            eleccion = input("Elige una etiqueta (número o 'N'): ").strip()

            if eleccion.lower() == 'n':
                nombre_archivo = input("Nombre de nueva etiqueta: ").strip() + ".json"
            else:
                try:
                    nombre_archivo = etiquetas[int(eleccion)-1]
                except:
                    print("Opción inválida.")
                    continue

            datos = crear_datos()
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

            eleccion = input("Selecciona una etiqueta o 'T': ").strip()
            if eleccion.lower() == 't':
                crear_tabla_combinada()
            else:
                try:
                    archivo = etiquetas[int(eleccion)-1]
                    crear_tabla_combinada(filtro=archivo)
                except:
                    print("Opción inválida.")
                    continue

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
