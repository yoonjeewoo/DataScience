# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:37:10 2016

@author: JEEWOOYOON
"""

from matplotlib import pyplot as plt

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades,test_2_grades)
plt.title("Axes are not Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.axis("equal")
plt.show()