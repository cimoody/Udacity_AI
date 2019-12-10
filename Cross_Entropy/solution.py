# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:03:24 2019

@author: crist
"""

import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))