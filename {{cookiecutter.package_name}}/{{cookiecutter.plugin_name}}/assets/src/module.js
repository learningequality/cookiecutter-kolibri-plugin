import RootVue from './views/{{cookiecutter.plugin_class_name}}Index';

{% if cookiecutter.content_renderer_plugin == 'Yes' %}
import ContentRendererModule from 'content_renderer_module';

class {{cookiecutter.plugin_class_name}}Module extends ContentRendererModule {
  get rendererComponent() {
    return RootVue;
  }
}
{% elif cookiecutter.has_own_page == 'Yes' %}
import routes from './routes';
import pluginModule from './modules/pluginModule';
import KolibriApp from 'kolibri_app';

class {{cookiecutter.plugin_class_name}}Module extends KolibriApp {
  get stateSetters() {
    return [];
  }
  get routes() {
    return routes;
  }
  get RootVue() {
    return RootVue;
  }
  get pluginModule() {
    return pluginModule;
  }
  ready() {
    return super.ready().then(() => {
      // reset module states after leaving their respective page
      this.routerInstance.afterEach((toRoute, fromRoute) => {
        this.store.dispatch('resetModuleState', { toRoute, fromRoute });
      });
    });
  }
}
{% else %}
import logger from 'kolibri.lib.logging';
import Vue from 'kolibri.lib.vue';
import KolibriModule from 'kolibri_module';

const logging = logger.getLogger(__filename);

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
{% set plugin_camelcase_name = cookiecutter.plugin_class_name|first|lower + cookiecutter.plugin_class_name[1:] %}

const {{ plugin_camelcase_name }} = new {{cookiecutter.plugin_class_name}}Module();

export { {{ plugin_camelcase_name }} as default };
