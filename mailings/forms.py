from django import forms

from mailings.models import Client


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('user',)

