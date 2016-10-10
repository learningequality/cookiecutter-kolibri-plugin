# coding=utf-8
"""
Plugin Template template tags
========================
Tags for including plugin javascript assets into a template. To use:
.. code-block:: html
    {% load plugin_template_tags %}
    <!-- Render inclusion tag for frontend JS elements -->
    {% plugin_template_assets %}
"""

from __future__ import absolute_import, print_function, unicode_literals
from django import template
from kolibri.core.webpack.utils import webpack_asset_render
from .. import hooks

register = template.Library()


@register.simple_tag()
def plugin_template_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses PluginTemplateSyncHook.
    :return: HTML of script tags to insert into plugin_template/plugin_template.html
    """
    return webpack_asset_render(hooks.PluginTemplateSyncHook, async=False)


@register.simple_tag()
def plugin_template_async_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses PluginTemplateSyncHook.
    :return: HTML of script tags to insert into plugin_template/plugin_template.html
    """
    return webpack_asset_render(hooks.PluginTemplateAsyncHook, async=True)
