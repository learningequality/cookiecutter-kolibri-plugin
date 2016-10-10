from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic.base import TemplateView


class {{cookiecutter.plugin_class_name}}View(TemplateView):
    template_name = "{{cookiecutter.plugin_name}}/{{cookiecutter.plugin_name}}.html"
