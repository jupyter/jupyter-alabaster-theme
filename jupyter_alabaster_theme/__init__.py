"""Jupyter Alabaster theme."""
import os
import subprocess
import sys

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]

def bash(fileName):
    """Runs a bash script in the local directory"""
    sys.stdout.flush()
    subprocess.call("bash {}".format(fileName), shell=True)

__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def update_context(app, pagename, templatename, context, doctree):
    context['jupyter_alabaster_theme_version'] = __version__

def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': __version__,
            'parallel_read_safe': True}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.ipynb']

# Conf.py import settings
source_parsers = {}
def init_theme():
    from recommonmark.parser import CommonMarkParser
    source_parsers['.md'] = CommonMarkParser
    source_suffix.append('.md')

html_theme = 'jupyter'
html_theme_path = get_html_theme_path()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'IPython.sphinxext.ipython_console_highlighting',
]

html_sidebars = {
   '**': [
        'custom_navigation.html'
    ]
}

html_additional_pages = {
    'custom_search': 'custom_search.html'
}

html_last_updated_fmt = "%a, %b %d, %Y"
