# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin

from gist.models import GistPluginModel


class GistPlugin(CMSPlugin):
    name = u'Gist'
    render_teplate = 'gist/templates/_gist_plugin.html'
    model = GistPluginModel

    def render(self, context, instance, placeholder):
        return context
