# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:07:36 2022

@author: oriol
"""

import pandas as pd
from prognosis.helper import get
from prognosis.com import topic_tickers, topic_df


topics = topic_df['code'].tolist()


class CountryGroup():
    def __init__(self, country_list):
        self.country_list = country_list

    def get_topic(self, name):
        assert name in topics, 'Choose among %s' % str(topics)
        codes = [name+x for x in self.country_list]
        return get(codes)
