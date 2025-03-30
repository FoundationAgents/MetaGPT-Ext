#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/11/20
@Author  : alexanderwu
@File    : setup.py
"""

from setuptools import find_namespace_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="metagpt-provider-google-gemini",
    version="0.1.0",
    packages=find_namespace_packages(include=["metagpt.*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    author="DeepWisdom",
    author_email="dongaoming@gmail.com",
    description="Google Gemini Provider for MetaGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekan/MetaGPT",
    install_requires=[
        "metagpt-core>=1.0.0",
        "google-generativeai>=0.3.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
