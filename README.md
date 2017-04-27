# Jupyter Alabaster Theme

A Sphinx theme for Jupyter based on the [Alabaster theme](https://alabaster.readthedocs.io/en/latest/).

## Installation and configuration

To use this theme on any Sphinx based documentation, follow these steps:

First, install the `jupyter_alabaster_theme` package using pip:

```bash
pip install jupyter_alabaster_theme
```

Second, edit the `conf.py` configuration file to point to the theme. There are three places 
in that file you will need to make changes.

At the top of the file, add an import of the theme and call `init_theme()`:

```python
# At the top.
from jupyter_alabaster_theme import init_theme
init_theme()
```

Further below, under the "Options for HTML output" section, commend out the line
that begins with `html_theme`:

```python
# Comment this line out
# html_theme = ...
```

Finally, at the bottom of `conf.py`, the following block of code, if present, should be removed:

```python
if not on_rtd:
    # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

Third, you will need to update your `environment.yml` or `requirements.txt` to depend on 
`jupyter_alabaster_theme` to get the build working on ReadTheDocs. Note, we have not yet
released a [Conda](https://conda.io/docs/intro.html) package for this theme, so you will
need to list it in the `environment.yml` file under the `pip` section.

## Questions

If you have questions about this project, please go to our Gitter channel:

https://gitter.im/jupyter/jupyter

