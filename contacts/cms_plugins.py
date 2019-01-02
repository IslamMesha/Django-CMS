from django.core.urlresolvers import reverse
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from contacts.models import ContactPluginModel
from contacts.forms import ContactAjaxForm


class ContactPlugin(CMSPluginBase):
    name = u'Contact Form'
    model = ContactPluginModel
    render_template = 'contact_widget.html'

    def render(self, context, instance, placeholder):
        try:
            path = context['request'].path
        except Exception as exception:
            print('There is some exception in getting request path: ', exception)
            path = ''
        form = ContactAjaxForm(initial={'referer': path})
        context.update({
            'title': instance.title,
            'form': form,
            # 'form_action': reverse('multi_form'),
            'form_action': 'http://localhost:8000/en/multi_form/',
        })
        return context


plugin_pool.register_plugin(ContactPlugin)
