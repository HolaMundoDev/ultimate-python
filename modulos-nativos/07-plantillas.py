from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path

plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")
template = Template(plantilla)
# cuerpo = template.substitute({"usuario": "Chanchito Feliz"})
cuerpo = template.substitute(usuario="Chanchito Triste")

path = Path("modulos-nativos/holamundo.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "ultimatepython@holamundo.io"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("ultimatepython@holamundo.io", "holamundo123")
    smtp.send_message(mensaje)
    print("Mensaje enviado")