# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:17:07 2016

@author: JEEWOOYOON
"""

import random 

def random_kid():
    return random.choice(["boy","girl"])
both_girls = 0
older_girl = 0
either_girl = 0
random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1
print both_girls
print older_girl
print either_girl

print "P(both | older): ", float(both_girls) / float(older_girl)
print "P(both | either):", float(both_girls) / float(either_girl)