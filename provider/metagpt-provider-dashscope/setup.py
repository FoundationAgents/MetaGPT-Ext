#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/8
@Author  : mashenquan
@File    : setup.py
"""

import setuptools
from setuptools import find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="metagpt-provider-dashscope",
    version="0.1.0",
    author="MetaGPT Team",
    author_email="MetaGPT@gmail.com",
    description="DashScope Provider for MetaGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekan/MetaGPT-Ext",
    include_package_data=True,
    packages=find_namespace_packages(include=["metagpt.*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={"metagpt": ["provider/dashscope/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=required,
)
