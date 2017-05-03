# Jupyter Alabaster Theme

[![Documentation Status](http://readthedocs.org/projects/jupyter-alabaster-theme/badge/?version=latest)](http://jupyter-alabaster-theme.readthedocs.io/en/latest/?badge=latest)

A Sphinx theme for Jupyter based on the [Alabaster theme](https://alabaster.readthedocs.io/en/latest/).

To use this theme on any Sphinx based documentation, follow these steps:

## Installation

Install the `jupyter_alabaster_theme` package using pip:

```bash
pip install jupyter_alabaster_theme
```

## Configuration

To use the theme in your Sphinx based documentation, follow these steps. For further
details, see the documentation for this theme [here](http://jupyter-alabaster-theme.readthedocs.io/en/latest/).

### Edit `conf.py`

Most of the work to use the theme is in editing your `conf.py` file that configures
Sphinx.

First, You will need to set the theme itself to `jupyter_alabaster_theme`:

```python
html_theme = 'jupyter_alabaster_theme'
```

Second, you will need to add `jupyter_alabaster_theme` to the list of extensions:

```python
extensions = [
    ...
    'jupyter_alabaster_theme',
]
```

Finally, at the bottom of `conf.py`, the following block of code, if present, should be removed:

```python
if not on_rtd:
    # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

### Update documentation dependencies

To get your documentation to build, you will need to update its build dependencies. Update your `environment.yml` or `requirements.txt` to depend on  `jupyter_alabaster_theme` to get the build working on ReadTheDocs. Note, we have not yet released a [Conda](https://conda.io/docs/intro.html) package for this theme, so you will need to list it in the `environment.yml` file under the `pip` section.

## Questions

If you have questions about this project, please go to our Gitter channel:

https://gitter.im/jupyter/jupyter
