from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks


class PluginTemplateSyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded synchronously in plugin_template/plugin_template.html
    """

    class Meta:
        abstract = True


class PluginTemplateAsyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded asynchronously in plugin_template/plugin_template.html
    """

    class Meta:
        abstract = True
