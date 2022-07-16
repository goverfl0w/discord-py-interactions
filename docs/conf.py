# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from interactions.base import __version__

# -- Project information -----------------------------------------------------

project = "interactions.py"
copyright = "2022, goverfl0w"
author = "goverfl0w"
release = __version__
version = ".".join(__version__.split(".", 2)[:2])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_sphinxtabs = True


# descriptions of the relevant function/method.
autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "hoverxref.extension",
    "sphinx_copybutton",
    "enum_tools.autoenum",
]

# Stackoverflow said that this is gonna cure my LaTeX errors for ref handling.
# https://stackoverflow.com/questions/67485567/sphinx-cross-reference-in-latex
latex_elements = {
    "preamble": r"""
\renewcommand{\hyperref}[2][]{#2}
"""
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.

# Language is commented out because of PR reviews. In a RTD-hosted case,
# the variable seems to be skipped.
# language = "de"

locale_dirs = ["locale/"]
gettext_compact = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# This autodocs private attrs and also fixes wrong sort
autodoc_default_options = {"member-order": "bysource", "private-members": True}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Intersphinx
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "discord": ("https://discordpy.readthedocs.io/en/latest/", None),
}
