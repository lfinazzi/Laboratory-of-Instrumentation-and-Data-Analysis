# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:02:06 2024

@author: finazzi
"""

import pyvisa as visa

rm = visa.ResourceManager()

# Lists all resources in machine
rm.list_resources()

# Open the resource
awg = rm.open_resource("USB0::0xF4ED::0xEE3A::SDG08BAQ1R0795::INSTR")

# Identity of resource and reset
awg.query("*IDN?")
awg.write("*RST?")

# Select function to output
awg.write("C1:BSWV WVTP,SINE")
awg.write("C1:BSWV WVTP,SQUARE")

# Select frequency 
awg.write("C1:BSWV FRQ,40E3")

# Read AWG config
awg.query("C1:BSWV?")

# Select amplitude and offset
awg.write("C1:BSWV AMP,2")
awg.write("C1:BSWV OFST,0.02")

# Select phase (degrees)
awg.write("C1:BSWV PHSE,15")
    
# Output ON or OFF
awg.write("C1:OUTput ON")
awg.write("C1:OUTput OFF")

# Close the resource
awg.close()
