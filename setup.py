#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from jupyter_alabaster_theme import __version__

# Environment and packages
# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# Packages
# MOD_NAME = "jupyter_alabaster_theme"
# PKGS = [x for x in find_packages() if x.split('.')[0] == MOD_NAME]

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
    version=__version__,
    description='Jupyter Alabaster Theme',
    long_description=read_file("README"),
    author='Jeff Forcier, Project Jupyter, and contributors',
    author_email='jupyter@googlegroups.com',
    url='https://alabaster.readthedocs.io',
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
    ],
    entry_points = {
        'sphinx_themes': [
            'path = jupyter_alabaster_theme:get_path',
        ]
    },
)
