# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


long_desc = '''Prognosis
==========
| This Python module provides a python wrapper around the API of Econdb.com.
| Prognosis also provides Python abstraction for macroeconomic variables for
| quick and orderly analysis
Installation
------------
Just type:
.. code:: bash
    pip install prognosis
You can also find `Prognosis on Github
<https://github.com/econdb/prognosis/>`_
Documentation
-------------
The documentation on installation, use and API description is found at econdb.com `documentation page. <https://www.econdb.com/documenation/inquisitor/>`_
Usage example
-------------
.. code:: python
	import inquisitor
	qb = inquisitor.Inquisitor()
	### List sources
	qb.sources()
	### List datasets
	qb.datasets(source='EU')
	### Obtain series data
	qb.series(dataset='EI_BSCO_M')
   '''

setup(
    name='prognosis',
    packages=find_packages(),
    version='0.0.1',
    description='A Python client for econdb.com/api/',
    long_description=long_desc,
    author='Oriol Andres',
    license='MIT License',
    author_email='admin@econdb.com',
    url='https://github.com/econdb/prognosis',
    download_url='https://github.com/econdb/prognosis/tarball/0.0.1',
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
