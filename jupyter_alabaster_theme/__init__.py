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

    # This add our custom sidebar to the configuration of Sphinx
    if not hasattr(app.config, 'html_sidebars'):
        app.config.html_sidebars = {}
    app.config.html_sidebars['**'] = ['custom_navigation.html']

    # Register our custom search page
    if not hasattr(app.config, 'html_additional_pages'):
        app.config.html_additional_pages = {}
    app.config.html_additional_pages['custom_search'] = 'custom_search.html'

    # Adjust the last updated format
    app.config.html_last_updated_fmt = "%a, %b %d, %Y"

    return {'version': __version__,
            'parallel_read_safe': True}

