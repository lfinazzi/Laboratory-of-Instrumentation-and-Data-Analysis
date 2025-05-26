# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:30:53 2024

@author: lucas
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:12:59 2024

@author: lucas
"""

#%% includes
import scipy.stats as stats
from scipy.odr import RealData, Model, ODR
import numpy as np
import matplotlib.pyplot as plt


# exponential function
def Function(M, x):
    return M[0] + M[1]*np.exp(-M[2]*x)
    

#%% Data generation

# data M to generate datapoints
M_gen = [1, 4, 0.4]

# gaussian uncertainty
sigma = 0.2

x = []
y = []

x_start = 0
x_end = 10

x = np.linspace(x_start, x_end, 100)

# append exponential function + gaussian uncertainty
for i in x:
    y.append(Function(M_gen, i) + stats.norm.rvs(loc=0, scale=sigma)) 

#plt.errorbar(x, y, yerr=sigma, fmt='.', color='k')


#%% now we fit

# creates the model to fit
model = Model(Function)

# creates the data object to use in the fit
data = RealData(x, y, sy=sigma)

# creates the ODR object to fit
odr = ODR(data, model, beta0=[0.,0.,0,])

# performs the fit
out = odr.run()


plt.figure(1)
plt.clf()
plt.errorbar(x, y, yerr=sigma, fmt='.', color='k', label="raw data")
plt.plot(x, Function(out.beta, x), linewidth=3, label="fit")
plt.xlabel("X [Adim.]", size=14)
plt.ylabel("Y [Adim.]", size=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)
plt.tight_layout()

print(f"Real M0: {M_gen[0]}")
print(f"Real M1: {M_gen[1]}")
print(f"Real M2: {M_gen[2]}")
print(f"Fit obtained M0: {out.beta[0]} pm {np.sqrt(out.cov_beta[0][0])}")
print(f"Fit obtained M1: {out.beta[1]} pm {np.sqrt(out.cov_beta[1][1])}")
print(f"Fit obtained M2: {out.beta[2]} pm {np.sqrt(out.cov_beta[2][2])}")




