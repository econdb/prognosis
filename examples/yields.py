# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:08:03 2022

@author: oriol
"""
import pandas as pd
from prognosis.helper import get, yahoo


# Daily yield - 10 year curve
usdyld = get('FRB_H15.37BF6.D.US', 'M')
usd3m = get('FRB_H15.4DCCD.M.US')
houus = get('HOUUS')
euryld = get('Y10YDDE')
gbpyld = get('Y10YDUK')
chyyld = get('Y10YDCN')
cpius = get('CPIUS')
cpicn = get('CPICN')
cpiuk = get('CPIUK')
cpiea = get('CPIEA')
eurusd = get('EURUSD')
gbpusd = get('GBPUSD')
usdcny = get('USDCNY')

impusd = get('IMPMONUS')
expusd = get('EXPMONUS')

oil = yahoo('CL=F')
gasoline = yahoo('RB=F')

m3us = get('M3US')
m3ea = get('M3DE')
gdpus = get('GDPUS')
gdebtus = get('GDEBTUS')


world_gdp = pd.read_csv('https://www.econdb.com/cross_section/GDP/',
                        index_col='ref_period', parse_dates=['ref_period'])
world_gdp = world_gdp.loc['2000-01-01':]
weights = (
    world_gdp.ffill().bfill().loc['2010-01-01'] /
    world_gdp.ffill().bfill().loc['2010-01-01'].sum())
wdgdp = (
    world_gdp.ffill().sum(axis=1) /
    (world_gdp.ffill().notnull() * weights).sum(axis=1))
ex_us = (wdgdp-gdpus['GDPUS']/4).dropna()
ex_us *= 4

dollar_adj_gdp = (gdpus['GDPUS'] + 0.1 * ex_us).dropna()

velocity = (dollar_adj_gdp/m3us['M3US']).dropna().to_frame(name='v')
usdyld = usdyld

inflation = cpius.pct_change(12)*100

(
velocity.join(
    (gdebtus['GDEBTUS']/gdpus['GDPUS']*10).to_frame(name='debt'))
.join(inflation).join((gdpus.pct_change(4)*100).dropna())
.join(usdyld).plot(secondary_y='v', figsize=(12, 8))
)

chm3 = (m3us.pct_change(12)*100).dropna()#usdyld
1 / ((usd3m + 4)/100)

real = (usd3m['FRB_H15.4DCCD.M.US'] - inflation['CPIUS']).to_frame(name='REAL')

df = inflation.join((gdpus.pct_change(4)*100).dropna()).join(chm3).join(usd3m).loc[pd.Timestamp('2000-01-01'):].dropna()
