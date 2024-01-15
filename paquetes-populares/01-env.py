# Varibles de entorno

import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

email = os.environ.get("SENDGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Correo de Pureba",
    html_content="Curso de <b>Ultimate Python<b/>"
)

try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers
    )
except Exception as e:
    print(e)

