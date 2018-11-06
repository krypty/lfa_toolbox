# Deployment on PyPI

Note you must increment the version every time you upload to (test)PyPI

Start by getting the sources as described in [INSTALL.md](docs/INSTALL.md)

## Create a binary wheel 

Then in the project root folder, create the binary wheel:

```bash
pip install wheel twine
python setup.py build
python setup.py sdist bdist_wheel
```

Upload the binary to TestPyPI:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Done ! 

