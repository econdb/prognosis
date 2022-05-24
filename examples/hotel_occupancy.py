# -*- coding: utf-8 -*-


from prognosis.widget import get_widget_data

widget_name = 'hotel-occupancy'
df = get_widget_data(widget_name, {'country': 'DE'})
