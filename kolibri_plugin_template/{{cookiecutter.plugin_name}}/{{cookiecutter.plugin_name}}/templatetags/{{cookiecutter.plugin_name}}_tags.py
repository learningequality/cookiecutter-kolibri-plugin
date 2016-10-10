# coding=utf-8
"""
{{cookiecutter.plugin_name}} template tags
========================
Tags for including plugin javascript assets into a template.
"""

from __future__ import absolute_import, print_function, unicode_literals
from django import template
from kolibri.core.webpack.utils import webpack_asset_render
from .. import hooks

register = template.Library()


@register.simple_tag()
def {{cookiecutter.plugin_name}}_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses {{cookiecutter.plugin_class_name}}SyncHook.
    :return: HTML of script tags to insert into {{cookiecutter.plugin_name}}/{{cookiecutter.plugin_name}}.html
    """
    return webpack_asset_render(hooks.{{cookiecutter.plugin_class_name}}SyncHook, async=False)


@register.simple_tag()
def {{cookiecutter.plugin_name}}_async_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses {{cookiecutter.plugin_class_name}}SyncHook.
    :return: HTML of script tags to insert into {{cookiecutter.plugin_name}}/{{cookiecutter.plugin_name}}.html
    """
    return webpack_asset_render(hooks.{{cookiecutter.plugin_class_name}}AsyncHook, async=True)
