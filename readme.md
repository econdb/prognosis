[![Python Versions](https://img.shields.io/pypi/pyversions/prognosis.svg)](https://pypi.python.org/pypi/prognosis)

### Brief

Econdb.com is an aggregator of economic data.

This Python module provides a wrapper around the API of Econdb.com.


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