import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

    
def send_mail(sender_mail, receiver_mail, sender_mail_password, file_name, message_subject, message_content):
    smtp_server = 'smtp.gmail.com'
    port = 465
    nom_fichier = 'test.jpg'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'envoie d\'un fichier'
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message.attach(MIMEText('envoyer une pièce jointe', 'plain'))
    with open(file_name, 'rb') as attachment:
        file_part = MIMEBase('application', 'octet-stream')
        file_part.set_payload(attachment.read())
        encoders.encode_base64(file_part)
        file_part.add_header(
        'Content-Disposition',
        'attachment; filename='+ str(nom_fichier)
        )
        message.attach(file_part)
        context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_mail, sender_mail_password)
        server.sendmail(sender_mail, receiver_mail, message.as_string())
        
