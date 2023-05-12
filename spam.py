import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Datos del correo que se va a enviar
remitente = "ti@diagnomol.com"
password = "#D31.SIS19@"
destinatario = "avisoatodos@diagnomol.com"
#destinatario = "ebaltazar@diagnomol.com"
asunto = "Memorándum: Seguridad anti SPAM"
#cuerpo = "esto es una prueba"
cuerpo = """\
	<!DOCTYPE html>
<html>
<body style="font-family: Arial">
    <center><h3>Seguridad anti SPAM</h3></center>
    Buenos días a todos los colaboradores, los invitamos a seguir las recomendaciones para evitar la propagación de spam dentro de la red de correo electrónico de la organización.<br><br>
    Se solicita hacer caso omiso y eliminar el email. Recuerde que, por principios de seguridad de la información, en NINGUN CASO el administrador de correo electrónico o los sistemas de  información solicitará las credenciales de su cuenta de correo o datos personales.<br><br>
    A continuación, se enlistan las recomendaciones en caso de sospecha de SPAM en el correo electrónico institucional.<br>

<ul>
    <li>Verificar que las direcciones de email tengan la estructura correcta de un correo electrónico (ejemplo@ilustrativo.com).</li>
    <li>Nunca responda un correo electrónico que considere spam. Lo único que hará será confirmar que su email es válido y por consecuencia puede recibir aún más correo spam.</li>
    <li>No haga clic en ninguno de los enlaces de un correo electrónico que considere spam.</li>
    <li>No utilice su cuenta de correo electrónico para suscribirse a sitios web de dudosa reputación, de esta manera el sitio web publicitario no saturará su email.</li>
    <li>No descargue ningún tipo de documento que no haya solicitado con terminación (.pdf.exe, .doc, .zip, .rar, .bin, .class, .txt o .au3)</li>
    <b><li>En caso de sospecha de algún correo de spam, acudir al área de sistemas para su revisión.</li></b>
</ul>

    Les deseamos un excelente inicio de semana y les agradecemos su atención.

<br>
<br><br> <table style="border-collapse: collapse;padding: 0;margin: 0;">
            <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                <td style="padding: 0;margin: 0;vertical-align:middle;font-family:Arial,Helvetica,sans-serif;padding-right:0.5em;border-right:#77AD19 solid 2px;">
                    <img src="http://diagnomol.com/images/LogDiag.jpg" alt="" style="padding:0;margin:0;max-width:192px">
                </td>
                <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;padding-left:0.5em">
                    <table style="border-collapse: collapse;padding: 0;margin: 0;">
                        <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                            <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                <table style="border-collapse: collapse;padding: 0;margin: 0;">
                                    <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;font-size:100%;font-weight:bolder">
                                            Area de TI
                                        </td>
                                    </tr>
                                    <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#77AD19;font-family:Arial,Helvetica,sans-serif;font-size:90%;text-align:right;font-weight:bolder">
                                           Tecnolog&iacute;as de la informaci&oacute;n
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                            <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                <table style="border-collapse: collapse;padding: 0;margin: 0;">
                                    <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                            <img src="http://diagnomol.com/images/telephone.png" alt="" style="max-width:18pt;vertical-align:middle">
                                        </td>
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;font-size:60%">
                                            +(52) 55 5652 6925&nbsp;&nbsp;Ext. 2902<br>
                                            +(52) 55 5652 0307
                                        </td>
                                       <!-- <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                            <img src="http://diagnomol.com/images/iphone.png" alt="" style="max-width:18pt;vertical-align:middle">
                                        </td>
                                         <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;font-size:60%">-->
                                            
                                        </td>
                                    </tr>
                                    <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                            <img src="http://diagnomol.com/images/email.png" alt="" style="display:inline-table;max-width:18pt;vertical-align:middle">
                                        </td>
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                            <a href="mailto:ti@diagnomol.com" style="vertical-align:middle;font-size:60%;color:#016A4C;font-family:Arial,Helvetica,sans-serif;text-decoration:none">ti@diagnomol.com</a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                            <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                <table style="border-collapse: collapse;padding: 0;margin: 0;">
                                    <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                                            <img src="http://diagnomol.com/images/location.png" alt="" style="display:inline-table;width:18pt;vertical-align:middle">
                                        </td>
                                        <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;font-size:60%">
                                            Centro Comercial Pedregal del Lago, 3er Nivel L-22 Av. Camino a Santa Teresa<br>
                                            No. 13, Col. Pedregal del Lago C.P. 14110, Tlalpan, CDMX, M&eacute;xico.
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;text-align: right">
                <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;">
                </td>
                <td style="padding: 0;margin: 0;vertical-align:middle;color:#016A4C;font-family:Arial,Helvetica,sans-serif;font-size:40%;">
                    <img src="http://diagnomol.com/images/information.png" alt="Aviso" style="vertical-align:middle">
                    Consulte nuestro aviso de privacidad en <a href="http://diagnomol.com/PDFs/privacidad.pdf">Aviso de Privacidad</a>
                </td>
            </tr>
        </table>
    </body>
</html>
"""

# Datos del Servidor SMTP del correo
servidorSMTP = "mail.diagnomol.com"
puerto = 587

# Objeto mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['to'] = destinatario
mensaje['subject'] = asunto

# Cuerpo del mensaje
mensaje.attach(MIMEText(cuerpo, 'html'))

# Inicializando la configuración del correo
sesionSMTP = smtplib.SMTP(servidorSMTP, puerto)

# Seguridad del Correo para enviarlo
sesionSMTP.starttls()

# Iniciando Sesión
sesionSMTP.login(remitente, password)
texto = mensaje.as_string()

# Envio del Correo 
sesionSMTP.sendmail(remitente, destinatario, texto)

# Cerrar la sesión
sesionSMTP.quit()




