# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:08:29 2022

@author: oriol
"""

topic_tickers = {
    'national_accounts':
        ['RGDP%s', 'RPRC%s', 'RPUC%s', 'RGFCF%s', 'REXP%s','RIMP%s'],
    'prices': ['CPI%s', 'PPI%s'],
    'government': ['GSPE%s', 'GREV%s', 'GBAL%s', 'GDEBT%s'],
    'monthly_trade': ['EXPMON%s', 'IMPMON%s'],
    'yield_curve': ['M3YD%s', 'Y10YD%s'],
    'retail_sales': ['RETA%s'],
    'ip': ['IP%s'],
    'energy':
        ['OILPROD%s', 'OILDEM%s', 'GASODEM%s', 'GASOPROD%s', 'GASDEM%s',
         'GASPROD%s'],
}
