Prognosis
=========

| This Python module provides a python wrapper around the API of Econdb.com.

Installation
------------

You can also find `Econdb on Github
<https://github.com/econdb/prognosis/>`_



Documentation
-------------

The documentation on installation, use and API description is found at econdb.com `documentation page. <https://www.econdb.com/documentation/inquisitor/>`_

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