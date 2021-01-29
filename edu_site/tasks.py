from courses.forms import ContactForm
from celery import Celery, shared_task



app = Celery('tasks', broker='pyamqp://guest@localhost//')

# @shared_task
# def do_mail_send(email_subject, email_body, from_email, recipient_list, fail_silently=False):
#     ContactForm.do_send_mail(email_subject, email_body, from_email, recipient_list, fail_silently=False)
#
# @app.task
# def do_mail_send(email_subject, email_body, from_email, recipient_list, fail_silently=False):
#     ContactForm.do_send_mail.delay(email_subject, email_body, from_email, recipient_list, fail_silently=False)

# @app.task
# def do_mail_send(email_subject, email_body, from_email, recipient_list, fail_silently=False):
#     ContactForm.do_send_mail.apply_async((
#         (email_subject, email_body, from_email, recipient_list),
#         {}), countdown=60)

@shared_task()
def do_mail_send(email_subject, email_body, from_email, recipient_list, fail_silently=False):
    ContactForm.do_send_mail.apply_async((
        (email_subject, email_body, from_email, recipient_list),
        {}), countdown=60)

