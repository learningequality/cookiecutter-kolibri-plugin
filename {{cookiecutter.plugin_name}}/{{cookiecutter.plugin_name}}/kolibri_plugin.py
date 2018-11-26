from __future__ import absolute_import, print_function, unicode_literals

{% if cookiecutter.frontend_plugin == 'Yes' or cookiecutter.has_own_page == 'Yes' %}
from kolibri.core.webpack import hooks as webpack_hooks
{% endif %}
from kolibri.plugins.base import KolibriPluginBase
{% if cookiecutter.content_renderer_plugin == 'Yes' %}
from kolibri.core.content import hooks as content_hooks
{% elif cookiecutter.has_own_page == 'Yes' %}
from . import hooks
{% else %}
from kolibri.plugins.user import hooks
{% endif %}


class {{cookiecutter.plugin_class_name}}(KolibriPluginBase):
    {% if cookiecutter.has_own_page  == 'No' %}pass{% else %}
    def url_module(self):
        from . import urls
        return urls

    def url_slug(self):
        return "^{{cookiecutter.plugin_name}}/"
    {% endif %}

{% if cookiecutter.frontend_plugin == 'Yes' or cookiecutter.content_renderer_plugin == 'Yes' %}
class {{ cookiecutter.plugin_class_name }}Asset({% if cookiecutter.content_renderer_plugin == 'Yes' %}content_hooks.ContentRendererHook{% else %}webpack_hooks.WebpackBundleHook{% endif %}):
    unique_slug = "{{ cookiecutter.plugin_name }}_module"
    src_file = "assets/src/{% if cookiecutter.has_own_page == 'Yes' %}app{% else %}module{% endif %}.js"
    {% if cookiecutter.content_renderer_plugin == 'Yes' %}content_types_file = "content_types.json"{% endif %}
{% endif %}

{% if cookiecutter.frontend_plugin == 'Yes' or cookiecutter.has_own_page  == 'Yes' %}
class {{cookiecutter.plugin_class_name}}InclusionHook(hooks.{% if cookiecutter.frontend_plugin == 'Yes' and cookiecutter.has_own_page == 'No' %}UserSyncHook{% else %}{{cookiecutter.plugin_class_name}}SyncHook{% endif %}):
    bundle_class = {{cookiecutter.plugin_class_name}}Asset
{% endif %}
