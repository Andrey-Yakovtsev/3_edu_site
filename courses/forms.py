from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Контактный e-mail')
    name = forms.CharField(label='Имя', widget=forms.TextInput)
    subject = forms.CharField(required=True, label='Тема')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')

    def do_send_mail(self, email_subject, email_body, from_email, recipient_list=['admin@example.com'], fail_silently=False):
        send_mail(self.email_subject, self.message, self.from_email, recipient_list=['admin@example.com'])


