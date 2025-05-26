# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:58:56 2024

@author: lucas
"""

# imports
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# histogram characteristics
bins = 30
mu = 4
sigma = 0.5
num_samples = 10000

# generate bins of histogram
bins = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)

# generate gaussian random variables
p = stats.norm.rvs(scale=sigma, loc=mu, size=num_samples)

# convert histogram to errorbar plot (x-axis = bins and y-axis = hist)
hist, bins = np.histogram(p, bins=bins)

# half the bin width
bin_width = (bins[1] - bins[0]) / 2

# this calculation is done so points are plotted in the middle of histogram bin
bins_c = [ i + bin_width for i in bins[:-1] ]

# Plot of histogram and equivalent errorbar plot (that we can fit)
plt.figure(1)
plt.clf()
plt.hist(p, bins=bins)
plt.errorbar(bins_c, hist, yerr=np.sqrt(hist), color="k", fmt='.')
plt.xlabel("x [Adim.]")
plt.ylabel("Entries [Adim.]")