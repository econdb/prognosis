# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:47:31 2022

@author: oriol
"""

from prognosis.widget import get_widget_data

widget_name = 'contributions-to-gdp'
df = get_widget_data(widget_name, {'country': 'DE', 'freq': 'Q'})
