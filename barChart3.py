# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 21:50:08 2016

@author: JEEWOOYOON
"""

from matplotlib import pyplot as plt

metions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], metions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.show()