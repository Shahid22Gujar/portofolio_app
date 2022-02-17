from django.core.mail import send_mail

from django.conf import settings


def send_email(email,message):
    
    subject = 'Email from Portofolio Website'
    message = f'Thanks for reaching us.\n{message}'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True