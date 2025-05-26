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
awg = rm.open_resource("")

# Resource identity and reset - IEEE-488.2 standard
awg.query("*IDN?")
awg.write("*RST?")

# Select sine function for output
awg.write("C1:BSWV WVTP,SINE")

#%%

#%%

# Close the resource
awg.close()
