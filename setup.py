import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pybetaface",
    version="1.0",
    description="Use the BetaFace API in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/williamd47/pybetaface",
    author="WilliamD47",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pybetaface"],
    include_package_data=True,
    install_requires=["requests"],
)