"""Jupyter Alabaster theme."""
import os
import subprocess
import sys


#---------------------------------------------------------------------------
# Find packages
#---------------------------------------------------------------------------

# Set the version of the jupyter_alabaster_theme
__version_info__ = (0, 2, 0)
__version__ = '.'.join(map(str, __version_info__))


#---------------------------------------------------------------------------
# Configure the Sphinx Application
#---------------------------------------------------------------------------



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

