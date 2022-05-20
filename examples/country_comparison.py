# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:17:10 2022

@author: oriol
"""


from prognosis import CountryGroup

group = CountryGroup(['ES', 'DE'])

ip = group.get_topic('IP')

ip.plot()
