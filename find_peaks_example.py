#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:25:03 2024

@author: finazzi
"""

import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import scipy.stats as stats

def Gaus(x, A, mu, sigma):
    return A / np.sqrt(2*np.pi*sigma**2) * np.exp(-(x - mu)**2 / 2 / sigma**2)


noise_sigma = 0.1

x = np.linspace(0, 10, 100)
y = [ Gaus(x[i], 4, 4, 1) + Gaus(x[i], 5, 7, 0.5) + stats.norm.rvs(0, noise_sigma) for i in range(len(x)) ]

plt.figure(1)
plt.clf()
plt.plot(x, y)

#%% Find peaks with default arguments! Doesn't work properly with noise!

pks = find_peaks(y)[0]

for l in pks:
    plt.scatter(x[l], y[l])


#%% Find peaks with custom arguments - works properly


plt.figure(2)
plt.clf()
plt.plot(x, y)


pks = find_peaks(y, height=1, width=10)[0]

for l in pks:
    plt.scatter(x[l], y[l])
    
    
print("----------First peak-----------")
print(f"index: {pks[0]}")
print(f"x-position: {round(x[pks[0]], 1)}")
print(f"amplitude: {round(y[pks[0]], 1)}")
print("")

print("----------Second peak-----------")
print(f"index: {pks[1]}")
print(f"x-position: {round(x[pks[1]], 1)}")
print(f"amplitude: {round(y[pks[1]], 1)}")





