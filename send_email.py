# send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_notificacion(destinatario, nombre):
    """
    Envía un correo de bienvenida al nuevo contacto.
    Usa Gmail con contraseña de aplicación (no la contraseña normal).
    """
    # 💡 CONFIGURA TUS DATOS AQUÍ
    remitente = "TU_CORREO@gmail.com"  # <-- pon aquí tu correo de Gmail
    password = "TU_CONTRASEÑA_DE_APLICACION"  # <-- pon aquí tu contraseña de aplicación de Gmail

    # Asunto y cuerpo del mensaje
    asunto = "👋 ¡Bienvenido al sistema de contactos!"
    mensaje = f"""
    Hola {nombre},

    Te damos la bienvenida al sistema de contactos.
    Tu información ha sido registrada correctamente en nuestra base de datos.

    ¡Gracias por unirte!

    -- Equipo de Contactos
    """

    # Crear mensaje MIME
    msg = MIMEMultipart()
    msg["From"] = remitente
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(mensaje, "plain"))

    try:
        # Conectarse al servidor SMTP de Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # seguridad TLS
            server.login(remitente, password)
            server.send_message(msg)

        print(f"✅ Correo enviado correctamente a {destinatario}")
        return True

    except Exception as e:
        print("⚠️ Error al enviar el correo:", e)
        return False
