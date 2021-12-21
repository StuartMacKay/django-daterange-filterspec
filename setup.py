#!/usr/bin/env python
"""
setup.py

setup() is configured with the project metadata so setup.cfg is used
primarily for options for the various tools used.


"""
import os

from setuptools import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
        return fp.read()


setup(
    name="django-daterange-filterspec",
    version="2.0.1",
    description="A DateRange Filter for Django Admin Changelists",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Stuart MacKay",
    author_email="smackay@flagstonesoftware.com",
    keywords="Django Admin DateRage Filter Changelists",
    packages=[
        "daterange",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires="Django>=2.2",
    license="License :: OSI Approved :: BSD License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
