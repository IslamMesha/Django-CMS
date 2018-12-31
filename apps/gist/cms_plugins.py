from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class GistPlugin(CMSPlugin):
    name = u'Gist'
    render_template = "gist/templates/_gist_plugin.html"
