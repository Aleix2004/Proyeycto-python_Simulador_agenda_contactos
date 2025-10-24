import json
import os
from utils import limpiar_pantalla, mostrar_banner, mostrar_etiquetas
from buscador_json import buscar_en_etiqueta

def menu_visualizacion_etiqueta(archivo_etiqueta):
    """Menu específico para visualizar una etiqueta con opciones de búsqueda."""
    while True:  # Bucle infinito para mantener el menú activo
        limpiar_pantalla()
        mostrar_banner(f"VISUALIZANDO: {archivo_etiqueta.replace('.json', '')}")
        print("   1. Ver todos los registros")  # Mostrar todos los datos de la etiqueta
        print("   2. Buscar en la etiqueta")    # Buscar registros específicos
        print("   0. Volver al menú anterior")  # Salir del menú actual
        
        opcion = input("\nSelecciona una opción (0-2): ").strip()
        
        if opcion == "0":
            break  # Salir del bucle y volver al menú anterior
        elif opcion == "1":
            # Ver todos los registros de la etiqueta
            datos = crear_tabla_combinada(filtro=archivo_etiqueta)
            if datos:
                input("\nPresiona Enter para continuar...")  # Pausa para ver resultados
        elif opcion == "2":
            # Buscar en la etiqueta usando el módulo buscador
            buscar_en_etiqueta(archivo_etiqueta, _crear_tabla_diccionarios)
        else:
            print("Opción no válida.")
            input("\nPresiona Enter para continuar...")

def cargar_datos_etiqueta(archivo_etiqueta):
    """Carga los datos de una etiqueta específica."""
    try:
        # Abrir y leer el archivo JSON
        with open(archivo_etiqueta, "r", encoding="utf-8") as f:
            datos = json.load(f)  # Cargar datos desde el archivo JSON
        
        # Normalizar datos a lista (manejar diferentes formatos)
        if isinstance(datos, dict):  # Si es un solo diccionario
            datos = [datos]  # Convertir a lista con un elemento
        elif not isinstance(datos, list):  # Si no es lista ni diccionario
            datos = []  # Inicializar como lista vacía
        
        # ORDENAR LOS DATOS POR NOMBRE (A-Z) alfabéticamente
        # key=lambda x: crea función temporal que extrae el nombre en minúsculas
        datos_ordenados = sorted(datos, key=lambda x: x.get('nombre', '').lower())
        
        # Agregar información de archivo e índice a cada elemento
        for i, item in enumerate(datos_ordenados):
            if isinstance(item, dict):  # Verificar que sea un diccionario válido
                item['_archivo'] = archivo_etiqueta.replace('.json', '')  # Nombre sin extensión
                item['_indice'] = i  # Índice según orden alfabético
        
        return datos_ordenados  # Retornar datos ordenados y enriquecidos
        
    except Exception as e:
        # Manejar errores de lectura del archivo
        print(f"Error al cargar datos: {e}")
        return []  # Retornar lista vacía en caso de error

def crear_tabla_combinada(filtro=None):
    """Crea una tabla con los datos de todos o de un archivo JSON específico."""
    # Obtener todos los archivos JSON en el directorio actual
    archivos_json = [archivo for archivo in os.listdir() if archivo.endswith('.json')]
    
    # Verificar si hay archivos JSON disponibles
    if not archivos_json:
        mostrar_banner("INFORMACION")
        print(" No hay archivos JSON (etiquetas) en el directorio actual. ")
        print("=" * 60)
        return  # Salir si no hay archivos
    
    todos_los_datos = []  # Lista para acumular todos los datos
    
    # Procesar cada archivo JSON
    for archivo in archivos_json:
        # Si hay filtro y el archivo no coincide, saltar a la siguiente iteración
        if filtro and archivo != filtro:
            continue
        
        try:
            # Leer y procesar cada archivo JSON
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)  # Cargar datos del archivo
                
            # Normaliza datos según el formato encontrado
            if isinstance(datos, list):  # Si es una lista de diccionarios
                for item in datos:
                    if isinstance(item, dict):
                        item['_archivo'] = archivo.replace('.json', '')  # Agregar nombre de archivo
                        # El índice se asignará después del ordenamiento general
                        todos_los_datos.append(item)
            elif isinstance(datos, dict):  # Si es un solo diccionario
                datos['_archivo'] = archivo.replace('.json', '')  # Agregar nombre de archivo
                # El índice se asignará después del ordenamiento general
                todos_los_datos.append(datos)
                
        except json.JSONDecodeError:
            # Manejar archivos JSON corruptos
            print(f"Error leyendo {archivo} - archivo corrupto")
        except Exception as e:
            # Manejar otros errores de lectura
            print(f"Error leyendo {archivo}: {e}")
    
    # Verificar si se encontraron datos
    if not todos_los_datos:
        mostrar_banner("INFORMACION")
        print(" No se encontraron datos para mostrar. ")
        print("=" * 60)
        return
    
    # ORDENAR TODOS LOS DATOS POR NOMBRE (A-Z) alfabéticamente
    todos_los_datos_ordenados = sorted(todos_los_datos, key=lambda x: x.get('nombre', '').lower())
    
    # Actualizar índices después del ordenamiento general
    for i, item in enumerate(todos_los_datos_ordenados):
        item['_indice'] = i  # Asignar índice global ordenado
    
    # Crear y mostrar la tabla con los datos ordenados
    return _crear_tabla_diccionarios(todos_los_datos_ordenados)

