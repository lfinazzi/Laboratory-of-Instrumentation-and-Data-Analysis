#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:00:16 2024

@author: finazzi
"""

#imports
import numpy as np

# define three lists
x = [1, 2, 3, 4, 5, 6, 7]
y = [ 3*i for i in x ]
z = [ i + 3 for i in y ]



#%% use numpy savetxt to save these lists to a .txt file
path = "./test.txt"
np.savetxt(path, np.c_[x, y, z], header="# x [Adim.]    y [Adim.]   z [Adim.]")

#%% use numy loadtxt to load same .txt file to memory

u, v, w = np.loadtxt(path, skiprows=1, unpack=True)
           

#%%