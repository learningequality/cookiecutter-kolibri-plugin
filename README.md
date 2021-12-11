# Cookiecutter Kolibri Plugin

This is a minimal [Cookiecutter](https://github.com/audreyr/cookiecutter) template for generating [Kolibri](https://github.com/learningequality/kolibri) plugins.

## Setup

You do not need to clone this repo to use the template. Instead, first enable your Kolibri Python virtual environment and install these dependencies in it:

```bash
pip install cookiecutter le-utils black sh --upgrade
```

If the plugin is going to be added to the Kolibri repo, make a new directory for it under `kolibri/plugins` in the Kolibri repo.

If not, make a new project directory for it outside of the Kolibri repo. In this case you may also want to first create a new empty repo on GitHub.com. These are generally named like `kolibri-[PLUGIN-NAME]-plugin`, for example [kolibri-oidc-provider-plugin](https://github.com/learningequality/kolibri-oidc-provider-plugin).

## Generate code

Change to the newly-created plugin directory. Run `cookiecutter` with this repo as an argument to start the process:

```bash
cookiecutter https://github.com/learningequality/cookiecutter-kolibri-plugin`
```

Cookiecutter will give some prompts:

* Select a readable plugin name, e.g. `Vector Video Player`
* You will then be prompted to enter a description, a repository url, and author details.
* If you would like to change the default pypi package name, you can modify it. It must be `kolibri_lowercase_separated_by_underscores` (ie. `kolibri_vector_video_player`).
* If you would like to change the default plugin Class name for the Javascript class, you can modify it. It must be `UpperCamelCase.` (ie. `VectorVideoPlayer`).
* Select if this is a frontend plugin (i.e. it will provide a Javascript module for frontend code)
* Select if this plugin will have its own page within the Django app - if you are creating an extension of existing functionality in Kolibri, this will not be the case - such as a content renderer plugin.
* Select if this plugin is a content renderer plugin, and what content kind and file extension it handles. If you are not creating a content renderer plugin, you may safely ignore these options.

## Install new plugin in Kolibri (external only)

If the plugin is not in the Kolibri repo under `kolibri/plugins`, some additional configuration is necessary.

Install the newly generated plugin in Kolibri locally for development:

```bash
pip install -e <LOCAL_PATH_TO_THE_PLUGIN_DIRECTORY>`
```

Enable the plugin on Kolibri:

```bash
kolibri plugin <plugin_name> enable`
```

Finally, add the plugin name to `kolibri/build_tools/build_plugins.txt`

## Final steps

Restart the Kolibri server. If the plugin has its own page, you can test the plugin by visiting `http://127.0.0.1:8000/<plugin_name>`

For external plugins, push to the remote repo. For internal plugins, open a PR against the Kolibi repo.
