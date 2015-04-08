#!/usr/bin/env python
"""pytest-factoryboy package config."""

import codecs
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import pytest_factoryboy


class ToxTestCommand(TestCommand):

    """Test command which runs tox under the hood."""

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        """Initialize options and set their defaults."""
        TestCommand.initialize_options(self)
        self.tox_args = '--recreate'

    def finalize_options(self):
        """Add options to the test runner (tox)."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Invoke the test runner (tox)."""
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, "README.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "AUTHORS.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "CHANGES.rst"), encoding="utf-8").read()
)

setup(
    name="pytest-factoryboy",
    description="Factory Boy support for pytest.",
    long_description=long_description,
    author="Oleg Pidsadnyi, Anatoly Bubenkov and others",
    license="MIT license",
    author_email="oleg.pidsadnyi@gmail.com",
    url="https://github.com/pytest-dev/pytest-factoryboy",
    version=pytest_factoryboy.__version__,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ] + [("Programming Language :: Python :: %s" % x) for x in "2.6 2.7 3.0 3.1 3.2 3.3 3.4".split()],
    cmdclass={"test": ToxTestCommand},
    install_requires=[
        "six",
        "factory_boy",
    ],
    # the following makes a plugin available to py.test
    entry_points={
        "pytest11": [
            "pytest-factoryboy = pytest_factoryboy.plugin",
        ],
    },
    tests_require=["tox"],
    packages=["pytest_factoryboy"],
    include_package_data=True,
)
