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
    - [Methods](#methods-1)
  - [Widget](#widget)
    - [Methods](#methods-2)
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
from prognosis import Country
germany = Country('DE')
```
### Available country codes
<details> 
<summary> Countries </summary> 

| **Country**                  | **Code** |
| ---------------------------- | -------- |
| Albania                      | `'AL'`   |
| Algeria                      | `'DZ'`   |
| Angola                       | `'AO'`   |
| Argentina                    | `'AR'`   |
| Australia                    | `'AU'`   |
| Austria                      | `'AT'`   |
| Azerbaijan                   | `'AZ'`   |
| Bangladesh                   | `'BD'`   |
| Belarus                      | `'BY'`   |
| Belgium                      | `'BE'`   |
| Bolivia                      | `'BO'`   |
| Bosnia And Herzegovina       | `'BA'`   |
| Brazil                       | `'BR'`   |
| Bulgaria                     | `'BG'`   |
| Cambodia                     | `'KH'`   |
| Canada                       | `'CA'`   |
| Chile                        | `'CL'`   |
| China                        | `'CN'`   |
| Colombia                     | `'CO'`   |
| Costa Rica                   | `'CR'`   |
| Croatia                      | `'HR'`   |
| Cyprus                       | `'CY'`   |
| Czechia                      | `'CZ'`   |
| Democratic Republic Of Congo | `'CD'`   |
| Denmark                      | `'DK'`   |
| Dominican Republic           | `'DO'`   |
| Ecuador                      | `'EC'`   |
| Egypt                        | `'EG'`   |
| El Salvador                  | `'SV'`   |
| Estonia                      | `'EE'`   |
| Ethiopia                     | `'ET'`   |
| European Union               | `'EU'`   |
| Finland                      | `'FI'`   |
| France                       | `'FR'`   |
| Germany                      | `'DE'`   |
| Ghana                        | `'GH'`   |
| Greece                       | `'GR'`   |
| Guatemala                    | `'GT'`   |
| Honduras                     | `'HN'`   |
| Hong  Kong                   | `'HK'`   |
| Hungary                      | `'HU'`   |
| India                        | `'IN'`   |
| Indonesia                    | `'ID'`   |
| Iran                         | `'IR'`   |
| Iraq                         | `'IQ'`   |
| Ireland                      | `'IE'`   |
| Israel                       | `'IL'`   |
| Italy                        | `'IT'`   |
| Japan                        | `'JP'`   |
| Jordan                       | `'JO'`   |
| Kazakhstan                   | `'KZ'`   |
| Kenya                        | `'KE'`   |
| Kuwait                       | `'KW'`   |
| Kyrgyzstan                   | `'KG'`   |
| Laos                         | `'LA'`   |
| Latvia                       | `'LV'`   |
| Lebanon                      | `'LB'`   |
| Libya                        | `'LY'`   |
| Lithuania                    | `'LT'`   |
| Luxembourg                   | `'LU'`   |
| Macao                        | `'MO'`   |
| Malaysia                     | `'MY'`   |
| Mexico                       | `'MX'`   |
| Mongolia                     | `'MN'`   |
| Morocco                      | `'MA'`   |
| Myanmar                      | `'MM'`   |
| Nepal                        | `'NP'`   |
| Netherlands                  | `'NL'`   |
| New Zealand                  | `'NZ'`   |
| Nicaragua                    | `'NI'`   |
| Nigeria                      | `'NG'`   |
| Norway                       | `'NO'`   |
| Oman                         | `'OM'`   |
| Pakistan                     | `'PK'`   |
| Panama                       | `'PA'`   |
| Paraguay                     | `'PY'`   |
| Peru                         | `'PE'`   |
| Philippines                  | `'PH'`   |
| Poland                       | `'PL'`   |
| Portugal                     | `'PT'`   |
| Qatar                        | `'QA'`   |
| Romania                      | `'RO'`   |
| Russian Federation           | `'RU'`   |
| Saudi Arabia                 | `'SA'`   |
| Senegal                      | `'SN'`   |
| Serbia                       | `'RS'`   |
| Singapore                    | `'SG'`   |
| Slovakia                     | `'SK'`   |
| Slovenia                     | `'SI'`   |
| South Africa                 | `'ZA'`   |
| South Korea                  | `'KR'`   |
| Spain                        | `'ES'`   |
| Sri Lanka                    | `'LK'`   |
| Sudan                        | `'SD'`   |
| Sweden                       | `'SE'`   |
| Switzerland                  | `'CH'`   |
| Taiwan                       | `'TW'`   |
| Tajikistan                   | `'TJ'`   |
| Tanzania                     | `'TZ'`   |
| Thailand                     | `'TH'`   |
| Tunisia                      | `'TN'`   |
| Turkey                       | `'TR'`   |
| Turkmenistan                 | `'TM'`   |
| Ukraine                      | `'UA'`   |
| United Arab Emirates         | `'AE'`   |
| United Kingdom               | `'UK'`   |
| United States                | `'US'`   |
| Uruguay                      | `'UY'`   |
| Uzbekistan                   | `'UZ'`   |
| Venezuela                    | `'VE'`   |
| Vietnam                      | `'VN'`   |
</details>

### Methods
    
- <details><summary><code>prices()</code></summary>Consumer and producer price index</details>              
- <details><summary><code>monthly_trade()</code></summary>Monthly imports and exports, in current prices</details>      
- <details><summary><code>government_accounts()</code></summary>Quarterly government accounts, in current prices, and government debt</details> 
- <details><summary><code>yield_curve()</code></summary>3 month and 10 year bond yields</details>         
- <details><summary><code>retail_sales()</code></summary>Monthly retail sales</details>        
- <details><summary><code>ip()</code></summary>Monthly industrial production</details>                  
- <details><summary><code>energy()</code></summary>Oil, gas, and gasoline production and demand. Data source: JODI.</details>        
- <details><summary><code>national_accounts()</code></summary>Quarterly national accounts in constant prices, by expenditure</details>         

## Country group
```python
from prognosis import CountryGroup
africa = CountryGroup('Africa')
custom_group = CountryGroup(['RU' 'US' 'CN'])
```
### Available coutry groups

<details>
<summary>Groups</summary>

| **Group**          | **Included country codes**                                                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'Africa'`         | ['DZ' 'AO' 'CD' 'EG' 'ET' 'GH' 'KE' 'LY' 'MA' 'NG' 'SN' 'ZA' 'SD' 'TZ' 'TN']                                                                                                                                     |
| `'Central Asia'`   | ['AZ' 'KZ' 'KG' 'MN' 'TJ' 'TM' 'UZ']                                                                                                                                                                                     |
| `'East Asia'`      | ['CN' 'HK' 'JP' 'KR' 'MO' 'TW']                                                                                                                                                                                           |
| `'Europe'`         | ['AL' 'AT' 'BY' 'BE' 'BA' 'BG' 'HR' 'CY' 'CZ' 'DK' 'EE' 'FI' 'FR' 'DE' 'GR' 'HU' 'IE' 'IT' 'LV' 'LT' 'LU' 'NL' 'NO' 'PL' 'PT' 'RO' 'RU' 'RS' 'SK' 'SI' 'ES' 'SE' 'CH' 'TR' 'UA' 'EU' 'UK'] |
| `'G20'`            | ['AR' 'AU' 'BR' 'CA' 'CN' 'FR' 'DE' 'IN' 'ID' 'IT' 'JP' 'KR' 'MX' 'RU' 'SA' 'ZA' 'TR' 'US' 'EU' 'UK']                                                                                                       |
| `'Latin America'`  | ['AR' 'BO' 'BR' 'CL' 'CO' 'CR' 'DO' 'EC' 'SV' 'GT' 'HN' 'NI' 'PA' 'PY' 'PE' 'UY' 'VE']                                                                                                                         |
| `'Middle East'`    | ['IR' 'IQ' 'IL' 'JO' 'KW' 'LB' 'OM' 'QA' 'SA' 'AE']                                                                                                                                                                   |
| `'North America'`  | ['CA' 'MX' 'US']                                                                                                                                                                                                             |
| `'Oceania'`        | ['AU' 'NZ']                                                                                                                                                                                                                   |
| `'South Asia'`     | ['BD' 'IN' 'NP' 'PK' 'LK']                                                                                                                                                                                                 |
| `'Southeast Asia'` | ['KH' 'ID' 'LA' 'MY' 'MM' 'PH' 'SG' 'TH' 'VN']                                                                                                                                                                          |
</details>

### Methods

<ul>    
    <li>
        <details>
            <summary><code>get_topic(topic)</code></summary>
            <br>
            <p>Available topics</p>
            <table>
                <thead>
                    <tr>
                        <th><strong>Topic</strong></th>
                        <th><strong>Description</strong></th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><code>'GDP'</code></td> <td>Gross domestic product</td></tr>
                    <tr><td><code>'PRC'</code></td> <td>Private consumption</td></tr>
                    <tr><td><code>'CON'</code></td> <td>Total consumption</td></tr>
                    <tr><td><code>'GCF'</code></td> <td>Gross capital formation</td></tr>
                    <tr><td><code>'GFCF'</code></td> <td>Gross fixed capital formation</td></tr>
                    <tr><td><code>'CI'</code></td> <td>Change in inventories</td></tr>
                    <tr><td><code>'CBAL'</code></td> <td>Commercial balance (goods + services</tr></td></tr>
                    <tr><td><code>'EXP'</code></td> <td>Exports of goods and services</td></tr>
                    <tr><td><code>'IMP'</code></td> <td>Imports of goods and services</td></tr>
                    <tr><td><code>'PI'</code></td> <td>Personal income</td></tr>
                    <tr><td><code>'RGDP'</code></td> <td>Real gross domestic product</td></tr>
                    <tr><td><code>'RPRC'</code></td> <td>Real private consumption</td></tr>
                    <tr><td><code>'RPUC'</code></td> <td>Real public consumption</td></tr>
                    <tr><td><code>'RCON'</code></td> <td>Real total consumption</td></tr>
                    <tr><td><code>'RGCF'</code></td> <td>Real gross capital formation</td></tr>
                    <tr><td><code>'RGFCF'</code></td> <td>Real gross fixed capital formation<td></tr>
                    <tr><td><code>'RCI'</code></td> <td>Real change in inventories</td></tr>
                    <tr><td><code>'REXP'</code></td> <td>Real exports of goods and services</td></tr>
                    <tr><td><code>'RIMP'</code></td> <td>Real imports of goods and services</td></tr>
                    <tr><td><code>'GDPPC'</code></td> <td>GDP per capita</td></tr>
                    <tr><td><code>'RGDPPC'</code></td> <td>Real GDP per capita</td></tr>
                    <tr><td><code>'GDPD'</code></td> <td>GDP (current US dollars</tr></td></tr>
                    <tr><td><code>'GDPDEF'</code></td> <td>GDP deflator</td></tr>
                    <tr><td><code>'CPI'</code></td> <td>Consumer price index</td></tr>
                    <tr><td><code>'CORE'</code></td> <td>Core consumer price index</td></tr>
                    <tr><td><code>'PPI'</code></td> <td>Producer price index</td></tr>
                    <tr><td><code>'URATE'</code></td> <td>Unemployment</td></tr>
                    <tr><td><code>'JVR'</code></td> <td>Job vacancy rate</td></tr>
                    <tr><td><code>'JQR'</code></td> <td>Job quits rate</td></tr>
                    <tr><td><code>'JLR'</code></td> <td>Job layoffs rate</td></tr>
                    <tr><td><code>'JHR'</code></td> <td>Job hires rate</td></tr>
                    <tr><td><code>'WAGE'</code></td> <td>Wages/Earnings</td></tr>
                    <tr><td><code>'WAGEMAN'</code></td> <td>Hourly wage manufacturing</td></tr>
                    <tr><td><code>'EMP'</code></td> <td>Total employment</td></tr>
                    <tr><td><code>'ACPOP'</code></td> <td>Active population</td></tr>
                    <tr><td><code>'PAY'</code></td> <td>Total payroll</td></tr>
                    <tr><td><code>'EMRATIO'</code></td> <td>Employment to working age population</td></tr>
                    <tr><td><code>'PART'</code></td> <td>Participation rate</td></tr>
                    <tr><td><code>'CLAIMS'</code></td> <td>Weekly unemployment insurance claims</td></tr>
                    <tr><td><code>'RETA'</code></td> <td>Retail trade</td></tr>
                    <tr><td><code>'IP'</code></td> <td>Industrial production</td></tr>
                    <tr><td><code>'CP'</code></td> <td>Construction production</td></tr>
                    <tr><td><code>'INVER'</code></td> <td>Investment rate</td></tr>
                    <tr><td><code>'SENT'</code></td> <td>Sentiment index</td></tr>
                    <tr><td><code>'CONF'</code></td> <td>Consumer confidence index</td></tr>
                    <tr><td><code>'UTIL'</code></td> <td>Utilization rate</td></tr>
                    <tr><td><code>'DWPE'</code></td> <td>Dwelling permits</td></tr>
                    <tr><td><code>'NFCI'</code></td> <td>Non-financial corporations investment rate</td></tr>
                    <tr><td><code>'CAR'</code></td> <td>Passenger car sales</td></tr>
                    <tr><td><code>'ELE'</code></td> <td>Production electricity</td></tr>
                    <tr><td><code>'ARIV'</code></td> <td>Tourist arrivals</td></tr>
                    <tr><td><code>'OIL'</code></td> <td>Oil production</td></tr>
                    <tr><td><code>'MANU'</code></td> <td>Manufacturing production</td></tr>
                    <tr><td><code>'CLI'</code></td> <td>OECD CLI</td></tr>
                    <tr><td><code>'TB'</code></td> <td>Trade balance</td></tr>
                    <tr><td><code>'NY'</code></td> <td>Net income from abroad (Primary Income)</td></tr>
                    <tr><td><code>'NCT'</code></td> <td>Net current transfers (Secondary Income)</td></tr>
                    <tr><td><code>'CA'</code></td> <td>Current account balance</td></tr>
                    <tr><td><code>'KA'</code></td> <td>Capital account</td></tr>
                    <tr><td><code>'CKA'</code></td> <td>Net foreign investment</td></tr>
                    <tr><td><code>'IIPA'</code></td> <td>International investment position: Assets</td></tr>
                    <tr><td><code>'IIPL'</code></td> <td>International investment position: Liabilities</td></tr>
                    <tr><td><code>'NIIP'</code></td> <td>Net international investment position</td></tr>
                    <tr><td><code>'EXPMON'</code></td> <td>Monthly exports</td></tr>
                    <tr><td><code>'IMPMON'</code></td> <td>Monthly imports</td></tr>
                    <tr><td><code>'GBAL'</code></td> <td>Government balance</td></tr>
                    <tr><td><code>'GSPE'</code></td> <td>General government total expenditure</td></tr>
                    <tr><td><code>'GREV'</code></td> <td>General government total revenue</td></tr>
                    <tr><td><code>'GDEBT'</code></td> <td>Government debt</td></tr>
                    <tr><td><code>'GDEBTN'</code></td> <td>Government net debt</td></tr>
                    <tr><td><code>'POP'</code></td> <td>Population</td></tr>
                    <tr><td><code>'HHS'</code></td> <td>Household saving</td></tr>
                    <tr><td><code>'HHDIR'</code></td> <td>Household debt to income ratio</td></tr>
                    <tr><td><code>'HOU'</code></td> <td>House price</td></tr>
                    <tr><td><code>'TFRT'</code></td> <td>Fertility rate</td></tr>
                    <tr><td><code>'LE00'</code></td> <td>Life expectancy at birth</td></tr>
                    <tr><td><code>'CRED'</code></td> <td>Domestic credit</td></tr>
                    <tr><td><code>'NFCLOAN'</code></td> <td>Lending to non-financial corporations</td></tr>
                    <tr><td><code>'PRIDEBT'</code></td> <td>Private debt</td></tr>
                    <tr><td><code>'NPL'</code></td> <td>Non performing loans</td></tr>
                    <tr><td><code>'MB'</code></td> <td>Monetary base</td></tr>
                    <tr><td><code>'M3'</code></td> <td>Money supply</td></tr>
                    <tr><td><code>'Y10YD'</code></td> <td>Long term yield</td></tr>
                    <tr><td><code>'M3YD'</code></td> <td>3 month yield</td></tr>
                    <tr><td><code>'IBD1'</code></td> <td>Interbank lending overnight rate</td></tr>
                    <tr><td><code>'POLIR'</code></td> <td>Policy rate - short term</td></tr>
                    <tr><td><code>'XUSD'</code></td> <td>Exchange rate v dollar</td></tr>
                    <tr><td><code>'SEI'</code></td> <td>Stock exchange index</td></tr>
                    <tr><td><code>'REER'</code></td> <td>Real effective exchange rate</td></tr>
                    <tr><td><code>'EQYCAP'</code></td> <td>Market capitalization</td></tr>
                    <tr><td><code>'OILPROD'</code></td> <td>Oil production</td></tr>
                    <tr><td><code>'OILDEM'</code></td> <td>Oil demand</td></tr>
                    <tr><td><code>'GASPROD'</code></td> <td>Gas production</td></tr>
                    <tr><td><code>'GASDEM'</code></td> <td>Gas demand</td></tr>
                    <tr><td><code>'GASOPROD'</code></td> <td>Gasoline production</td></tr>
                    <tr><td><code>'GASODEM'</code></td> <td>Gasoline demand</td></tr>
                </tbody>
            </table>
        </details>
    </li>
</ul>

## Widget
```python
from prognosis.widget import get_widget_data
get_widget_data("supermarket-country-index", {'country': 'US'})
```
### Methods
- <details><summary><code>get_widget_data(widget_name, opts)</code></summary>...</details>       
- <details><summary><code>get_widget_options(widget_name)</code></summary>...</details>       
- <details><summary><code>get_available_widgets()</code></summary>...</details>       

# License
MIT