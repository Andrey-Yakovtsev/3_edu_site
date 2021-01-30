from django import forms
from edu_site.tasks import mail_send_task

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Контактный e-mail')
    name = forms.CharField(label='Имя', widget=forms.TextInput)
    subject = forms.CharField(required=True, label='Тема')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')
    recipient_list = ['admin@example.com']

    def do_send_mail(self):
        mail_send_task.apply_async((
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['from_email'],
            self.recipient_list
        ), countdown=30)

