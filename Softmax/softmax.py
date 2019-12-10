# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:53:45 2019

@author: crist
"""

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    num = np.exp(L)
    dem = num.sum()
    softmax = []
    for i in range(len(L)):
        softmax.append(1.0*num[i]/dem)
        print(i+1, num[i], dem, softmax[i])
    return softmax

softmax([5,6,7])