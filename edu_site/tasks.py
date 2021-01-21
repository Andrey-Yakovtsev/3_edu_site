from datetime import time

from django.core.mail import send_mail
from celery import Celery, shared_task


app = Celery('tasks', broker='pyamqp://guest@localhost//')

@shared_task
def do_mail_send(email_subject, email_body, from_email, recipient_list, fail_silently=False):
    print('Job is queued!!!!!!!!!')
    send_mail(email_subject, email_body, from_email, recipient_list, fail_silently=False)
