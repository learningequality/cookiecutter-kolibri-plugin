#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup

name = "{{ cookiecutter.plugin_name }}"


setup(
    name=name,
    version="0.1.0",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.repository_url }}",
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
)
