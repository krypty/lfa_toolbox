import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))

setup(
    name="lfa_toolbox",
    version="0.1.4",
    description="LFA Toolbox is an educational library to play with fuzzy systems",
    author="Gary Marigliano",
    url="http://iict-space.heig-vd.ch/cpn/",
    long_description=open(os.path.join(HERE, "README.md")).read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.5",
    setup_requires=["pytest-runner"],
    tests_require=["pytest==3.3.2"],
    include_package_data=True,
)
