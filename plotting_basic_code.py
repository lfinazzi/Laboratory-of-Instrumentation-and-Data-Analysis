# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:35:09 2024

@author: finazzi
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
y2 = [2, 4, 6, 8, 10]

x_err = 0.1
y_err = 1

# plot without errorbars

# creates a window labeled "1"
plt.figure(1)                 
# clears figure if a previous figure was in window "1"           
plt.clf()         
              
# plots x and y using round markers and blue color
plt.plot(x, y, 'o', color="tab:blue")    

# labels
plt.xlabel("x axis [units]", size=14)
plt.ylabel("y axis [units]", size=14)

# changes default size of plot ticks
plt.xticks(size=14)
plt.yticks(size=14)



# plot with errorbars

# creates a window labeled "2"
plt.figure(2)                 
# clears figure if a previous figure was in window "2"           
plt.clf()         
              
# plots x and y using round markers and blue color
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', color="tab:blue")    

# labels
plt.xlabel("x axis [units]", size=14)
plt.ylabel("y axis [units]", size=14)

# changes default size of plot ticks
plt.xticks(size=14)
plt.yticks(size=14)


# plots two curves with custom legend

plt.figure(3)                           
plt.clf()         
plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o', label="first")  
plt.errorbar(x, y2, yerr=y_err, fmt='o', label="second")   
plt.xlabel("x axis [units]", size=14)
plt.ylabel("y axis [units]", size=14)
plt.xticks(size=14)
plt.yticks(size=14)

# generates legend
plt.legend(fontsize=14)