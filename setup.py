import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))

setup(
    name="lfa_toolbox",
    version="0.2",
    description="LFA Toolbox is an educational library to play with fuzzy systems",
    author="Gary Marigliano",
    url="http://iict-space.heig-vd.ch/cpn/",
    long_description=open(os.path.join(HERE, "README.md")).read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.5",
    install_requires=["numpy>=1.10", "matplotlib>=2.1.1"],
    setup_requires=["numpy>=1.10", "matplotlib>=2.1.1", "pytest-runner"],
    tests_require=["pytest==3.3.2"],
    include_package_data=True,
    license="GPL",
    classifier=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
)
