from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives




def envoi_de_mail(subject,message,sender,to):

    html_content = message
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, sender, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    #send_mail(subject,message,sender,[to],fail_silently=False, )
