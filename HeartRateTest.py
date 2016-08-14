# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 13:01:03 2016

@author: F041
"""

import matplotlib.pyplot  as plt
import matplotlib.dates  as mdates
import numpy as np
import pandas as pd

heartrate=np.loadtxt("C:\Users\F041\Desktop\HR.csv", 
                                     delimiter=",",
                                     usecols(1,))
