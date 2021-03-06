#!/usr/bin/env python
from smug import version
from setuptools import setup, find_packages

try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []

setup(
    name="smug",
    version=version,
    long_description=__doc__,
    url="https://github.com/ClinicalGenomicsGBG/smug",
    author="Isak Sylvin",
    author_email="isak.sylvin@gu.se",
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["smug=smug.cli:root"],
    },
)
