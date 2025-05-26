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

#☺ linear function (to see goodness of fit when fit is wrong...)
def Quad(M, x):
    return M[0] + M[1]*x + M[2]*x**2
    

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
odr.set_job(2)      # use this if you are only fitting with y-errors
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


#%% goodness of fit parameters

fit_params = 3
dof = (len(y) - fit_params) # degrees of freedom 
chi2 = out.res_var * dof    # chi2 --> approaches dof when fit is good

pvalue = 1 - stats.chi2.cdf(chi2, df=dof)

print("----------Correct fit--------------")
print("Fitted parameters:", out.beta)
print("Parameter errors:", out.sd_beta)
print(f"Chi-square / dof: {chi2} / {dof}")
print("P-value:", pvalue)
print("\n")


#%% now we fit a linear function (wrong fit)

# creates the model to fit
model = Model(Quad)

# creates the ODR object to fit
odr = ODR(data, model, beta0=[0.,0.,0.])

# performs the fit
odr.set_job(2)      # use this if you are only fitting with y-errors
out = odr.run()


plt.figure(2)
plt.clf()
plt.errorbar(x, y, yerr=sigma, fmt='.', color='k', label="raw data")
plt.plot(x, Quad(out.beta, x), linewidth=3, label="fit")
plt.xlabel("X [Adim.]", size=14)
plt.ylabel("Y [Adim.]", size=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)
plt.tight_layout()


#%% goodness of fit parameters

fit_params = 3
dof = (len(y) - fit_params) # degrees of freedom 
chi2 = out.res_var * dof    # chi2 --> approaches dof when fit is good

pvalue = 1 - stats.chi2.cdf(chi2, df=dof)


print("----------Wrong fit--------------")
print("Fitted parameters:", out.beta)
print("Parameter errors:", out.sd_beta)
print(f"Chi-square / dof: {chi2} / {dof}")
print("P-value:", pvalue)








