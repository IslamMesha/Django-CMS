# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from cms.models.pagemodel import Page
from contacts.forms import ContactForm, ContactAjaxForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'templates/contact_form.html'

    def get_initial(self):
        initial = super(ContactFormView, self).get_initial()
        initial['referer'] = self.request.META.get('HTTP_REFERER', ''),
        return initial

    def get_success_url(self):
        page = get_object_or_404(Page, reverse_id='contact_form_submission', publisher_is_draft=False)
        return page.get_absolute_url()

    def form_valid(self, form):
        form.save()
        return super(ContactFormView, self).form_valid(form)


class AjaxableResponseMixin(object):
    def render_to_json_responses(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_responses(form.errors)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_responses(data)
        else:
            return response


class ContactFormAjaxView(AjaxableResponseMixin, FormView):
    form_class = ContactAjaxForm
    http_method_names = [u'post']

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        self.object = form.save(commit=True)
        return super(ContactFormAjaxView, self).form_valid(form)
