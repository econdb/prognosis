# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:05:10 2022

@author: oriol
"""

country = 'FR'

# Average room availability and prices by week
hotel_data = get_widget_data('hotel-occupancy', {'country': country})


# Average temperatures and rain by month
weather_data = get_widget_data('weather-observations', {'country': country})


# Supermarket prices vs CPI and food price Index (if available)
supermarket_data = get_widget_data(
    'supermarket-benchmark', {'country': country})
