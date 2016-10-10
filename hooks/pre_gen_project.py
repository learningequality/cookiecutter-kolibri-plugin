import re
import sys

PLUGIN_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
plugin_name = '{{ cookiecutter.plugin_name }}'
plugin_class_name = '{{ cookiecutter.plugin_class_name }}'

matching_plugin_class_name = plugin_name.split('_')
matching_plugin_class_name = "".join(x.title() for x in matching_plugin_class_name[:])

if not re.match(PLUGIN_REGEX, plugin_name):
    print(
    'ERROR: "{}" is not a valid Kolibri plugin name. A valid Kolibri plugin name must be lowercase_separated_by_underscores (ie. vector_video_player).'.format(
        plugin_name))
    # exits with status 1 to indicate failure
    sys.exit(1)

if not plugin_class_name == matching_plugin_class_name:
    print(
    'ERROR: "{}" does not match the recommended Kolibri plugin Class name "{}". A valid Kolibri plugin Class name must be UpperCamelCase. (ie. VectorVideoPlayer)'.format(
        plugin_class_name, matching_plugin_class_name))
    # exits with status 1 to indicate failure
    sys.exit(1)
