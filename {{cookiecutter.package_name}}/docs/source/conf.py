# -*- coding: utf-8 -*-
"""Sphinx Configuration"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import {{ cookiecutter.module_name }}
import alabaster
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'alabaster']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = {{ cookiecutter.module_name }}.__project_name__
copyright = "2015+, {pkg.__author__}".format(pkg={{ cookiecutter.module_name }})

version = {{ cookiecutter.module_name }}.__version__
release = {{ cookiecutter.module_name }}.__version__

exclude_patterns = ['_build', '.env']
pygments_style = 'sphinx'  # Syntax highlighting style

html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_sidebars = {'**': []}
