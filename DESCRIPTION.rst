Prognosis
============

The mission of the company is to process information in ways that
facilitate understanding of the economic situation|at different
granularity levels.

The sources of data include official statistics agencies|and so-called
alternative data sources|where we collect direct observations of the
market and generate aggregate statistics.

Econdb Ltd. is a limited company registered in United Kingdom|with
company number 10759232.

Table of Contents
-----------------

-  `Introduction <#introduction>`__

   -  `Table of Contents <#table-of-contents>`__
   -  `Installation <#installation>`__
   -  `Quick examples <#quick-examples>`__

-  `Api reference <#api-reference>`__

   -  `Country <#country>`__

      -  `Available country codes <#available-country-codes>`__
      -  `Methods <#methods>`__

   -  `Country group <#country-group>`__

      -  `Available coutry groups <#available-coutry-groups>`__
      -  `Methods <#methods-1>`__

   -  `Widget <#widget>`__

      -  `Methods <#methods-2>`__

-  `License <#license>`__

Installation
------------

This Python module provides a wrapper around the API of Econdb.com.
You can also find Econdb on `Github <https://github.com/econdb/prognosis>`__
::

   pip install prognosis

Quick examples
--------------

Some examples are given below|to see more check
`examples <./examples>`__

.. code:: python

   from prognosis import Country
   germany = Country('DE')

   ### National Accounts
   nac = germany.national_accounts()

   ### Consumer and producer prices
   prices = germany.prices()

   ### Government accounts
   gov = germany.government_accounts()

Api reference
=============

Country
-------

.. code:: python

   from prognosis import Country
   germany = Country('DE')

Available country codes
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <details> 
   <summary> Countries </summary> 

============================ ========
**Country**                  **Code**
============================ ========
Albania                      ``'AL'``
Algeria                      ``'DZ'``
Angola                       ``'AO'``
Argentina                    ``'AR'``
Australia                    ``'AU'``
Austria                      ``'AT'``
Azerbaijan                   ``'AZ'``
Bangladesh                   ``'BD'``
Belarus                      ``'BY'``
Belgium                      ``'BE'``
Bolivia                      ``'BO'``
Bosnia And Herzegovina       ``'BA'``
Brazil                       ``'BR'``
Bulgaria                     ``'BG'``
Cambodia                     ``'KH'``
Canada                       ``'CA'``
Chile                        ``'CL'``
China                        ``'CN'``
Colombia                     ``'CO'``
Costa Rica                   ``'CR'``
Croatia                      ``'HR'``
Cyprus                       ``'CY'``
Czechia                      ``'CZ'``
Democratic Republic Of Congo ``'CD'``
Denmark                      ``'DK'``
Dominican Republic           ``'DO'``
Ecuador                      ``'EC'``
Egypt                        ``'EG'``
El Salvador                  ``'SV'``
Estonia                      ``'EE'``
Ethiopia                     ``'ET'``
European Union               ``'EU'``
Finland                      ``'FI'``
France                       ``'FR'``
Germany                      ``'DE'``
Ghana                        ``'GH'``
Greece                       ``'GR'``
Guatemala                    ``'GT'``
Honduras                     ``'HN'``
Hong Kong                    ``'HK'``
Hungary                      ``'HU'``
India                        ``'IN'``
Indonesia                    ``'ID'``
Iran                         ``'IR'``
Iraq                         ``'IQ'``
Ireland                      ``'IE'``
Israel                       ``'IL'``
Italy                        ``'IT'``
Japan                        ``'JP'``
Jordan                       ``'JO'``
Kazakhstan                   ``'KZ'``
Kenya                        ``'KE'``
Kuwait                       ``'KW'``
Kyrgyzstan                   ``'KG'``
Laos                         ``'LA'``
Latvia                       ``'LV'``
Lebanon                      ``'LB'``
Libya                        ``'LY'``
Lithuania                    ``'LT'``
Luxembourg                   ``'LU'``
Macao                        ``'MO'``
Malaysia                     ``'MY'``
Mexico                       ``'MX'``
Mongolia                     ``'MN'``
Morocco                      ``'MA'``
Myanmar                      ``'MM'``
Nepal                        ``'NP'``
Netherlands                  ``'NL'``
New Zealand                  ``'NZ'``
Nicaragua                    ``'NI'``
Nigeria                      ``'NG'``
Norway                       ``'NO'``
Oman                         ``'OM'``
Pakistan                     ``'PK'``
Panama                       ``'PA'``
Paraguay                     ``'PY'``
Peru                         ``'PE'``
Philippines                  ``'PH'``
Poland                       ``'PL'``
Portugal                     ``'PT'``
Qatar                        ``'QA'``
Romania                      ``'RO'``
Russian Federation           ``'RU'``
Saudi Arabia                 ``'SA'``
Senegal                      ``'SN'``
Serbia                       ``'RS'``
Singapore                    ``'SG'``
Slovakia                     ``'SK'``
Slovenia                     ``'SI'``
South Africa                 ``'ZA'``
South Korea                  ``'KR'``
Spain                        ``'ES'``
Sri Lanka                    ``'LK'``
Sudan                        ``'SD'``
Sweden                       ``'SE'``
Switzerland                  ``'CH'``
Taiwan                       ``'TW'``
Tajikistan                   ``'TJ'``
Tanzania                     ``'TZ'``
Thailand                     ``'TH'``
Tunisia                      ``'TN'``
Turkey                       ``'TR'``
Turkmenistan                 ``'TM'``
Ukraine                      ``'UA'``
United Arab Emirates         ``'AE'``
United Kingdom               ``'UK'``
United States                ``'US'``
Uruguay                      ``'UY'``
Uzbekistan                   ``'UZ'``
Venezuela                    ``'VE'``
Vietnam                      ``'VN'``
============================ ========

