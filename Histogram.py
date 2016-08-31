# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:01:15 2016

@author: JEEWOOYOON
"""

from matplotlib import pyplot as plt
from collections import Counter
#from __future__ import division

num_friends = [100, 49, 41, 40, 25, 32, 64, 75, 32, 61, 60, 12, 4, 0, 10 ,10, 75, 40, 41, 41, 100]

friends_counts = Counter(num_friends)
"""
print friends_counts[41]
xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 5])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
"""
num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

def median(v):
    """v의 중앙값을 반환"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    
    if n%2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint 
        return (sorted_v[lo] + sorted_v[hi]) / 2

print median(num_friends)

def quantile(x, p):
    """x의 p분위에 속하는 값을 반환"""
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def mode(x):
    """최빈값이 하나보다 많다면 list를 반환"""
    counts = Counter(x)
    max_count = max(counts.values())ㅁ
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]
print mode(num_friends)

def data_range(x):
    return max(x)-min(x)

print data_range(num_friends)

def mean(x):
    return sum(x)/len(x)
    
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squares(xs):
    ans = 0
    for x in xs:
        ans = (x*x) + ans
    return ans
#print sum_of_squares([1,2,3])
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    #print deviations, "\n"
    #print sum_of_squares(deviations)
    return sum_of_squares(deviations) / (n - 1)
#print variance(num_friends)
    
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
    
