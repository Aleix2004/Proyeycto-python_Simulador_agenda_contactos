<details>
  <summary>📖 Introducción y descripción del proyecto.</summary>
  
# 📇 SISTEMA DE GESTIÓN DE CONTACTOS

## 🚀 INTRODUCCIÓN

  El Sistema de Gestión de Contactos es una aplicación modular desarrollada en Python que permite administrar de manera eficiente una agenda de contactos personal o empresarial. Este proyecto destaca por su arquitectura escalable, persistencia de datos y sistema de categorización mediante etiquetas, ofreciendo una solución completa para la organización de información de contacto.

<br>

## Propósito del Sistema
Desarrollar una herramienta intuitiva y robusta que simplifique la gestión de contactos, permitiendo no solo el almacenamiento básico sino también la categorización avanzada, búsqueda eficiente y operaciones CRUD completas, todo ello con una interfaz de usuario amigable por consola.

<br>
<br>

# 📋 DESCRIPCIÓN DEL PROYECTO

🎯 Objetivos Principales

* **Centralización:** Unificar la información de contactos en una base de datos estructurada
* **Categorización:** Implementar un sistema flexible de etiquetas para organizar contactos
* **Accesibilidad:** Proporcionar operaciones rápidas de búsqueda, filtrado y modificación
* **Persistencia:** Garantizar la seguridad y permanencia de los datos mediante almacenamiento JSON
* **Escalabilidad:** Diseñar una arquitectura modular que permita futuras expansiones


<br>
<br>


## ✨ Características Principales

Módulos del Sistema

* **main.py** - Núcleo y coordinador general
* **AC_json_2.py** - Gestor de persistencia JSON
* **a_c_1.py** - Operaciones básicas de contactos
* **show_list.py** - Visualización y búsqueda
* **Delete_contact.py** - Eliminación segura
* **AC_05.py** - Modificación de datos
* **AC_06_Tag_Contacts.py** - Sistema de etiquetas
* **send_email.py** - Notificaciones (simuladas)
* **utils.py** - Utilidades compartidas

<br>

1. Gestión Completa de Contactos
   
✅ Crear nuevos contactos con validación de campos obligatorios

✅ Visualizar lista completa ordenada alfabéticamente

✅ Modificar información existente de manera intuitiva

✅ Eliminar contactos con confirmación visual

✅ Búsqueda y filtrado por múltiples criterios

<br>

2. Sistema Avanzado de Etiquetas
🏷️ Crear etiquetas personalizadas como categorías

🏷️ Asignar múltiples etiquetas a un mismo contacto

🏷️ Visualizar contactos agrupados por etiquetas

🏷️ Renombrar y reorganizar etiquetas existentes

<br>

3. Persistencia de Datos
💾 Almacenamiento en formato JSON para portabilidad

💾 Sincronización automática entre memoria y archivos

💾 Backup implícito mediante archivos de texto legibles

💾 Recuperación de datos ante reinicios del sistema

<br>

4. Experiencia de Usuario

👨‍💻 Interfaz de consola limpia y organizada

👨‍💻 Navegación intuitiva con menús jerárquicos

👨‍💻 Feedback visual inmediato de todas las operaciones

👨‍💻 Manejo robusto de errores y entradas inválidas

</details>

<br>
<br>
<br>

<details>
  <summary>🎨 Diseño de la solución</summary>

  El flujo de datos describe cómo la información viaja a través del sistema, desde que el usuario realiza una acción hasta que se persiste en almacenamiento y se muestra la respuesta. Es el "sistema circulatorio" de la aplicación.

<img width="3500" height="2290" alt="deepseek_mermaid_20251024_b2c935" src="https://github.com/user-attachments/assets/fb648400-e059-4366-9437-f8a159ba014d" />

</details>


<br>
<br>
<br>


<details>
  <summary>📱 Capturas de pantalla y ejemplos de ejecución</summary>

# Screen del menú principal

<img width="743" height="501" alt="image" src="https://github.com/user-attachments/assets/da89606f-8b66-46ee-87ac-58fde758cd39" />

En la captura se puede ver el menú desplegable que ofrece todas las opciones del proyecto enumeradas

1. Crear nuevo contacto (guardar en JSON) donde creas los contactos y se guarda directamente en el json.

2. Ver o filtrar contactos (desde JSON) donde ves el json y accedes a todos los contactos.

3. Borrar contactos del archivo JSON, básicamente borrás contactos accediendo al json.

4. Gestionar etiquetas JSON, Puedes crear, usar y asignar etiquetas como por ejemplo (familias.json, amigos.json)

5. Modificar contactos o etiquetas, por si te equivocas en al asignar un nombre


<br>

# JSON

