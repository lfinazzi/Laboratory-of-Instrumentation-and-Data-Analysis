# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:58:36 2024

@author: finazzi
"""

#%% includes

import pyvisa as visa

# python library for easy plotting
from matplotlib import pyplot as plt

#%%

rm = visa.ResourceManager()

# Lists all resources in machine
rm.list_resources()

# Open the resource
osc = rm.open_resource("")

# Identity of resource and reset
osc.query("*IDN?")
osc.write("*RST?")

#%% Measures preamble

# Voltage scale - CH1
raw_y_scale = osc.query("C1:VOLT_DIV?")
 
# Voltage offset - CH1
raw_y_offset = osc.query("C1:OFFSET?")

# sampling rate
sampling_rate = osc.query("SARA?")

# horizontal scale
raw_x_scale = osc.query("TDIV?")

# horizontal offset - CH1
raw_x_offset = osc.query("TRDL?")

#%%

# page 142 of programming manual
osc.write("WFSU SP,0,NP,0,FP,0")    # waveform format
osc.write("C1:WF? DAT2")            # write waveform read request for CH1
wf = osc.read_raw()                 # reads waveform

record_length = wf[12:21]           # how long is the returned waveform
start_data = 21                     # start byte of data

# plots the raw returned waveform        
plt.figure(1)
plt.plot(wf)
plt.xlabel("Measurement number")
plt.ylabel("Amplitude [arb. u.]")

#%% 

#%%

osc.close()
