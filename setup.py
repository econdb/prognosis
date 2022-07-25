# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


long_desc = '''Prognosis
=========

| This Python module provides a python wrapper around the API of Econdb.com.


You can also find `Econdb on Github
<https://github.com/econdb/prognosis/>`_


Usage example
-------------



.. code:: python

	from prognosis import Country
	germany = Country('DE')

	### National Accounts
	nac = germany.national_accounts()

	### Consumer and producer prices
	prices = germany.prices()

	### Government accounts
	gov = germany.government_accounts()
'''


setup(
    name='prognosis',
    packages=find_packages(),
    version='0.0.9',
    author='Oriol Andres',
    description='A Python client for econdb.com/api/',
    long_description=long_desc,
    license='MIT License',
    author_email='admin@econdb.com',
    url='https://github.com/econdb/prognosis',
    download_url='https://github.com/econdb/prognosis/tarball/0.0.9',
    keywords=['data', 'economics', 'finance', 'api'],
    install_requires=["requests"],
    tests_require=["httmock"],
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    extras_require={
        "pandas": ["pandas"]
    }
)
