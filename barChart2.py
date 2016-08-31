# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 21:28:39 2016

@author: JEEWOOYOON
"""

import matplotlib.pyplot as plt
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10*10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],histogram.values(),8)

plt.axis([-5,105,0,5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distributions of Exam 1 Grades")
plt.show()