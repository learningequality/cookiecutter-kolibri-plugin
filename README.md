# Cookiecutter Kolibri Plugin
Minimal [Cookiecutter](https://github.com/audreyr/cookiecutter) template for generating [Kolibri](https://github.com/learningequality/kolibri) plugins.

## Usage

* Install Cookiecutter.

  `$ pip install cookiecutter`


* Generate a new Kolibri plugin within the directory of your choice.

  `$ cookiecutter https://github.com/learningequality/cookiecutter-kolibri-plugin`

* Select a readable plugin name. 
  
  e.g. `Vector Video Player`.

* You will then be prompted to enter a description, a repository url, author details, and a license.

* If you would like to change the default pypi package name, you can modify it. 
  
  Must be `kolibri_lowercase_separated_by_underscores` (ie. `kolibri_vector_video_player`).

* If you would like to change the default plugin Class name for the Javascript class, you can modify it. 
  
  Must be `UpperCamelCase.` (ie. `VectorVideoPlayer`).


* Install the newly generated plugin in Kolibri.

  `$ pip install -e <LOCAL_PATH_TO_THE_PLUGIN_DIRECTORY>`
  
  
* Enable the plugin on Kolibri.

  `$ kolibri plugin <plugin_name> enable`
  

* Restart the Kolibri server.


* You can test the plugin by visiting `http://127.0.0.1:8000/<plugin_name>`
