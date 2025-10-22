    # send_email.py (modo prueba)

def enviar_notificacion(destinatario, nombre, modo="console"):
    """
    Envía un correo de bienvenida al nuevo contacto.
    Modo:
        - "console": solo imprime el correo en consola (modo prueba)
    """
    asunto = "👋 ¡Bienvenido al sistema de contactos!"
    mensaje = f"""
Hola {nombre},

Te damos la bienvenida al sistema de contactos.
Tu información ha sido registrada correctamente en nuestra base de datos.

¡Gracias por unirte!

-- Equipo de Contactos
"""

    if modo == "console":
        print("\n=== EMAIL SIMULADO (modo prueba) ===")
        print(f"Para: {destinatario}")
        print(f"Asunto: {asunto}")
        print(mensaje)
        print("==================================\n")
        return True
    else:
        # Aquí podrías agregar modo SMTP real si quieres más adelante
        print("Modo de envío no implementado.")
        return False
