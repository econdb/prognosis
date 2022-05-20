# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from prognosis.com import country_df
from prognosis import Country


for ix, row in country_df[country_df['name'].isin(('Spain', 'Italy'))].iterrows():
    Country(row['iso2']).retail_sales().plot()
    plt.show()
