# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models


class GistPluginModel(CMSPlugin):
    gist_id = models.CharField('Gist ID', blank=False, default='', help_text='Please supply the GitHub username',
                               max_length=32)
    gist_user = models.CharField('GitHub User', blank=False, default='', help_text='Please supply the GitHub username',
                                 max_length=32)

    file_name = models.CharField('File Name', blank=True, default='', help_text='Optional supply a filename',
                                 max_length=64)

    def __unicode__(self):
        return u'%s:%s:%s' % (self.gist_id, self.gist_user, self.file_name)
