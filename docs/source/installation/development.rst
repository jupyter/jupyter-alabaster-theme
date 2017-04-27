.. developer

=================
Development
=================
* Fork the repository and clone it locally.
* `cd` into the Jupyter-Alabaster-Theme directory
* Consider using a `virtualenv` or conda `environment` to manage packages.
*  Install the packages (from the root of the directory) with pip

.. code::

    pip install -r dev-requirements.txt

* `cd` into the docs directory
* The docs can be built with the following:

.. code::

    make clean && make html_theme

The docs will be built in `build/html`. They can be viewed by starting an HTTP
server and navigating to 0.0.0.0:8000 in your web browser.
.. code::

    python3 -m http.server
