# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:13:11 2016

@author: Daniele
"""

from __future__ import division
from scipy.stats.stats import pearsonr  
from scipy.ndimage.filters import gaussian_filter

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scisig
import math


GSRTdata=np.genfromtxt('test.txt',skip_header=0,delimiter=',',dtype=float, deletechars='\n')

media_GSR=0

GSR=[]
R=[]

contatore=0
for line in GSRTdata:
    gsr=float(line[0])
    temp=int(line[1])
    media_GSR+=gsr
    if contatore==3:
        GSR.append(media_GSR/(contatore+1))
        media_GSR=0        
        contatore=0
    else:
        contatore+=1
plt.close

GSRs=[]

if len(GSR)!=0:
    print len(GSR)
    GSRmax=max(GSR)
    for resistance in GSR:
        x=resistance/GSRmax
        GSRs.append(x)
if GSRs !=0:
    for value in GSRs:
        skinR=10**5            
        R.append(1/value)

GSR=gaussian_filter(GSR,sigma=5)

dGSR=[]
i=0
diff=0
while i<len(GSR)-1:
   diff=(GSR[i+1]-GSR[i])
   dGSR.append(diff)
   i+=1
   
#plt.plot(dGSR)
#plt.plot(dHR, marker='x',linewidth=0.7, mew=0.4, ms=3)

dGSR=gaussian_filter(dGSR,sigma=4)
GSRs=gaussian_filter(GSRs,sigma=4)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(GSR,label='GSR')

#ax1.plot(RRs,marker='o',label='RR',linewidth=0.3, mew=0.4, ms=3)
plt.legend(loc='upper right');
plt.show()