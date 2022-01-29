# Cookiecutter Kolibri Plugin

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template for generating minimal Kolibri plugins. [Read more about the plugin architecture here](https://kolibri-dev.readthedocs.io/en/develop/backend_architecture/plugins.html).

## Setup

You do not need to clone this repo to use the template. Instead, first enable your Kolibri Python virtual environment and install these dependencies in it:

```bash
pip install cookiecutter le-utils black sh --upgrade
```

The `cookiecutter` command will create a new top-level project directory in the location where you run the command, as well as a Python module subdirectory. You should run it outside of any existing git repo.

If the plugin is going to be added to the Kolibri repo, after running `cookiecutter` you will copy the Python module subdirectory to `kolibri/plugins` in the Kolibri repo.

If the plugin will be a separate repo, after running `cookiecutter` you will `cd` into it and initialize a new git repo with `git init`. In this case you may also want to first create a new empty repo on GitHub.com. These are generally named like `kolibri-[PLUGIN-NAME]-plugin`, for example [kolibri-oidc-provider-plugin](https://github.com/learningequality/kolibri-oidc-provider-plugin).

## Generate code

In a terminal, `cd` to the place where you want a new project directory created. Run `cookiecutter` with this repo as an argument to start the process:

```bash
cookiecutter https://github.com/learningequality/cookiecutter-kolibri-theme-plugin`
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
