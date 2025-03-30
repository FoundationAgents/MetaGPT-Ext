#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_namespace_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get requirements from requirements.txt
with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="metagpt-provider-bedrock",
    version="0.1.0",
    description="AWS Bedrock provider for MetaGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekan/MetaGPT-Ext/tree/main/provider/metagpt-provider-bedrock",
    author="MetaGPT Team",
    author_email="meta.gpt.chain@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="metagpt, bedrock, provider, aws",
    packages=find_namespace_packages(include=["metagpt.*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.9, <3.12",
    install_requires=requirements,
    project_urls={
        "Bug Reports": "https://github.com/geekan/MetaGPT-Ext/issues",
        "Source": "https://github.com/geekan/MetaGPT-Ext/",
    },
)
