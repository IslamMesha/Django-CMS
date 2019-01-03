from django.forms.models import ModelForm
from easy_select2.widgets import Select2

from gist.models import GistPluginModel


class GistPluginAdminForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = GistPluginModel

    def __init__(self, *args, **kwargs):
        super(GistPluginAdminForm, self).__init__(*args, **kwargs)

        def get_choices():
            values = GistPluginModel.objects.values_list('gist_user', flat=True).distinct().order_by('gist_user')
            return [{'id': str(value), 'text': str(value)} for value in values]

        self.fields['gist_user'].widget = Select2(select2attrs={
            'data': get_choices()
        }, )
