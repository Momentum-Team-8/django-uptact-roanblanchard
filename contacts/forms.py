from django.forms import ModelForm, Textarea
from .models import Contact, Note


class ContactForm(ModelForm):
    class Meta:
        widgets = {'note': Textarea(attrs={'cols': 80, 'rows': 20})}
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
            'note',
        ]
