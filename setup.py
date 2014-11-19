#!/usr/bin/env python
#coding=utf-8

import os

from setuptools import setup, find_packages

setup(
    name = "object2json",
    version = "0.1",
    author = "Hust.cc",
    author_email = "i@hust.cc",
    description = ("Python script converts Object to JSON"),
    license = "LICENSE",
    keywords = "python object convert json",
    url = "https://github.com/hustcc/object2json",
    py_modules=['object2json'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: The MIT License (MIT)",
        ],
    install_requires=[
        ],
    entry_points={
    }
)