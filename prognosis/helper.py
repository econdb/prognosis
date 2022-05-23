# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:51:35 2022

@author: oriol
"""

import pandas as pd
import time

series_endpoint = 'https://www.econdb.com/api/series/'

def get(code, freq=None):
    ts = pd.read_csv(
        '%s?ticker=[%s]&format=csv' %
        (series_endpoint, ','.join(code) if isinstance(code, list) else code),
        index_col='Date', parse_dates=['Date'])
    if freq == 'M':
        ts = ts.groupby(ts.index.map(lambda x: x.replace(day=1))).mean()
    return ts

def yahoo(code):
    ts = (
        pd.read_csv(
        'https://query1.finance.yahoo.com/v7/finance/download/%s?'
        'period1=1400000000&period2=%d&interval=1d&events=history'
        '&includeAdjustedClose=true' % (code, time.time() // 100 *100),
        date_parser='Date').set_index('Date')['Adj Close'])
    return ts
