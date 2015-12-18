#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "requests",
    "PyGithub",
]

test_requirements = [
    "requests-mock",
    "mock",
    "flake8"
]

setup(
    name='pyup',
    version='0.1.0',
    description="A tool to update all your projects requirements",
    long_description=readme + '\n\n' + history,
    author="Jannis Gebauer",
    author_email='ja.geb@me.com',
    url='https://github.com/pyup/pyup',
    packages=[
        'pyup',
    ],
    package_dir={'pyup':
                 'pyup'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pyup',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    dependency_links=['git+https://github.com/jayfk/PyGithub.git@top#egg=PyGithub']
)
