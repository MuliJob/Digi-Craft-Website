from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os

def send_welcome_email(receiver):
    subject = 'Welcome to Digicraft'
    sender = os.getenv('EMAIL_SENDER')

    text_content = render_to_string('email/digicraftemail.txt')
    html_content = render_to_string('email/digicraftemail.html')

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def message_notification(name):
    subject = 'Digicraft'
    sender = os.getenv('EMAIL_SENDER')
    receiver = os.getenv('ADMIN_EMAIL')

    text_content = render_to_string('email/adminemail.txt', {"name": name})
    html_content = render_to_string('email/adminemail.html', {"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

