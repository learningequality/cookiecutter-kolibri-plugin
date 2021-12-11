{% set is_frontend_plugin = cookiecutter.content_renderer_plugin == 'Yes' or cookiecutter.frontend_plugin == 'Yes' %}

# {{ cookiecutter.readable_plugin_name }}

Note: this plugin was originally generated from a [Cookiecutter template](https://github.com/learningequality/cookiecutter-kolibri-plugin). The instructions below should be updated by the plugin author.

If this plugin is in the `kolibri/plugins` directory of the Kolibri repo, most of the instructions below do not apply.

## Install this plugin in Kolibri

Activate your Kolibri Python virtual environment.

If this plugin is on PyPi, inside your Kolibri virtual environment you can run:

```bash
pip install {{ cookiecutter.plugin_name }}
```

Enable the plugin:

```bash
kolibri plugin {{ cookiecutter.plugin_name }} enable
```

Add the plugin name to `kolibri/build_tools/build_plugins.txt`.

Finally, rebuild and restart Kolibri.


## Install this plugin for development

Clone this repo, install the plugin in your Kolibri Python virtual environment and enable it:


```bash
pip install -e <LOCAL-PATH-TO-REPO>
kolibri plugin {{ cookiecutter.plugin_name }} enable
```

{% if is_frontend_plugin %}
From the Kolibri repo, update any frontend dependenices:

```bash
yarn install
```
{% endif %}

## Publishing to PyPi

Follow the instructions above to install the plugin for development.

{% if is_frontend_plugin %}
From the Kolibri directory, build the frontend assets:

```bash
yarn run build
```
{% endif %}

Update `setup.py` to a newer version. Move to the root of the plugin directory and run:

```bash
make release
``