def _crear_tabla_diccionarios(datos):
    """Crea tabla formateada para lista de diccionarios."""
    if not datos:  # Verificar si hay datos para mostrar
        return None
    
    # Identificar todas las claves únicas presentes en los datos
    claves = set()  # Conjunto para claves únicas
    for item in datos:
        claves.update(item.keys())  # Agregar todas las claves de cada item

    # Excluir campos internos de la visualización
    campos_internos = {'_archivo'}  # Solo _archivo es interno ahora
    # Orden deseado para las columnas
    orden_deseado = ["_indice", "_archivo", "nombre", "apellido", "correo", "telefono"]
    # Ordenar claves: primero las del orden deseado, luego las restantes alfabéticamente
    claves = [c for c in orden_deseado if c in claves] + [c for c in sorted(claves) if c not in orden_deseado and c not in campos_internos]
    
    # Calcular anchos de columna basados en el contenido más largo
    anchos = {clave: len(str(clave)) for clave in claves}  # Inicializar con ancho del encabezado
    for item in datos:
        for clave in claves:
            if clave == "_indice":
                # Para _indice, mostrar número + 1 (para evitar el 0)
                valor = str(item.get(clave, 0) + 1)
            else:
                valor = str(item.get(clave, ''))  # Convertir valor a string
            anchos[clave] = max(anchos[clave], len(valor))  # Actualizar ancho máximo
    
    # Crear separador de tabla
    separador = "+"
    for clave in claves:
        separador += "-" * (anchos[clave] + 2) + "+"  # +2 por los espacios alrededor
    
    # Construir la tabla línea por línea
    tabla = [separador]  # Iniciar con separador superior
    
    # Crear fila de encabezados
    fila_encabezados = "|"
    for clave in claves:
        if clave == "_indice":
            fila_encabezados += f" {'#':<{anchos[clave]}} |"  # Mostrar '#' en lugar de '_INDICE'
        elif clave not in ['_archivo']:  # Campos normales
            fila_encabezados += f" {clave.upper():<{anchos[clave]}} |"  # Alineación izquierda
        else:
            fila_encabezados += f" {clave.upper():<{anchos[clave]}} |"  # Campos internos también
    tabla.append(fila_encabezados)
    tabla.append(separador)  # Separador después de encabezados
    
    # Crear filas de datos
    for item in datos:
        fila = "|"
        for clave in claves:
            if clave == "_indice":
                # Sumar 1 al índice para evitar el 0
                valor = str(item.get(clave, 0) + 1)
            else:
                valor = str(item.get(clave, ''))  # Obtener valor como string
            fila += f" {valor:<{anchos[clave]}} |"  # Alinear izquierda con padding
        tabla.append(fila)
    
    tabla.append(separador)  # Separador final
    
    # Mostrar la tabla
    if len(datos) == 1:
        mostrar_banner("REGISTRO ENCONTRADO")  # Título para un solo registro
    else:
        mostrar_banner("LISTA DE CONTACTOS")  # Título para múltiples registros
    
    print("\n".join(tabla))  # Unir todas las líneas de la tabla
    print(f"\nTotal de registros: {len(datos)}")  # Mostrar conteo total
    
    # Mostrar etiquetas únicas solo si hay más de una
    etiquetas_unicas = len(set(item.get('_archivo', '') for item in datos))
    if etiquetas_unicas > 1:
        print(f"Etiquetas mostradas: {etiquetas_unicas}")
    
    return datos  # Retornar datos para posible uso posterior

def visualizar_datos():
    """Función principal para visualizar datos"""
    limpiar_pantalla()
    etiquetas = mostrar_etiquetas()  # Obtener lista de etiquetas disponibles
    if not etiquetas:
        print("No hay etiquetas disponibles.")
        input("\nPresiona Enter para continuar...")
        return
    
    mostrar_banner("VER DATOS")
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):  # Enumerar desde 1
        print(f"   {i}. {et}")
    print("   T. Ver todas las etiquetas")  # Opción para ver todo
    print("   0. Volver al menu principal")  # Opción para salir

    eleccion = input("\nSelecciona una etiqueta o 'T': ").strip().lower()
    if eleccion == "0":
        return  # Volver al menú principal
    elif eleccion == 't':
        # Mostrar todas las etiquetas combinadas
        crear_tabla_combinada()
        input("\nPresiona Enter para continuar...")  # Pausa para ver resultados
    else:
        try:
            eleccion_num = int(eleccion)  # Convertir a número
            if eleccion_num < 1 or eleccion_num > len(etiquetas):
                print("Opción no válida.")
                input("\nPresiona Enter para continuar...")
            else:
                # Obtener la etiqueta seleccionada y abrir su menú específico
                etiqueta_nombre = etiquetas[eleccion_num-1]  # -1 por índice base 0
                archivo = etiqueta_nombre + ".json"  # Agregar extensión
                menu_visualizacion_etiqueta(archivo)  # Abrir menú de la etiqueta
        except ValueError:
            # Manejar entrada que no es número
            print("Opción no válida.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando el archivo se ejecuta directamente
    visualizar_datos()  # Iniciar la función principal de visualización