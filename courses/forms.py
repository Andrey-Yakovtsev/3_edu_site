from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Контактный e-mail')
    name = forms.CharField(label='Имя', widget=forms.TextInput)
    subject = forms.CharField(required=True, label='Тема')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')

    def do_send_mail(self, email_subject, email_body, from_email, recipient_list=['admin@example.com'], fail_silently=False):
        email_subject = 'COURSESAPP :: Contact form message '
        email_body = f'You have new message: ' \
                     f'Sender name: {self.name}' \
                     f'Sender e-mail : {self.from_email}, ' \
                     f'Message: {self.message}'
        from_email = self.from_email
        name = self.name
        recipient_list = ['admin@example.com']
        send_mail(self.subject, self.message, self.from_email, recipient_list=['admin@example.com']).apply_async(countdown=10)
