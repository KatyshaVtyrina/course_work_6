from django import forms

from mailings.models import Client, Mailings, Message


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('user',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailings
        exclude = ('status', 'user')


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
