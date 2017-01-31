const RootComponent = require('./vue');
const logging = require('kolibri.lib.logging').getLogger(__filename);
{% if cookiecutter.content_renderer_plugin == 'Yes' %}
const ContentRendererModule = require('content_renderer_module');

class {{cookiecutter.plugin_class_name}}Module extends ContentRendererModule {
  get rendererComponent() {
    return RootComponent;
  }
  get contentType() {
    return '{{ '{{ content_kind }}' }}/{{ '{{ file_extension }}' }}';
  }
}
{% else %}
const Vue = require('vue');
const KolibriModule = require('kolibri_module');

class {{cookiecutter.plugin_class_name}}Module extends KolibriModule {
  /*
   Callback invoked when this module is initialized.
   */
  initialize() {
    logging.debug('Module is initialized.');
  }

  /*
   Callback invoked when this module is registered.
   */
  ready() {
    this.rootvue = new Vue({
      el: 'rootvue',
      render: createElement => createElement(RootVue),
    });
  }
}

{% endif %}
module.exports = new {{cookiecutter.plugin_class_name}}Module();
