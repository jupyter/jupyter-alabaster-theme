.. user

=================
User
=================

How to install
===============
To use this theme on any Sphinx based documentation, follow these steps:

Install the ``jupyter_alabaster_theme`` package using pip:

.. code::

    pip install jupyter_alabaster_theme

Edit your ``conf.py`` file:

1. Set the theme to ``jupyter_alabaster_theme``:

.. code-block:: python

    html_theme = 'jupyter_alabaster_theme'

2. Add ``jupyter_alabaster_theme`` to the list of extensions:

.. code-block:: python

    extensions = [
       ...
       'jupyter_alabaster_theme',
    ]

3. At the bottom of ``conf.py``, if the following block of code is present,
   remove or modify it, otherwise ``sphinx_rtd_theme`` or the default readthedocs
   theme will be set:

.. code-block:: python

    # -- Read The Docs --------------------------------------------------------

    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if not on_rtd:
        # only import and set the theme if we're building docs locally
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    else:
        # readthedocs.org uses their theme by default, so no need to specify it
        # build rest-api, since RTD doesn't run make
        from subprocess import check_call as sh
        sh(['make', 'rest-api'], cwd=docs)

- Here's an option for modifying the code block above:

.. code-block:: python

    # -- Read The Docs --------------------------------------------------------

    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    # Don't need to set html_theme if done earlier in conf.py
    if on_rtd:
        # Do anything else needed to build documentation on RTD


Update Documentation Dependencies

To get your documentation to build, you will need to update its build
dependencies. Update your ``environment.yml`` or ``requirements.txt`` to depend on
``jupyter_alabaster_theme`` to get the build working on ReadTheDocs.
Note, we have not yet released a `Conda <https://conda.io/docs/intro.html>`_
package for this theme, so you will need to list it in the ``environment.yml``
file under the ``pip`` section.


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

* The theme itself sets ``html_sidebars`` to include a custom sidebar navigation
  template. If you want to use different sidebar templates, simply set your own
  in ``conf.py``, to override the theme's defaults. Otherwise you can add more by:

.. code::

    html_sidebars.update(
      # Additional sidebars can be added here
    )
