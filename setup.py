# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="pytest_strings",
    version="0.0.1",
    url="https://github.com/eddwardo/pytest_strings",
    author="Piotr Szymanski",
    author_email="skyleton@gmail.com",
    packages=find_packages(),
    entry_points={
        "pytest11": [
            "strings = pytest_strings"
        ]
    },
    install_requires=[
        "pytest>2"
    ],
)
