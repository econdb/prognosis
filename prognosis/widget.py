# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:09:46 2022

@author: oriol
"""

import pandas as pd
import requests
from io import BytesIO

domain = 'https://www.econdb.com'


def get_available_widgets():
    return requests.post(
        domain + '/widgets/',
        json={'path': 'prognosis', 'args': []}).json()


def get_widget_options(widget_name):
    return requests.get(
        '%s/widgets/%s/options/' % (domain, widget_name)).json()


def get_widget_data(widget_name, opts):
    buff = BytesIO(requests.get(
        '%s/widgets/%s/data/' % (domain, widget_name),
        params={'format': 'csv', **opts}).content)
    buff.seek(0)
    df = pd.read_csv(buff)
    buff.close()
    return df
