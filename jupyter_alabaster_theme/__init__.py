"""Jupyter Alabaster theme."""

from __future__ import absolute_import, print_function

import os
import subprocess
import sys


# Import version information
from .version import version_info, __version__


def get_path():
    """Return the absolute path of the parent directory of this file."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    """Update the Sphinx context to include the version of this package."""
    context['jupyter_alabaster_theme_version'] = __version__


def setup(app):
    """Configure the Sphinx application object.

    See the API in http://www.sphinx-doc.org/en/stable/extdev/appapi.html
    """
    # Setup event for html-path-context
    app.connect('html-page-context', update_context)

    # Add in correct Date Time format for Documentation footer
    app.config.html_last_updated_fmt = "%a, %b %d, %Y"

    # Safely add navigation.html to the html_sidebars
    if not hasattr(app.config, 'html_sidebars'):
        app.config.html_sidebars = {}
    if '**' not in app.config.html_sidebars:
        app.config.html_sidebars['**'] = []
    app.config.html_sidebars['**'].append('navigation.html')

    # Return information
    return {'version': __version__,
            'parallel_read_safe': True}
