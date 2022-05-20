[![Python Versions](https://img.shields.io/pypi/pyversions/prognosis.svg)](https://pypi.python.org/pypi/prognosis)

### Brief

Econdb.com is an aggregator of economic data.

This Python module provides a wrapper around the API of Econdb.com.

To send requests to the API, users need to provide an authentication token, which can be obtained by registering at econdb.com.

Documentation of the API and use examples can be found on the [documentation site](https://www.econdb.com/documentation/inquisitor).

### Installation

```pip install prognosis```

### Quick examples

```
from prognosis import Country
germany = Country('DE')

### National Accounts
nac = germany.national_accounts()

### Consumer and producer prices
prices = germany.prices()

### Government accounts
gov = germany.government_accounts()
```

### License

MIT