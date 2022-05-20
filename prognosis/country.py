# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:30:58 2022

@author: oriol
"""

import pandas as pd
from prognosis.helper import get


groups = {
    'national_accounts':
        ['RGDP%s', 'RPRC%s', 'RPUC%s', 'RGFCF%s', 'REXP%s','RIMP%s'],
    'prices': ['CPI%s', 'PPI%s'],
    'government': ['GSPE%s', 'GREV%s', 'GBAL%s', 'GDEBT%s'],
    'monthly_trade': ['EXPMON%s', 'IMPMON%s'],
    'yield_curve': ['M3YD%s', 'Y10YD%s'],
    'retail_sales': ['RETA%s'],
    'ip': ['IP%s'],
}


class Country():
    def __init__(self, country_code):
        self.country_code = country_code

    def get_group(self, name):
        codes = [x % self.country_code for x in groups[name]]
        return get(codes)

    def national_accounts(self):
        return self.get_group('national_accounts')

    def prices(self):
        return self.get_group('prices')

    def monthly_trade(self):
        return self.get_group('monthly_trade')

    def government_accounts(self):
        return self.get_group('government')

    def yield_curve(self):
        return self.get_group('yield_curve')

    def retail_sales(self):
        return self.get_group('retail_sales')

    def ip(self):
        return self.get_group('ip')
