# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:12:59 2024

@author: finazzi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mu = 2
sigma = 0.5

# Parameters
num_samples = 10000
avg_samples = 3

norm_samples = np.random.normal(loc=mu, scale=sigma, size=(num_samples, avg_samples))

# Plot the Gaussian fit and the sum
plt.figure(1)
plt.clf()
# have to transpose to get num_samples events
plt.hist(norm_samples.transpose()[0], bins=50)
plt.xlabel('Value', size=14)
plt.ylabel('Probability', size=14)
plt.xticks(size=14)
plt.yticks(size=14)

averages = np.sum(norm_samples, axis=1)
averages /= avg_samples
plt.hist(averages, bins=50)

print(f"Normal samples mu: {mu}")
print(f"Normal samples mu: {sigma}")
print(f"Calculated mean: {np.mean(averages)}")
print(f"Theoretical mean std. dev.: {sigma / np.sqrt(avg_samples)}")
print(f"Calculated mean std. dev.: {np.std(averages)}")
