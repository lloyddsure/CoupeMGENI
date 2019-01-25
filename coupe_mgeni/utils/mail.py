from django.core.mail import send_mail

def envoi_de_mail(subject,message,sender,to):
    send_mail(
        subject,
        message,
        sender,
        [to],
        fail_silently=False,
    )
