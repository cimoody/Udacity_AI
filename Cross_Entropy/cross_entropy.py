# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:59:59 2019

@author: crist
"""
import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    entropy_i = []
    for i in range(len(Y)):
        e_i = -1.0 * Y[i] * np.log(P[i]) - (1.0 - Y[i]) * np.log(1.0 - P[i])
        entropy_i.append(e_i)
    cross_entropy =  sum(entropy_i) 
    return(cross_entropy)


Y=[1,0,1,1] 
P=[0.4,0.6,0.1,0.5]
print(cross_entropy(Y, P))