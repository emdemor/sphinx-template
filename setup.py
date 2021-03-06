# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="sample",
    version="0.0.0",
    description="....",
    long_description=readme,
    author="Eduardo Morais",
    author_email="emdemor415@gmail.com",
    url="",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
