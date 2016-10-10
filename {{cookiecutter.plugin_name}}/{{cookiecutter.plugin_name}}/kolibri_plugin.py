from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase
from . import hooks, urls


class {{cookiecutter.plugin_class_name}}(KolibriPluginBase):
    def url_module(self):
        return urls

    def url_slug(self):
        return "^{{cookiecutter.plugin_name}}"


class {{cookiecutter.plugin_class_name}}Asset(webpack_hooks.WebpackBundleHook):
    unique_slug = "{{cookiecutter.plugin_name}}_module"
    src_file = "assets/src/module.js"
    static_dir = "kolibri/plugins/{{cookiecutter.plugin_name}}/static"


class {{cookiecutter.plugin_class_name}}InclusionHook(hooks.{{cookiecutter.plugin_class_name}}SyncHook):
    bundle_class = {{cookiecutter.plugin_class_name}}Asset
