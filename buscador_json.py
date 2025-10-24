import json
import os
from utils import limpiar_pantalla, mostrar_banner

def buscar_en_datos(datos, termino_busqueda, campo_busqueda):
    """Busca el término en el campo específico de los datos."""
    resultados = []
    termino = termino_busqueda.lower()  # Convertir a minúsculas para búsqueda case-insensitive
    
    for item in datos:
        if campo_busqueda == "todos":
            # Buscar en todos los campos posibles del diccionario
            if (termino in item.get('nombre', '').lower() or
                termino in item.get('apellido', '').lower() or
                termino in item.get('correo', '').lower() or
                termino in item.get('telefono', '').lower()):
                resultados.append(item)  # Agregar item a resultados si coincide en cualquier campo
        else:
            # Buscar en un campo específico
            valor_campo = item.get(campo_busqueda, '').lower()  # Obtener valor del campo y convertir a minúsculas
            if termino in valor_campo:
                resultados.append(item)  # Agregar item a resultados si coincide en el campo específico
    
    return resultados

def seleccionar_campo_busqueda():
    """Muestra menú para seleccionar el campo de búsqueda."""
    limpiar_pantalla()  # Limpiar la pantalla de la terminal
    mostrar_banner("SELECCIONAR CAMPO DE BÚSQUEDA")  # Mostrar título con formato
    print("   1. Buscar en Nombre")
    print("   2. Buscar en Apellido")
    print("   3. Buscar en Correo")
    print("   4. Buscar en Teléfono")
    print("   5. Buscar en Todos los campos")
    print("   0. Volver al menú anterior")
    
    opcion = input("\nSelecciona una opción (0-5): ").strip()  # Obtener entrada del usuario y quitar espacios
    
    # Mapeo de opciones numéricas a nombres de campos reales
    mapeo_campos = {
        "1": "nombre",
        "2": "apellido", 
        "3": "correo",
        "4": "telefono",
        "5": "todos"
    }
    
    if opcion == "0":
        return None  # Salir si el usuario elige volver
    elif opcion in mapeo_campos:
        return mapeo_campos[opcion]  # Devolver el nombre del campo correspondiente
    else:
        print("Opción no válida.")  # Manejar entrada inválida
        input("\nPresiona Enter para continuar...")
        return None

def buscar_en_etiqueta(archivo_etiqueta, crear_tabla_func):
    """Función para buscar dentro de una etiqueta específica manteniendo índices originales."""
    # Primero seleccionar el campo de búsqueda
    campo_busqueda = seleccionar_campo_busqueda()
    if campo_busqueda is None:  # Si el usuario canceló la búsqueda
        return
    
    limpiar_pantalla()  # Limpiar pantalla para la búsqueda
    
    # Diccionario para mostrar títulos descriptivos según el campo seleccionado
    titulo_campo = {
        "nombre": "NOMBRE",
        "apellido": "APELLIDO", 
        "correo": "CORREO",
        "telefono": "TELÉFONO",
        "todos": "TODOS LOS CAMPOS"
    }
    
    mostrar_banner(f"BUSCAR EN {titulo_campo[campo_busqueda]}")
    print(f"Etiqueta: {archivo_etiqueta.replace('.json', '')}")  # Mostrar nombre de etiqueta sin extensión
    print("=" * 60)  # Línea separadora
    
    # Cargar todos los datos de la etiqueta ORDENADOS alfabéticamente
    datos_completos_ordenados = cargar_datos_etiqueta_ordenados(archivo_etiqueta)
    if not datos_completos_ordenados:  # Verificar si hay datos disponibles
        print("No hay datos en esta etiqueta para buscar.")
        input("\nPresiona Enter para continuar...")
        return
    
    termino_busqueda = input("Ingresa el término a buscar: ").strip()  # Obtener término de búsqueda
    
    if not termino_busqueda:  # Validar que se ingresó un término
        print("No ingresaste ningún término para buscar.")
        input("\nPresiona Enter para continuar...")
        return
    
    # Realizar la búsqueda en el campo específico usando la función auxiliar
    resultados = buscar_en_datos(datos_completos_ordenados, termino_busqueda, campo_busqueda)
    
    limpiar_pantalla()  # Limpiar pantalla para mostrar resultados
    
    if resultados:  # Si se encontraron resultados
        # Mostrar encabezado según el tipo de búsqueda
        if campo_busqueda == "todos":
            mostrar_banner(f"RESULTADOS: '{termino_busqueda}' en todos los campos")
        else:
            mostrar_banner(f"RESULTADOS: '{termino_busqueda}' en {campo_busqueda}")
        
        print(f"Se encontraron {len(resultados)} resultado(s)")  # Mostrar cantidad de resultados
        print("=" * 60)
        
        # Usar la función de crear tabla del módulo visualizar para mostrar resultados formateados
        crear_tabla_func(resultados)
        
    else:  # Si no se encontraron resultados
        mostrar_banner("BÚSQUEDA SIN RESULTADOS")
        if campo_busqueda == "todos":
            print(f"No se encontraron resultados para: '{termino_busqueda}' en ningún campo")
        else:
            print(f"No se encontraron resultados para: '{termino_busqueda}' en {campo_busqueda}")
        print("=" * 60)
    
    input("\nPresiona Enter para continuar...")  # Pausa para que el usuario vea los resultados

def cargar_datos_etiqueta_ordenados(archivo_etiqueta):
    """Carga los datos de una etiqueta específica y los ordena alfabéticamente."""
    try:
        # Abrir y leer el archivo JSON con codificación UTF-8 para caracteres especiales
        with open(archivo_etiqueta, "r", encoding="utf-8") as f:
            datos = json.load(f)  # Cargar datos desde el archivo JSON
        
        # Normalizar datos a lista (manejar diferentes formatos de entrada)
        if isinstance(datos, dict):  # Si es un solo diccionario
            datos = [datos]  # Convertir a lista con un elemento
        elif not isinstance(datos, list):  # Si no es lista ni diccionario
            datos = []  # Inicializar como lista vacía
        
        # ORDENAR LOS DATOS POR NOMBRE (A-Z) antes de asignar índices
        # key=lambda x: crea una función temporal que extrae el nombre de cada elemento
        datos_ordenados = sorted(datos, key=lambda x: x.get('nombre', '').lower())
        
        # Agregar información de archivo e índice ORDENADO a cada elemento
        for i, item in enumerate(datos_ordenados):
            if isinstance(item, dict):  # Verificar que sea un diccionario válido
                item['_archivo'] = archivo_etiqueta.replace('.json', '')  # Guardar nombre del archivo sin extensión
                item['_indice'] = i  # Índice según orden alfabético (no el original)
        
        return datos_ordenados  # Devolver datos ordenados y enriquecidos
        
    except Exception as e:
        # Manejar errores de lectura del archivo
        print(f"Error al cargar datos: {e}")
        return []  # Devolver lista vacía en caso de error

if __name__ == "__main__":
    # Código que solo se ejecuta cuando el archivo se ejecuta directamente (no cuando se importa)
    print("Módulo de búsqueda - Debe ser importado desde visualizar.py")