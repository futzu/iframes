#!/usr/bin/env python3

import setuptools
import iframes

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="iframes",
    version=iframes.version(),
    author="Adrian",
    author_email="spam@iodisco.com",
    description="Fast detection of iframes in mpegts streams",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/iframes",
    install_requires=[
        "new_reader",
    ],
    py_modules=["iframes"],
    scripts=['bin/iframes'],
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
)
