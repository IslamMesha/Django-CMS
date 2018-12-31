# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gist.models import GistPluginModel

# TODO: Write a line of code which get all of the project apps.
admin.site.register(GistPluginModel)
