from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Контактный e-mail')
    name = forms.CharField(label='Имя', widget=forms.TextInput)
    subject = forms.CharField(required=True, label='Тема')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')
    recipient_list = ['admin@example.com']

    def do_send_mail(self):
        send_mail(self.cleaned_data['subject'], self.cleaned_data['message'], self.cleaned_data['from_email'], self.recipient_list) #.apply_async(countdown=10)

    # def do_send_mail(self, email_subject, message, from_email, recipient_list, fail_silently=False):
    #     email_subject = 'COURSESAPP :: Contact form message '
    #     email_body = f'You have new message: ' \
    #                  f'Sender e-mail : {from_email}, ' \
    #                  f'Message: {message}'
    #     recipient_list = ['admin@example.com']
    #     send_mail(self.email_subject, self.message, self.from_email, recipient_list).apply_async(countdown=10)