.. raw:: html

   </details>

Methods
~~~~~~~

+---------------------------+-----------------------------------------+
| **Method**                | **Description**                         |
+===========================+=========================================+
| ``prices()``              | Consumer and producer price index       |
+---------------------------+-----------------------------------------+
| ``monthly_trade()``       | Monthly imports and exports, in current |
|                           | prices                                  |
+---------------------------+-----------------------------------------+
| ``government_accounts()`` | Quarterly government accounts, in       |
|                           | current prices, and government debt     |
+---------------------------+-----------------------------------------+
| ``yield_curve()``         | 3 month and 10 year bond yields         |
+---------------------------+-----------------------------------------+
| ``retail_sales()``        | Monthly retail sales                    |
+---------------------------+-----------------------------------------+
| ``ip()``                  | Monthly industrial production           |
+---------------------------+-----------------------------------------+
| ``energy()``              | Oil, gas, and gasoline production and   |
|                           | demand. Data source: JODI.              |
+---------------------------+-----------------------------------------+
| ``national_accounts()``   | Quarterly national accounts in constant |
|                           | prices, by expenditure                  |
+---------------------------+-----------------------------------------+

Country group
-------------

.. code:: python

   from prognosis import CountryGroup
   africa = CountryGroup('Africa')
   custom_group = CountryGroup(['RU' 'US' 'CN'])

Available coutry groups
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <details>
   <summary>Groups</summary>

+----------------------+----------------------------------------------+
| **Group**            | **Included country codes**                   |
+======================+==============================================+
| ``'Africa'``         | ['DZ' 'AO' 'CD' 'EG' 'ET' 'GH' 'KE' 'LY'     |
|                      | 'MA' 'NG' 'SN' 'ZA' 'SD' 'TZ' 'TN']          |
+----------------------+----------------------------------------------+
| ``'Central Asia'``   | ['AZ' 'KZ' 'KG' 'MN' 'TJ' 'TM' 'UZ']         |
+----------------------+----------------------------------------------+
| ``'East Asia'``      | ['CN' 'HK' 'JP' 'KR' 'MO' 'TW']              |
+----------------------+----------------------------------------------+
| ``'Europe'``         | ['AL' 'AT' 'BY' 'BE' 'BA' 'BG' 'HR' 'CY'     |
|                      | 'CZ' 'DK' 'EE' 'FI' 'FR' 'DE' 'GR' 'HU' 'IE' |
|                      | 'IT' 'LV' 'LT' 'LU' 'NL' 'NO' 'PL' 'PT' 'RO' |
|                      | 'RU' 'RS' 'SK' 'SI' 'ES' 'SE' 'CH' 'TR' 'UA' |
|                      | 'EU' 'UK']                                   |
+----------------------+----------------------------------------------+
| ``'G20'``            | ['AR' 'AU' 'BR' 'CA' 'CN' 'FR' 'DE' 'IN'     |
|                      | 'ID' 'IT' 'JP' 'KR' 'MX' 'RU' 'SA' 'ZA' 'TR' |
|                      | 'US' 'EU' 'UK']                              |
+----------------------+----------------------------------------------+
| ``'Latin America'``  | ['AR' 'BO' 'BR' 'CL' 'CO' 'CR' 'DO' 'EC'     |
|                      | 'SV' 'GT' 'HN' 'NI' 'PA' 'PY' 'PE' 'UY'      |
|                      | 'VE']                                        |
+----------------------+----------------------------------------------+
| ``'Middle East'``    | ['IR' 'IQ' 'IL' 'JO' 'KW' 'LB' 'OM' 'QA'     |
|                      | 'SA' 'AE']                                   |
+----------------------+----------------------------------------------+
| ``'North America'``  | ['CA' 'MX' 'US']                             |
+----------------------+----------------------------------------------+
| ``'Oceania'``        | ['AU' 'NZ']                                  |
+----------------------+----------------------------------------------+
| ``'South Asia'``     | ['BD' 'IN' 'NP' 'PK' 'LK']                   |
+----------------------+----------------------------------------------+
| ``'Southeast Asia'`` | ['KH' 'ID' 'LA' 'MY' 'MM' 'PH' 'SG' 'TH'     |
|                      | 'VN']                                        |
+----------------------+----------------------------------------------+

