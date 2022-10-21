# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:07:36 2022

@author: oriol
"""

from prognosis.helper import get
from prognosis.com import topic_df, country_groups, country_df


topics = topic_df['code'].tolist()


class CountryGroup():
    def __init__(self, country_list):
        if isinstance(country_list, str):
            self.country_list = country_groups[country_list]
        else:
            assert isinstance(country_list, list)
            countries = country_df["iso2"].values
            for country in country_list:
                if not country in countries:
                    raise Exception("%s does not exist" % country)
            self.country_list = country_list

    def get_topic(self, name):
        assert name in topics, 'Choose among %s' % str(topics)
        codes = [name+x for x in self.country_list]
        return get(codes)
