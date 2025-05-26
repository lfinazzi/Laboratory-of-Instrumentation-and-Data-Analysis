# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:49:12 2024

@author: lucas
"""

import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt

def GetWaveform(osc, ch):
    osc.write("WFSU SP, 1, NP, 0, FP, 1") # waveform format set-up
    time.sleep(0.1)     # sleep to not hang the communication channel

    if ch == 2:
        osc.write("C2:WF? DAT2")
        time.sleep(0.1)
        wf = osc.read_raw()[21:-2]        
        
        raw_y_offset = osc.query("C2:OFFSET?")
        y_off = float((raw_y_offset.split(' ')[1]).split('V')[0])

        raw_y_scale = osc.query("C2:VOLT_DIV?")
        y_scale = float((raw_y_scale.split(' ')[1]).split('V')[0])
    
    elif ch == 1:
    # 
        osc.write("C1:WF? DAT2") # request channel data
        time.sleep(0.1)
        wf = osc.read_raw()[21:-2]
        raw_y_offset = osc.query("C1:OFFSET?")
        y_off = float((raw_y_offset.split(' ')[1]).split('V')[0])

        raw_y_scale = osc.query("C1:VOLT_DIV?")
        y_scale = float((raw_y_scale.split(' ')[1]).split('V')[0])
        
     # read data removing header and footer

    wvf = [] # creates output list
    for i in range(len(wf)):
        if (wf[i] > 127):
            wvf.append(int(wf[i]) - 255)
        else:
            wvf.append(int(wf[i]))
            
    wvf = [i * (y_scale/25) - y_off for i in wvf] # Formula to conver (found in manual)
    
    timebase = osc.query("TDIV?")
    timebase = float((timebase.split(' ')[1]).split('s')[0])

    tot_time = 20 * timebase #el 20 es especifico de este osc
    time = [i * tot_time / len(wvf) - tot_time/2 for i in range(len(wvf))]
    
    # returns calibrated x, y for respective waveform
    return time, wvf
    

#%% Get resources

rm = visa.ResourceManager()

# Lists all resources in machine
rm.list_resources() #use this to get equipment name

#%% Open resource and request waveform

osc = rm.open_resource("")

osc.query("*IDN?")
osc.write("*RST?")

# get waveform from channel 1
x, y = GetWaveform(osc, 1)


plt.figure(1)
plt.clf()
plt.plot(x, y)

osc.close()



    

    
    
