import os
from utils import limpiar_pantalla, mostrar_banner
from etiquetas_json import gestionar_etiquetas
from poner_datos_json import poner_datos_json
from visualizar import visualizar_datos
from modificar import gestionar_modificar
from eliminar import gestionar_eliminar

def main():
    """Funcion principal del programa"""
    while True:  # Bucle infinito para mantener el programa ejecutándose
        # 1. Limpiar pantalla al inicio de cada iteración del menú
        limpiar_pantalla()
        
        # 2. Mostrar menú principal con banner decorativo
        mostrar_banner("GESTOR DE DATOS JSON CON ETIQUETAS")
        print("   1. Gestion de etiquetas JSON")      # Crear/administrar etiquetas
        print("   2. Agregar datos a una etiqueta")   # Añadir nuevos registros
        print("   3. Ver datos por etiqueta o todos") # Consultar y visualizar datos
        print("   4. Modificar datos")                # Editar registros existentes
        print("   5. Eliminar datos")                 # Borrar registros o etiquetas
        print("   6. Salir")                          # Terminar el programa

        # 3. Obtener y procesar la opción del usuario
        opcion = input("\nSelecciona una opcion (1-6): ").strip()  # strip() elimina espacios en blanco

        # 4. Ejecutar la funcionalidad correspondiente según la opción seleccionada
        if opcion == "1":
            # Gestión de etiquetas: crear nuevas etiquetas JSON
            gestionar_etiquetas()  # Llama al módulo que maneja la creación de etiquetas

        elif opcion == "2":
            # Agregar datos: permite ingresar nuevos registros en una etiqueta existente
            poner_datos_json()     # Llama al módulo para añadir datos a las etiquetas
            input("\nPresiona Enter para continuar...")  # Pausa después de completar la operación

        elif opcion == "3":
            # Visualizar datos: consulta y muestra los datos almacenados
            visualizar_datos()     # Llama al módulo de visualización (probablemente incluye búsqueda)
            input("\nPresiona Enter para continuar...")  # Pausa para que el usuario vea los resultados

        elif opcion == "4":
            # Modificar datos: permite editar registros existentes
            gestionar_modificar()  # Llama al módulo de modificación de datos

        elif opcion == "5":
            # Eliminar datos: borra registros específicos o etiquetas completas
            gestionar_eliminar()   # Llama al módulo de eliminación

        elif opcion == "6":
            # Salir del programa: opción para terminar la ejecución
            mostrar_banner("SALIENDO DEL PROGRAMA")  # Mensaje de despedida con formato
            print("Hasta pronto!")                   # Mensaje amigable de despedida
            break  # Rompe el bucle while True, terminando el programa

        else:
            # Manejar opciones inválidas (fuera del rango 1-6)
            print("Opcion no valida, intenta de nuevo.")  # Mensaje de error
            input("\nPresiona Enter para continuar...")   # Pausa antes de mostrar el menú nuevamente


if __name__ == "__main__":
    # Punto de entrada del programa - solo se ejecuta cuando el script se ejecuta directamente
    main()  # Inicia la función principal del programa