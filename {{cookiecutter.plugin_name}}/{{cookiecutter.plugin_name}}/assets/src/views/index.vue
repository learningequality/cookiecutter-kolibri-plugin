<template>

  <div>
    {% if cookiecutter.content_renderer_plugin != 'Yes' %}
    <h1>{{cookiecutter.readable_plugin_name}}</h1>
    {% endif %}
  </div>

</template>


<script>

  module.exports = {};

</script>


<style lang="stylus" scoped>

  @require '~kolibri.styles.definitions'

</style>
