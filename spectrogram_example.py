# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:39:26 2024

@author: finazzi
"""

import pyaudio  
import wave  
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram
  
#define stream chunk - Loads some samples   

chunk = 130E3
  
#open a wav format music  
f = wave.open("./sample.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
 
#read data - format: binary string
data = f.readframes(chunk)  

# converts binary string to int16 amplitude
data_amp = np.frombuffer(data, np.int16)

# Compute the spectrogram
frequencies, times, Sxx = spectrogram(data_amp, f.getframerate())

# Plot the spectrogram
plt.figure(1)
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
plt.colorbar(label='dB')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.title('Spectrogram of audio file')
plt.tight_layout()



