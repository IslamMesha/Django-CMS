# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from contacts.models import

from django.contrib import admin

from contacts.models import Contact

admin.site.register(Contact)
