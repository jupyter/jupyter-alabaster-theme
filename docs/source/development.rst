.. developer

=================
Development
=================

Running the Docs Locally
========================
* Fork the repository and clone it locally.
* ``cd`` into the Jupyter-Alabaster-Theme directory
* Consider using a ``virtualenv`` or conda ``environment`` to manage packages.
*  Install the packages (from the root of the directory) with pip

.. code::

    pip install -r dev-requirements.txt

* ``cd`` into the docs directory
* The docs can be built with the following:

.. code::

    make clean && make html_theme

The docs will be built in ``build/html``. They can be viewed by starting an HTTP
server and navigating to 0.0.0.0:8000 in your web browser.

.. code::

    python3 -m http.server


Changing the Theme
==================
Modifying CSS:

**Do not** change CSS directly, instead change Post CSS files. This project is
using Post CSS, specifically the `css-next <http://cssnext.io>`_ module. Post
CSS allows us to have nested CSS selectors and makes it easier to read them.

To Add a Post CSS file:

1. Create a file called ``foo.pcss`` in ``jupyter_alabaster_theme/statuc/pcss``

2. Add ``@mimport foo.css`` to ``index.css``.

3. In ``package.json`` add a script with a name ``css:foo`` and action
   ``"postcss jupyter_alabaster_theme/static/pcss/foo.pcss -o jupyter_alabaster_theme/static/css/foo.css",``

4. Update ``css`` script in ``package.json`` to include ``npm run css:foo``.

To compile Post CSS into CSS:

.. code::

    npm run css


Modifying Sphinx templates:

1. Make appropriate changes to templates.

2. Uninstall ``jupyter_alabaster_theme``:

.. code::

    pip uninstall jupyter_alabaster_theme

3. Install the package:


.. code::

    pip install .

4. Re-build the Sphinx documentation (from the appropriate directory) and
   refresh your browser.

.. code::

    make clean && make html
