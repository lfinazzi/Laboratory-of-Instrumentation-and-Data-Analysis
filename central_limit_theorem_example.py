# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:12:59 2024

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
num_samples = 1000000
num_uniform_distributions = 2  # Number of uniform distributions to sum
uniform_range = (-1, 1)  # Range of the uniform distributions

# Generate uniform distributions and sum them
uniform_samples = np.random.uniform(low=uniform_range[0], high=uniform_range[1], size=(num_samples, num_uniform_distributions))
gaussian_approximation = np.sum(uniform_samples, axis=1)

# gaussian fit on histogram
mu, std = norm.fit(gaussian_approximation)
x = np.linspace(mu - 3*std, mu + 3*std, 100)
p = norm.pdf(x, mu, std)

# Plot the Gaussian fit and the sum
plt.figure(1)
plt.clf()
plt.plot(x, p, linewidth=2, color="red", label="fit")
plt.hist(gaussian_approximation, bins=50, color='blue', alpha=0.7, density=True, label="data")
plt.xlabel('Value', size=14)
plt.ylabel('Probability Density', size=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)



# Plot the histogram of the Gaussian approximation
