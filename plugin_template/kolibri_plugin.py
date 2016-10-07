from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase
from . import hooks, urls


class PluginTemplate(KolibriPluginBase):
    def url_module(self):
        return urls

    def url_slug(self):
        return "^plugin_template"


class PluginTemplateAsset(webpack_hooks.WebpackBundleHook):
    unique_slug = "plugin_template_module"
    src_file = "assets/src/module.js"
    static_dir = "kolibri/plugins/plugin_template/static"


class PluginTemplateInclusionHook(hooks.PluginTemplateSyncHook):
    bundle_class = PluginTemplateAsset
