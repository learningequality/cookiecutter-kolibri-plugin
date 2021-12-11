from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks


class {{cookiecutter.plugin_class_name}}SyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded synchronously in {{cookiecutter.plugin_name}}/{{cookiecutter.plugin_name}}.html
    """

    class Meta:
        abstract = True


class {{cookiecutter.plugin_class_name}}AsyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded asynchronously in {{cookiecutter.plugin_name}}/{{cookiecutter.plugin_name}}.html
    """

    class Meta:
        abstract = True
