#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_namespace_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name="metagpt-provider-anthropic",
    version="0.1.0",
    description="Anthropic (Claude) provider for MetaGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MetaGPT Team",
    author_email="contact@deepwisdom.ai",
    url="https://github.com/geekan/MetaGPT-Ext",
    packages=find_namespace_packages(include=["metagpt.*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=required,
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
