.. user

=================
User
=================

How to install
===============
* ``pip install jupyter_alabaster_theme``
* Edit your ``conf.py`` file to point to the theme:

.. code-block:: python

    # At the top
    from jupyter_alabaster_theme import *
    init_theme()
    # ...
    # Comment out the `html_theme =` line

Important Notes
================
* Avoid using ``captions`` in the ``toctree`` since that is not accessible to mobile
  navigation menus and the breadcrumbs.
* Avoid adding subsections that are on the same page as the section to the ``toctree``.
  Subsections are not accessible to the mobile navigation menus and breadcrumbs.
  This can be avoided by limiting ``maxdepth`` for a ``toctree``. Another option is
  to set the ``titlesonly`` option:

 .. code-block:: python

     .. toctree::
         :titlesonly:

         title1
         title2

* More information about the ``toctree`` can be found at the `Sphinx documentation
  site <http://www.sphinx-doc.org/en/stable/markup/toctree.html>`_
* The theme itself sets ``html_additional_pages`` to include a custom search template.
  If you are using this to add additional pages, to avoid overriding this value, use:

.. code::

    html_additional_pages.update(
      # Additional pages can be added here
    )

* The same goes for ``html_sidebars``. If you want to use different sidebar
  templates, simply set your own to override the theme's defaults. Otherwise you
  can add more by:

.. code::

    html_sidebars.update(
      # Additional sidebars can be added here
    )

    _extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.intersphinx',
        'sphinx.ext.mathjax',
        'nbsphinx',
        'IPython.sphinxext.ipython_console_highlighting',
    ]

    # The suffix(es) of source filenames.
    # You can specify multiple suffix as a list of string:
    source_suffix = ['.rst', '.ipynb']

    # Conf.py import settings
    source_parsers = {}
    def init_theme():
        from recommonmark.parser import CommonMarkParser
        source_parsers['.md'] = CommonMarkParser
        source_suffix.append('.md')