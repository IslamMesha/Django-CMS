# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from gist.forms import GistPluginAdminForm
from gist.models import GistPluginModel
from mysite import settings


class GistPlugin(CMSPluginBase):
    name = u'Gist'
    text_enabled = True
    model = GistPluginModel
    form = GistPluginAdminForm
    render_template = '_gist_plugin.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'gist/images/git.png'

    def icon_alt(self, instance):
        return u'Gist: %s' % instance


plugin_pool.register_plugin(GistPlugin)
