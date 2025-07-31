#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="stockAnalysisTool",
    version="0.1.4",
    description="A Package which help user to analysis and filter out good stock",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kenneth Zeng",
    author_email="kennethyzeng@gmail.com",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),  # Automatically includes 'stockAnalysisTool'
    install_requires=[     #list dependencies
        "requests>=2.0.0",  # Example dependency
        "openpyxl>=3.1.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)