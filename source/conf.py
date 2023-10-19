# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tech_log'
copyright = '2023, hashitaro330'
author = 'hashitaro330'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'furo'
html_theme = 'classic'
html_static_path = ['_static']

html_title = 'Tech Log'

# html_theme = 'sphinx_rtd_theme'


extensions = ['myst_parser']

# extensions = [
#     'sphinx.ext.autodoc', 
#     'sphinx.ext.viewcode',
#     'sphinx.ext.napoleon',
#     'myst_parser',
#     'sphinx.ext.imgmath',
#     'sphinx.ext.mathjax',
#     'sphinx_math_dollar',
#     ]

# extensions = [
#     'sphinx.ext.autodoc',
#     'sphinx.ext.viewcode',
#     'sphinx.ext.todo',
#     'sphinx.ext.napoleon',
#     'sphinx_rtd_theme'
# ]

# source_suffix = {
#     '.rst': 'restructuretext',
#     '.md': 'markdown',
# }
