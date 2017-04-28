#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, print_function

import os
from setuptools import setup, find_packages


# Environment and packages
# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# The absolute path to this file
here = os.path.abspath(os.path.dirname(__file__))

# Grab the version information without importing the package
ns = {}
with open(os.path.join(here, 'jupyter_alabaster_theme', 'version.py')) as f:
    exec(f.read(), {}, ns)

# Helpers
def read_file(name):
    """Read file name (without extension) to string."""
    cur_path = os.path.dirname(__file__)
    exts = ('txt', 'rst', 'md')
    for ext in exts:
        path = os.path.join(cur_path, '.'.join((name, ext)))
        if os.path.exists(path):
            with open(path, 'rt') as file_obj:
                return file_obj.read()

    return ''

# Setup
setup(
    name='jupyter_alabaster_theme',
    version=ns['__version__'],
    description='Jupyter Alabaster Theme',
    long_description=read_file("README"),
    author='Jeff Forcier, Project Jupyter, and contributors',
    author_email='jupyter@googlegroups.com',
    url='http://jupyter-alabaster-theme.readthedocs.io/en/latest/index.html',
    license='BSD',
    packages=['jupyter_alabaster_theme'],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],
    install_requires=[
        "setuptools",
        "alabaster"
    ],
    entry_points={
        'sphinx_themes': [
            'path = jupyter_alabaster_theme:get_path',
        ]
    },
)
