# Cookiecutter Kolibri Plugin

## Usage

* Install Cookiecutter.

  `$ pip install cookiecutter`


* Generate a new Kolibri plugin within current directory.

  `$ cookiecutter https://github.com/christianmemije/cookiecutter-kolibri-plugin`


* Select a plugin name. 
  
  Must be `lowercase_separated_by_underscores` (ie. `vector_video_player`).


* Select a plugin Class name. 
  
  Must be `UpperCamelCase.` (ie. `VectorVideoPlayer`).


* Install newly generated plugin on Kolibri.

  `$ pip install -e <LOCAL_PATH_TO_THIS_PLUGIN_FOLDER>`


* Enable the plugin on Kolibri.

  `$ kolibri plugin <plugin_name> enable`
