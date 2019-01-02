from django.conf.urls import url
from contacts.views import ContactFormView, ContactFormAjaxView

urlpatterns = [
    url(r'^multi_form$', view=ContactFormAjaxView.as_view(), name='multi_form'),
    url(r'^$', view=ContactFormView.as_view(), name='contact-form'),
]
