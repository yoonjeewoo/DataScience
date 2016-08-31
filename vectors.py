# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:47:33 2016

@author: JEEWOOYOON
"""

from functools import partial

def vector_add(v,w) :
    return [v_i + w_i for v_i, w_i in zip(v, w)]
    
def vector_subtract(v,w) :
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum_1(vectors) :
    result = vectors[0]
    for vector in vectors[1:] :
        result = vector_add(result, vector)
    return result
    
def vector_sum_2(vectors) :
    return reduce(vector_add, vectors)
    
def scalar_multiply(c, v) :
    return [c * v_i for v_i in v]

def vector_mean(vectors) :
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum_2(vectors))

def dot(v, w) :
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v) :
    return dot(v, v)
    
import math

def magnitude(v) :
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w) :
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w) :
    return magnitude(vector_subtract(v, w))
