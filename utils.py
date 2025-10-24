import json
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')
    # os.name == 'nt' verifica si el sistema operativo es Windows
    # Si es Windows ('nt'), usa 'cls', de lo contrario usa 'clear' (Linux/Mac)

def mostrar_banner(titulo):
    """Muestra un banner con bordes decorativos"""
    print("\n" + "=" * 60)  # Línea superior de 60 caracteres "="
    print(f" {titulo:^58} ")  # Centra el título en 58 espacios para dejar bordes
    print("=" * 60)  # Línea inferior de 60 caracteres "="

def mostrar_subtitulo(subtitulo):
    """Muestra un subtitulo con formato"""
    print(f"\n {subtitulo}")  # Imprime el subtítulo con un salto de línea
    print("-" * 50)  # Línea separadora de 50 caracteres "-"

def mostrar_etiquetas():
    """Devuelve una lista de nombres de etiquetas (sin .json) ordenadas alfabeticamente."""
    # os.listdir() obtiene todos los archivos en el directorio actual
    archivos = [f for f in os.listdir() if f.endswith('.json')]
    # Filtra solo los archivos que terminan con .json
    
    # Remueve la extensión .json de cada nombre de archivo
    etiquetas = [archivo.replace('.json', '') for archivo in archivos]
    
    etiquetas.sort()  # Ordena alfabéticamente la lista de etiquetas
    return etiquetas  # Retorna la lista ordenada

def guardar_cambios(nombre_archivo, datos):
    """Guarda los cambios en el archivo JSON."""
    try:
        # Abre el archivo en modo escritura con codificación UTF-8
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            # Verifica si hay solo un elemento en los datos
            if len(datos) == 1:
                # Si hay un solo elemento, lo guarda como objeto JSON individual
                # (sin corchetes de array)
                json.dump(datos[0], f, indent=4, ensure_ascii=False)
            else:
                # Si hay múltiples elementos, los guarda como array JSON
                json.dump(datos, f, indent=4, ensure_ascii=False)
                # Parámetros de json.dump:
                # - indent=4: formato legible con indentación de 4 espacios
                # - ensure_ascii=False: permite caracteres no ASCII (tildes, ñ, etc.)
                
    except Exception as e:
        # Captura cualquier error durante el proceso de guardado
        print(f"Error al guardar cambios: {e}")