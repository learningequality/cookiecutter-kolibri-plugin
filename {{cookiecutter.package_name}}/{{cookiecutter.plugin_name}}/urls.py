from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.{{cookiecutter.plugin_class_name}}View.as_view()),
]
