[![Python Versions](https://img.shields.io/pypi/pyversions/prognosis.svg)](https://pypi.python.org/pypi/prognosis)

# Introduction

The mission of the company is to process information in ways that facilitate understanding of the economic situation|at different granularity levels.

The sources of data include official statistics agencies|and so-called alternative data sources|where we collect direct observations of the market and generate aggregate statistics.

Econdb Ltd. is a limited company registered in United Kingdom|with company number 10759232.

## Table of Contents
- [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Quick examples](#quick-examples)
- [Api reference](#api-reference)
  - [Country](#country)
    - [Available country codes](#available-country-codes)
    - [Methods](#methods)
  - [Country group](#country-group)
    - [Available coutry groups](#available-coutry-groups)
  - [Widget](#widget)
- [License](#license)
## Installation

This Python module provides a wrapper around the API of Econdb.com.
```
pip install prognosis
```

## Quick examples
Some examples are given below|to see more check [examples](./examples)
```python
from prognosis import Country
germany = Country('DE')

### National Accounts
nac = germany.national_accounts()

### Consumer and producer prices
prices = germany.prices()

### Government accounts
gov = germany.government_accounts()
```

# Api reference
## Country
```python
germany = Country('DE')
```
### Available country codes
<details> 
<summary> Countries </summary> 

| **Country**                  | **Code** |
| ---------------------------- | -------- |
| Albania                      | AL       |
| Algeria                      | DZ       |
| Angola                       | AO       |
| Argentina                    | AR       |
| Australia                    | AU       |
| Austria                      | AT       |
| Azerbaijan                   | AZ       |
| Bangladesh                   | BD       |
| Belarus                      | BY       |
| Belgium                      | BE       |
| Bolivia                      | BO       |
| Bosnia And Herzegovina       | BA       |
| Brazil                       | BR       |
| Bulgaria                     | BG       |
| Cambodia                     | KH       |
| Canada                       | CA       |
| Chile                        | CL       |
| China                        | CN       |
| Colombia                     | CO       |
| Costa Rica                   | CR       |
| Croatia                      | HR       |
| Cyprus                       | CY       |
| Czechia                      | CZ       |
| Democratic Republic Of Congo | CD       |
| Denmark                      | DK       |
| Dominican Republic           | DO       |
| Ecuador                      | EC       |
| Egypt                        | EG       |
| El Salvador                  | SV       |
| Estonia                      | EE       |
| Ethiopia                     | ET       |
| European Union               | EU       |
| Finland                      | FI       |
| France                       | FR       |
| Germany                      | DE       |
| Ghana                        | GH       |
| Greece                       | GR       |
| Guatemala                    | GT       |
| Honduras                     | HN       |
| Hong  Kong                   | HK       |
| Hungary                      | HU       |
| India                        | IN       |
| Indonesia                    | ID       |
| Iran                         | IR       |
| Iraq                         | IQ       |
| Ireland                      | IE       |
| Israel                       | IL       |
| Italy                        | IT       |
| Japan                        | JP       |
| Jordan                       | JO       |
| Kazakhstan                   | KZ       |
| Kenya                        | KE       |
| Kuwait                       | KW       |
| Kyrgyzstan                   | KG       |
| Laos                         | LA       |
| Latvia                       | LV       |
| Lebanon                      | LB       |
| Libya                        | LY       |
| Lithuania                    | LT       |
| Luxembourg                   | LU       |
| Macao                        | MO       |
| Malaysia                     | MY       |
| Mexico                       | MX       |
| Mongolia                     | MN       |
| Morocco                      | MA       |
| Myanmar                      | MM       |
| Nepal                        | NP       |
| Netherlands                  | NL       |
| New Zealand                  | NZ       |
| Nicaragua                    | NI       |
| Nigeria                      | NG       |
| Norway                       | NO       |
| Oman                         | OM       |
| Pakistan                     | PK       |
| Panama                       | PA       |
| Paraguay                     | PY       |
| Peru                         | PE       |
| Philippines                  | PH       |
| Poland                       | PL       |
| Portugal                     | PT       |
| Qatar                        | QA       |
| Romania                      | RO       |
| Russian Federation           | RU       |
| Saudi Arabia                 | SA       |
| Senegal                      | SN       |
| Serbia                       | RS       |
| Singapore                    | SG       |
| Slovakia                     | SK       |
| Slovenia                     | SI       |
| South Africa                 | ZA       |
| South Korea                  | KR       |
| Spain                        | ES       |
| Sri Lanka                    | LK       |
| Sudan                        | SD       |
| Sweden                       | SE       |
| Switzerland                  | CH       |
| Taiwan                       | TW       |
| Tajikistan                   | TJ       |
| Tanzania                     | TZ       |
| Thailand                     | TH       |
| Tunisia                      | TN       |
| Turkey                       | TR       |
| Turkmenistan                 | TM       |
| Ukraine                      | UA       |
| United Arab Emirates         | AE       |
| United Kingdom               | UK       |
| United States                | US       |
| Uruguay                      | UY       |
| Uzbekistan                   | UZ       |
| Venezuela                    | VE       |
| Vietnam                      | VN       |
</details>
<br>

### Methods
    
| **Method**                                                   |
| ------------------------------------------------------------ |
| <details><summary>prices()</summary>...</details>              |
| <details><summary>monthly_trade()</summary>...</details>       |
| <details><summary>government_accounts()</summary>...</details> |
| <details><summary>yield_curve()</summary>...</details>         |
| <details><summary>retail_sales()</summary>...</details>        |
| <details><summary>ip()</summary>...</details>                  |
| <details><summary>energy()</summary>...</details>              |

## Country group
```python
germany = Country('DE')
```
### Available coutry groups
| **Country**                  | **Countries** |
| ---------------------------- | -------- |
'Africa'| ['DZ', 'AO', 'CD', 'EG', 'ET', 'GH', 'KE', 'LY', 'MA', 'NG', 'SN', 'ZA', 'SD', 'TZ', 'TN'],
'Central Asia'| ['AZ', 'KZ', 'KG', 'MN', 'TJ', 'TM', 'UZ'],
'East Asia'| ['CN', 'HK', 'JP', 'KR', 'MO', 'TW'],
'Europe'| ['AL', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 'EU', 'UK'],
'G20'| ['AR', 'AU', 'BR', 'CA', 'CN', 'FR', 'DE', 'IN', 'ID', 'IT', 'JP', 'KR', 'MX', 'RU', 'SA', 'ZA', 'TR', 'US', 'EU', 'UK'],
'Latin America'| ['AR', 'BO', 'BR', 'CL', 'CO', 'CR', 'DO', 'EC', 'SV', 'GT', 'HN', 'NI', 'PA', 'PY', 'PE', 'UY', 'VE'],
'Middle East'| ['IR', 'IQ', 'IL', 'JO', 'KW', 'LB', 'OM', 'QA', 'SA', 'AE'],
'North America'| ['CA', 'MX', 'US'],
'Oceania'| ['AU', 'NZ'],
'South Asia'| ['BD', 'IN', 'NP', 'PK', 'LK'],
'Southeast Asia'| ['KH', 'ID', 'LA', 'MY', 'MM', 'PH', 'SG', 'TH', 'VN']

## Widget

# License
MIT