.. raw:: html

   </details>

.. _methods-1:

Methods
~~~~~~~

.. raw:: html

   <ul>    
   <li>
   <details>
   <summary><code>get_topic(topic)</code></summary>
   <br>
   Available topics

============== ==============================================
**Topic**      **Desctiption**
============== ==============================================
``'GDP'``      Gross domestic product
``'PRC'``      Private consumption
``'PUC'``      Public consumption
``'CON'``      Total consumption
``'GCF'``      Gross capital formation
``'GFCF'``     Gross fixed capital formation
``'CI'``       Change in inventories
``'CBAL'``     Commercial balance (goods + services)
``'EXP'``      Exports of goods and services
``'IMP'``      Imports of goods and services
``'PI'``       Personal income
``'RGDP'``     Real gross domestic product
``'RPRC'``     Real private consumption
``'RPUC'``     Real public consumption
``'RCON'``     Real total consumption
``'RGCF'``     Real gross capital formation
``'RGFCF'``    Real gross fixed capital formation
``'RCI'``      Real change in inventories
``'REXP'``     Real exports of goods and services
``'RIMP'``     Real imports of goods and services
``'GDPPC'``    GDP per capita
``'RGDPPC'``   Real GDP per capita
``'GDPD'``     GDP (current US dollars)
``'GDPDEF'``   GDP deflator
``'CPI'``      Consumer price index
``'CORE'``     Core consumer price index
``'PPI'``      Producer price index
``'URATE'``    Unemployment
``'JVR'``      Job vacancy rate
``'JQR'``      Job quits rate
``'JLR'``      Job layoffs rate
``'JHR'``      Job hires rate
``'WAGE'``     Wages/Earnings
``'WAGEMAN'``  Hourly wage manufacturing
``'EMP'``      Total employment
``'ACPOP'``    Active population
``'PAY'``      Total payroll
``'EMRATIO'``  Employment to working age population
``'PART'``     Participation rate
``'CLAIMS'``   Weekly unemployment insurance claims
``'RETA'``     Retail trade
``'IP'``       Industrial production
``'CP'``       Construction production
``'INVER'``    Investment rate
``'SENT'``     Sentiment index
``'CONF'``     Consumer confidence index
``'UTIL'``     Utilization rate
``'DWPE'``     Dwelling permits
``'NFCI'``     Non-financial corporations investment rate
``'CAR'``      Passenger car sales
``'ELE'``      Production electricity
``'ARIV'``     Tourist arrivals
``'OIL'``      Oil production
``'MANU'``     Manufacturing production
``'CLI'``      OECD CLI
``'TB'``       Trade balance
``'NY'``       Net income from abroad (Primary Income)
``'NCT'``      Net current transfers (Secondary Income)
``'CA'``       Current account balance
``'KA'``       Capital account
``'CKA'``      Net foreign investment
``'IIPA'``     International investment position: Assets
``'IIPL'``     International investment position: Liabilities
``'NIIP'``     Net international investment position
``'EXPMON'``   Monthly exports
``'IMPMON'``   Monthly imports
``'GBAL'``     Government balance
``'GSPE'``     General government total expenditure
``'GREV'``     General government total revenue
``'GDEBT'``    Government debt
``'GDEBTN'``   Government net debt
``'POP'``      Population
``'HHS'``      Household saving
``'HHDIR'``    Household debt to income ratio
``'HOU'``      House price
``'TFRT'``     Fertility rate
``'LE00'``     Life expectancy at birth
``'CRED'``     Domestic credit
``'NFCLOAN'``  Lending to non-financial corporations
``'PRIDEBT'``  Private debt
``'NPL'``      Non performing loans
``'MB'``       Monetary base
``'M3'``       Money supply
``'Y10YD'``    Long term yield
``'M3YD'``     3 month yield
``'IBD1'``     Interbank lending overnight rate
``'POLIR'``    Policy rate - short term
``'XUSD'``     Exchange rate v dollar
``'SEI'``      Stock exchange index
``'REER'``     Real effective exchange rate
``'EQYCAP'``   Market capitalization
``'OILPROD'``  Oil production
``'OILDEM'``   Oil demand
``'GASPROD'``  Gas production
``'GASDEM'``   Gas demand
``'GASOPROD'`` Gasoline production
``'GASODEM'``  Gasoline demand
============== ==============================================

.. raw:: html

   </details>
   </li>
   </ul>

Widget
------

.. code:: python

   from prognosis.widget import get_widget_data
   get_widget_data("supermarket-country-index", {'country': 'US'})

.. _methods-2:

Methods
~~~~~~~

-  

   .. raw:: html

      <details><summary><code>get_widget_data(widget_name, opts)</code></summary>...</details>       

-  

   .. raw:: html

      <details><summary><code>get_widget_options(widget_name)</code></summary>...</details>       

-  

   .. raw:: html

      <details><summary><code>get_available_widgets()</code></summary>...</details>       

License
=======

MIT

.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/prognosis.svg
   :target: https://pypi.python.org/pypi/prognosis
