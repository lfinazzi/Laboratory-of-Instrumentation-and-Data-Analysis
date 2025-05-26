# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:58:42 2024

@author: lucas
"""

import pyaudio  
import wave  
import matplotlib.pyplot as plt
import numpy as np
  
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

# plots the 
plt.figure()
plt.plot(data_amp)
plt.xlabel("Sample [Adim.]")
plt.ylabel("Amplitude [Adim.]")


"""excercises

    1. Calibrate imported signal time axis
    2. Use numpy to calculate FFT of audio and plot it
        link: https://numpy.org/doc/stable/reference/routines.fft.html
    3. Use scipy.signal to apply filter to data_amp vector
        link: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
    4. See/Listen to modified audio

"""


#%% plays modified audio

#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True) 
        
#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  
  
#stop stream  
stream.stop_stream()  
stream.close()  
  
#close PyAudio  
p.terminate()  
