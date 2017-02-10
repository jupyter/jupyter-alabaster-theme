## Installation
Install the package using PIP, from the root of this directory:

```bash
pip install .
```

Edit the "conf.py" configuration file to point to the jupyter theme:

```python
# At the top.
from jupyter_alabaster_theme import *
init_theme()

# ...

# Comment out the `html_theme =` line
```
