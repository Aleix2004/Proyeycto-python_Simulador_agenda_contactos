import json
import os
from utils import limpiar_pantalla, mostrar_banner, mostrar_etiquetas, guardar_cambios
from visualizar import crear_tabla_combinada

def eliminar_etiqueta():
    """Permite eliminar una etiqueta completa."""
    limpiar_pantalla()  # Limpiar la pantalla
    mostrar_banner("ELIMINAR ETIQUETA")  # Mostrar título con formato
    
    # Obtener lista de etiquetas disponibles
    etiquetas = mostrar_etiquetas()
    if not etiquetas:  # Verificar si hay etiquetas
        print("No hay etiquetas disponibles.")
        input("\nPresiona Enter para continuar...")
        return
    
    # Mostrar menú de etiquetas disponibles
    print("Etiquetas disponibles:")
    for i, et in enumerate(etiquetas, 1):  # Enumerar desde 1
        print(f"   {i}. {et}")
    print("   0. Volver al menu principal")  # Opción para salir
    
    try:
        # Obtener selección del usuario
        eleccion = int(input("\nSelecciona la etiqueta a eliminar (numero): "))
        if eleccion == 0:  # Salir si elige 0
            return
        
        # Validar que la opción esté en rango válido
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Construir nombre del archivo con extensión .json
        archivo_eliminar = etiquetas[eleccion-1] + ".json"
        
        # Mostrar contenido de la etiqueta antes de eliminar (para confirmación)
        print(f"\nContenido de '{archivo_eliminar}':")
        crear_tabla_combinada(filtro=archivo_eliminar)  # Mostrar tabla con los datos
        
        # Pedir confirmación antes de eliminar
        confirmacion = input(f"\nEstas seguro de que quieres eliminar la etiqueta '{archivo_eliminar}'? (s/n): ").lower()
        if confirmacion == 's':  # Si confirma, eliminar archivo
            os.remove(archivo_eliminar)  # Eliminar archivo del sistema
            print(f"Etiqueta '{archivo_eliminar}' eliminada correctamente.")
        else:
            print("Eliminacion cancelada.")  # Si cancela, no hacer nada
        
        input("\nPresiona Enter para continuar...")  # Pausa para que usuario vea resultado
        
    except Exception as e:  # Manejar cualquier error
        print(f"Error al eliminar la etiqueta: {e}")
        input("\nPresiona Enter para continuar...")

def eliminar_datos_etiqueta():
    """Permite eliminar datos especificos de una etiqueta."""
    limpiar_pantalla()
    mostrar_banner("ELIMINAR DATOS DE ETIQUETA")
    
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
        eleccion = int(input("\nSelecciona la etiqueta (numero): "))
        if eleccion == 0:
            return
        
        if eleccion < 1 or eleccion > len(etiquetas):
            print("Opcion invalida.")
            input("\nPresiona Enter para continuar...")
            return
        
        # Construir nombre del archivo seleccionado
        archivo_seleccionado = etiquetas[eleccion-1] + ".json"
        
        # Mostrar contenido actual de la etiqueta
        print(f"\nContenido actual de '{archivo_seleccionado}':")
        datos_completos = crear_tabla_combinada(filtro=archivo_seleccionado)  # Obtener datos y mostrar tabla
        if not datos_completos:  # Si no hay datos, salir
            input("\nPresiona Enter para continuar...")
            return
        
        # Convertir índice mostrado a índice interno
        indice_mostrado = int(input("\nIngresa el numero de indice del registro a eliminar (o 0 para volver): "))
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
        
        # Mostrar detalles del registro seleccionado para confirmación
        limpiar_pantalla()
        mostrar_banner("REGISTRO SELECCIONADO PARA ELIMINAR")
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
                # Buscar coincidencia exacta en todos los campos
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
        
        # Pedir confirmación final antes de eliminar
        confirmacion = input("\nEstas seguro de que quieres eliminar este registro? (s/n): ").lower()
        if confirmacion == 's':
            # Proceder con la eliminación
            if len(datos_archivo) == 1:
                # Si era el único registro, eliminar el archivo completo
                os.remove(archivo_seleccionado)
                print(f"Registro eliminado y archivo '{archivo_seleccionado}' borrado por quedar vacio.")
            else:
                # Eliminar solo el registro específico de la lista
                datos_archivo.pop(indice_archivo)  # Remover elemento por índice
                guardar_cambios(archivo_seleccionado, datos_archivo)  # Guardar cambios en archivo
                print("Registro eliminado correctamente.")
        else:
            print("Eliminacion cancelada.")  # Usuario canceló la eliminación
        
        input("\nPresiona Enter para continuar...")  # Pausa final
        
    except Exception as e:  # Manejo de errores general
        print(f"Error al eliminar datos: {e}")
        input("\nPresiona Enter para continuar...")

def gestionar_eliminar():
    """Menu principal para eliminar"""
    while True:  # Bucle infinito hasta que usuario elija salir
        limpiar_pantalla()
        mostrar_banner("ELIMINAR DATOS")
        print("   1. Eliminar etiqueta completa")  # Eliminar archivo completo
        print("   2. Eliminar datos de etiqueta")  # Eliminar registro específico
        print("   0. Volver al menu principal")    # Salir del menú
        
        opcion = input("\nSelecciona una opcion (0-2): ").strip()  # Obtener opción
        
        if opcion == "0":
            break  # Salir del bucle y volver al menú principal
        elif opcion == "1":
            eliminar_etiqueta()  # Llamar función eliminar etiqueta completa
        elif opcion == "2":
            eliminar_datos_etiqueta()  # Llamar función eliminar registro específico
        else:
            print("Opcion no valida, intenta de nuevo.")  # Manejar opción inválida
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    # Código que se ejecuta solo cuando el archivo se ejecuta directamente
    gestionar_eliminar()  # Iniciar el menú de eliminación