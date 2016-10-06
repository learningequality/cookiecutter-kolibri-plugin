const KolibriModule = require('kolibri_module');

class PluginTemplateModule extends KolibriModule {
  /*
  inherited callback when this module is initialized.
  */
  initialize() {
    console.log('this module is initialized');
  }

  /*
  inherited callback when this module is loaded.
  */
  ready() {
    console.log('this module is ready');
  }
}

module.exports = new PluginTemplateModule();
