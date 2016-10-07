from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic.base import TemplateView


class PluginTemplateView(TemplateView):
    template_name = "plugin_template/plugin_template.html"
