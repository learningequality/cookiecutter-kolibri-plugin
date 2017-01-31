import io
import os
import shutil
from cookiecutter.environment import StrictEnvironment
from le_utils.constants import content_kinds
from cookiecutter.generate import FileSystemLoader

plugin_name = '{{ cookiecutter.plugin_name }}'

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def location(resource):
    return os.path.join(
        PROJECT_DIRECTORY,
        '{{ cookiecutter.plugin_name }}/{resource}'.format(resource=resource)
    )

def remove_file(file_name):
    file = location(file_name)
    if os.path.exists(file):
        os.remove(file)

def remove_folder(folder_name):
    """Remove a folder"""
    folder = location(folder_name)
    if os.path.exists(folder):
        shutil.rmtree(folder)

def render_file(file_name, context, env):
    file = location(file_name)
    assert os.path.exists(file)
    infile = file.replace(os.path.sep, '/')
    tmpl = env.get_template(infile)
    rendered_file = tmpl.render(**context)
    with io.open(file, 'w', encoding='utf-8') as fh:
        fh.write(rendered_file)

if '{{ cookiecutter.frontend_plugin }}' != 'Yes' and '{{ cookiecutter.content_renderer_plugin }}' != 'Yes':
    remove_folder('assets')
    for file in [
        '.eslintrc.js',
        'package.json',
        'webpack.config.js',
        ]:
        remove_file(file)

if '{{ cookiecutter.has_own_page }}' != 'Yes':
    remove_folder('templates')
    remove_folder('templatetags')
    for file in [
        'urls.py',
        'views.py',
        'hooks.py',
        ]:
        remove_file(file)

if '{{ cookiecutter.content_renderer_plugin }}' == 'Yes':
    context = {
        'content_kind': ''
    }
    while context['content_kind'] not in dict(content_kinds.choices):
        print('Choose a content kind that this plugin renders, choose from {}'.format(', '.join(dict(content_kinds.choices).keys())))
        context['content_kind'] = raw_input('Select the content kind that this plugin renders: ')
        if context['content_kind'] not in dict(content_kinds.choices):
            print('Invalid kind.')
    context['file_extension'] = raw_input('Please provide the file extension that this plugin renders: ')
    env = StrictEnvironment(
        context=context,
        keep_trailing_newline=True,
    )
    env.loader = FileSystemLoader('/')
    render_file('kolibri_plugin.py', context, env)
    render_file('assets/src/module.js', context, env)
