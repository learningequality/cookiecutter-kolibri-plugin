from __future__ import absolute_import, print_function, unicode_literals

from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase

from . import hooks

{% if cookiecutter.has_own_page  == 'Yes' %}

class {{cookiecutter.plugin_class_name}}(KolibriPluginBase):
    def url_module(self):
        from . import urls
        return urls

    def url_slug(self):
        return "^{{cookiecutter.plugin_name}}/"

{% endif %}
{% if cookiecutter.content_renderer_plugin == 'Yes' or cookiecutter.frontend_plugin == 'Yes' %}

class {{ cookiecutter.plugin_class_name }}Asset(webpack_hooks.WebpackBundleHook):
    unique_slug = "{{ cookiecutter.plugin_name }}_module"
    src_file = "assets/src/{% if cookiecutter.has_own_page %}app{% else %}module{% endif %}.js"
    {% if cookiecutter.content_renderer_plugin == 'Yes' %}
    events = {
        "content_render:{{ '{{ content_kind }}' }}/{{ '{{ file_extension }}' }}": "render"
    }
    {% endif %}

{% endif %}
{% if cookiecutter.content_renderer_plugin  == 'Yes' %}

class {{ cookiecutter.plugin_class_name }}InclusionHook(hooks.LearnASyncHook):
    bundle_class = {{ cookiecutter.plugin_class_name }}Asset

{% endif %}
