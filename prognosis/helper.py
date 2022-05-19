# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:51:35 2022

@author: oriol
"""

import requests
import pandas as pd
import numpy as np
import time

def get(code):
    return pd.read_csv(
        'https://www.econdb.com/api/series/%s/?format=csv' % code,
        index_col='Date', parse_dates=['Date'])

def yahoo(code):
    ts = (
        pd.read_csv(
        'https://query1.finance.yahoo.com/v7/finance/download/%s?'
        'period1=1400000000&period2=%d&interval=1d&events=history'
        '&includeAdjustedClose=true' % (code, time.time() // 100 *100),
        date_parser='Date').set_index('Date')['Adj Close'])
    return ts
