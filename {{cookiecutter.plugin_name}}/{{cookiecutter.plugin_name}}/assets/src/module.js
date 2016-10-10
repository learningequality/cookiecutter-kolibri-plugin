const Vue = require('vue');
const KolibriModule = require('kolibri_module');

class {{cookiecutter.plugin_class_name}}Module extends KolibriModule {
  /*
   Inherited callback when this module is initialized.
   */
  initialize() {
    console.log('Module is initialized.');
  }

  /*
   Inherited callback when this module is loaded.
   */
  ready() {
    this.vm = new Vue({
      el: 'body',
      components: {
        rootvue: require('./vue'),
      },
    });
  }
}

module.exports = new {{cookiecutter.plugin_class_name}}Module();
