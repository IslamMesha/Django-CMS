from django import forms
from django.forms import ModelForm
from contacts.models import Contact


class ContactBaseForm(ModelForm):
    class Meta:
        abstract = True

    required_css_class = 'required'
    verify_email = forms.EmailField(label=u'Verify Email', help_text=u'Please retype your email here.', max_length=255,
                                    required=True)
    required_fields = []

    def __init__(self, *args, **kwargs):
        super(ContactBaseForm, self).__init__(*args, **kwargs)
        for field in self.required_fields:
            self.fields[field].required = True

    def clean(self):
        cleaned_data = super(ContactBaseForm, self).clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')
        if email != verify_email:
            raise forms.ValidationError(u'Please ensure that you enter the correct email address twice.')
        return cleaned_data


class ContactForm(ContactBaseForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'company', 'email', 'verify_email', 'telephone', 'comments', 'referer'
        ]
        widgets = {
            'referer': forms.HiddenInput(),
        }

    required_fields = ['name', 'email', 'verify_email', ]


class ContactAjaxForm(ContactBaseForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'verify_email', 'telephone', 'referer'
        ]
        widgets = {
            'referer': forms.HiddenInput(),
        }

    required_fields = ['email', 'verify_email', ]
