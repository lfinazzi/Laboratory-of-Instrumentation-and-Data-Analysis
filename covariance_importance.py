#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:50:21 2024

@author: finazzi
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# for fitting
from scipy.odr import ODR, RealData, Model

# define our fit model
def Linear(M, x):
    return M[0]*x + M[1]

# dataset to study
x = np.linspace(2, 3, 11)
y = [2.78, 3.29, 3.29, 3.33, 3.23, 3.69, 3.46, 3.87, 3.62, 3.4, 3.99]
y_err = 0.3

# syntax to create a model object, a data object and fit the data
model = Model(Linear)
data = RealData(x, y, sy=y_err)
odr = ODR(data, model, beta0=[0.,0.])
odr.set_job(fit_type=2)       # ordinary least squares
out = odr.run()

x_fit = np.linspace(0, 5, 50)

# plot all
plt.figure(1)
plt.clf()
plt.scatter(np.mean(x), np.mean(y), marker="s", color="red", label="Data mean")
plt.errorbar(x, y, yerr=y_err, fmt='o', label="data")
plt.plot(x_fit, Linear(out.beta, x_fit), label="Linear fit")
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.xlim(0, 5)
plt.grid(True)

yp = Linear(out.beta, x_fit)

# calculate errorbar of estimation without covariance
yp_wrong = [ np.sqrt( x_fit[i]**2 * out.cov_beta[0][0] + out.cov_beta[1][1] ) for i in range(len(x_fit)) ]

# calculate errorbar of estimation with covariance
yp_right = [ np.sqrt( x_fit[i]**2 * out.cov_beta[0][0] + out.cov_beta[1][1] + 2*x_fit[i]*out.cov_beta[0][1]) for i in range(len(x_fit)) ]

yp_low_wrong = [ yp[i] - yp_wrong[i]/2 for i in range(len(x_fit)) ]
yp_high_wrong = [ yp[i] + yp_wrong[i]/2 for i in range(len(x_fit)) ]
yp_low_right = [ yp[i] - yp_right[i]/2 for i in range(len(x_fit)) ]
yp_high_right = [ yp[i] + yp_right[i]/2 for i in range(len(x_fit)) ]


# plot the errorbars
plt.plot(x_fit, yp_low_wrong, "--", color="tab:green", label="Errorbars (wrong)")
plt.plot(x_fit, yp_high_wrong, "--", color="tab:green")
plt.plot(x_fit, yp_low_right, color="black", label="Errorbars (right)")
plt.plot(x_fit, yp_high_right, color="black")

# plot legend
plt.legend(fontsize=14)














#%%