<img width="643" height="501" alt="image" src="https://github.com/user-attachments/assets/38f9d43b-1d5f-4b87-a712-d24ff123e414" />

<br>

# ETIQUETAS

<img width="600" height="680" alt="image" src="https://github.com/user-attachments/assets/533883ed-afbd-416a-bdf8-6f6e5faafa3c" />

En esta screen puedes ver todas las etiquetas y que hay dentro de las etiquetas, para saber si un contacto está dentro de familia o amigos o etc.

<br>

## 4. Manual de instalación del proyecto

### Requisitos previos

Antes de instalar y ejecutar el proyecto, es necesario disponer de los siguientes elementos:

- Sistema operativo: Windows 10 o superior (también compatible con macOS o Linux).  
- Python: versión 3.12.x (es la versión utilizada durante el desarrollo del proyecto).  
- Git: para clonar el repositorio desde GitHub.  
- Editor de código recomendado: Visual Studio Code o cualquier entorno compatible con Python.

---

### Instalación de Python

1. Descargar Python desde la página oficial:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Durante el proceso de instalación:
   - Marcar la casilla “Add Python to PATH”.  
   - Seleccionar la opción de instalación recomendada.  
3. Una vez finalizada la instalación, comprobar que Python se haya instalado correctamente ejecutando el siguiente comando en la terminal o PowerShell:

   ```
   bash
   python --version
   ```

## Clonación del repositorio

Para obtener el proyecto desde GitHub, se debe clonar el repositorio mediante Git.

Abrir la terminal o PowerShell y ejecutar el siguiente comando:

 ```git clone https://github.com/Aleix2004/Proyeycto-python_Simulador_agenda_contactos.git```

Acceder a la carpeta del proyecto con:

 ```cd Proyeycto-python_Simulador_agenda_contactos```

<br>

## Instalación de dependencias

El proyecto no requiere librerías externas adicionales. Sin embargo, se recomienda actualizar el gestor de paquetes pip a su última versión ejecutando:

```pip install --upgrade pip```

<br>

## Ejecución del programa

Para iniciar el sistema, se debe ejecutar el archivo principal del proyecto:

```python main.py```

Una vez iniciado, aparecerá en pantalla el menú principal del sistema de gestión de contactos.

<img width="744" height="538" alt="image" src="https://github.com/user-attachments/assets/7f19f3bc-da80-4407-a7bd-bff041059145" />

</details>



<br>
<br>
<br>


<details>
  <summary>📌 CONCLUSIONES Y DIFICULTADES</summary>

# 📌 CONCLUSIONES Y DIFICULTADES

## ✅ CONCLUSIONES

<br>

### Logros Alcanzados

* Se desarrolló un sistema completo y funcional de gestión de contactos con arquitectura modular.
* Se implementó con éxito un sistema de etiquetas flexible que permite categorización múltiple.
* La persistencia de datos en JSON garantiza portabilidad y recuperación de información.
* La interfaz de usuario resulta intuitiva y accesible incluso para usuarios no técnicos.
* El sistema demuestra escalabilidad, permitiendo añadir nuevas funcionalidades fácilmente.

<br>

### Valor del Proyecto

* Soluciona un problema real de organización de información personal y profesional.
* Combina simplicidad de uso con capacidades técnicas avanzadas.
* Sirve como base sólida para futuras expansiones y mejoras.
* Demuestra buenas prácticas de programación y diseño modular.

<br>
<br>



## 🚧 DIFICULTADES ENCONTRADAS

### Coordinación entre Módulos

* Mantener la sincronización entre la memoria y los archivos JSON requirió atención constante.
* Gestionar las dependencias entre los diferentes archivos del sistema representó un desafío.
* Garantizar que todos los módulos accedieran a la versión más actualizada de los datos.

<br>

### Manejo de Errores

* Implementar validaciones robustas para entradas de usuario inesperadas.
* Manejar casos edge como archivos JSON corruptos o vacíos.
* Prevenir pérdida de datos durante operaciones de modificación o eliminación.

<br>

### Experiencia de Usuario

* Diseñar una navegación intuitiva entre múltiples menús y submenús.
* Balancear funcionalidad avanzada con simplicidad de uso.
* Proporcionar feedback claro al usuario en todas las operaciones.

<br>

### Arquitectura de Datos

* Diseñar un sistema de etiquetas que no duplicara información innecesariamente.
* Mantener la integridad referencial entre contactos principales y etiquetas.
* Optimizar el rendimiento al crecer la cantidad de contactos y etiquetas.

<br>

### Persistencia y Recuperación

* Garantizar que los datos sobrevivieran reinicios del programa sin corrupción.
* Manejar adecuadamente la carga inicial cuando no existían archivos previos.
* Implementar backup implícito mediante el formato JSON legible.

</details>




























