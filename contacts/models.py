# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone

from mysite import settings


class Contact(models.Model):
    name = models.CharField(u'Name', blank=True, default='', help_text='Enter your name', max_length=64)
    company = models.CharField(u'Company or Organization', blank=True, default='',
                               help_text="Enter your Organization's name",
                               max_length=64)
    email = models.EmailField(u'Email', blank=False, default='',
                              error_messages={'invalid': 'Enter a valid email address'}, help_text='Enter your email',
                              max_length=64)
    telephone = models.CharField(u'Phone Number', blank=True, default='', help_text='Enter your phone number',
                                 max_length=32)
    comments = models.TextField(blank=True, default='', help_text='Let us know what is on your mind?')
    contact_date = models.DateTimeField(blank=False, default=timezone.now,
                                        help_text=u'When this person completed this form')
    was_contacted = models.BooleanField(u'Was contacted or not?', default=False,
                                        help_text=u'Check this if someone has already reached out to this person')
    notes = models.TextField(u'Contact Notes', blank=True, default='',
                             help_text='Internal notes relating to contacting this person')
    referer = models.CharField(u'Referring Page', blank=True, default='',
                               help_text=u'This is page the visitor was on before coming on the contact page',
                               max_length=2084)

    def send_notification_email(self):
        email_subject = render_to_string('contacts/notificaton_subject.txt', {'contact': self, })
        email_body = render_to_string('contacts/notificaton_body.txt', {'contact': self, })
        try:
            send_mail(email_subject, email_body, settings.SERVER_EMAIL, settings.MANAGERS,
                      fail_silently=(not settings.DEBUG))
        except Exception as exception:
            print ('Exception has been occurred while sending email: ', exception)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                self.send_notification_email(self)
            except Exception as exception:
                print ('Exception has been occurred while sending email: ', exception)
                pass
        super(Contact, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s : {%s} ' % (self.name, str(self.contact_date),)


class ContactPluginModel(CMSPlugin):
    title = models.CharField(u'Title', blank=True, help_text=u'Optional. Title of the widget', max_length=64)
