<template>

  <div>
    {% if cookiecutter.content_renderer_plugin != 'Yes' %}
    <h1>{{cookiecutter.readable_plugin_name}}</h1>
    {% endif %}
  </div>

</template>


<script>

  export default {
    name: '{{cookiecutter.plugin_class_name}}Index'
  };

</script>


<style lang="stylus" scoped>

  @require '~kolibri.styles.definitions'

</style>
