# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:36:36 2024

@author: finazzi
"""

#%% includes
import scipy.stats as stats
from scipy.odr import RealData, Model, ODR
import numpy as np
import matplotlib.pyplot as plt


#☺ linear function (to see goodness of fit when fit is wrong...)
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


# creates the model to fit
model = Model(Function)

chi2_h = []
iterations = 1000   # >1000 takes a while!
fit_params = 3
for i in range(iterations):     # will fit many times to see chi2 and pvalue distributions

    y = []
    # generate data in every iteration
    for i in x:
        y.append(Function(M_gen, i) + stats.norm.rvs(loc=0, scale=sigma)) 

    # creates the data object to use in the fit
    data = RealData(x, y, sy=sigma)

    # creates the ODR object to fit
    odr = ODR(data, model, beta0=[0.,0.,0,])

    # performs the fit
    odr.set_job(2)      # use this if you are only fitting with y-errors
    out = odr.run()

    dof = (len(y) - fit_params) # degrees of freedom 
    chi2 = out.res_var * dof    # chi2 --> approaches dof when fit is good
    
    chi2_h.append(chi2)


#%% plots the distribution

# define bins for chi2 histogram
bins = np.linspace(dof - 4*np.sqrt(2*dof), dof + 4*np.sqrt(2*dof), 100)

# we plot the data along with a chi2 distribution with dof degrees of freedom
# (not a fit)
plt.figure(1)
plt.clf()
plt.hist(chi2_h, bins=bins, density=True, label="data")
plt.plot(bins, stats.chi2.pdf(bins, df=dof), color="red", label=r"$\chi^2$ dist", linewidth=3)
plt.xlabel(r"$\chi^2$ [Adim.]", size=14)
plt.ylabel("Entries [Adim.]", size=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)
plt.tight_layout()

