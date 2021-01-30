from django.core.mail import send_mail

from celery import Celery, shared_task



app = Celery('tasks', broker='pyamqp://guest@localhost//')

@shared_task()
def mail_send_task(email_subject, email_body, from_email, recipient_list, fail_silently=False):
    send_mail(email_subject, email_body, from_email, recipient_list)


