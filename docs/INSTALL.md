# Installation

lfa_toolbox requires Python>=3.5.

## From PyPI (recommended)

```bash
pip install lfa_toolbox
```

Verify that it works with a Python terminal:

```python
import lfa_toolbox
```

## From sources

1. `git clone <this_repo>`
2. `cd <this_repo>`
3. Create a virtualenv and activate it
```
python -m venv myvenv
./myenv/bin/activate
```
4. Build the sources
```
cd lfa_toolbox
pip install -r requirements.txt
```
5. Install it inside your virtualenv with `python setup.py install`

