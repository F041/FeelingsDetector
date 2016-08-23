# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:13:11 2016

@author: F041
"""

from __future__ import division
from scipy.ndimage.filters import gaussian_filter  

def GSRdata(fileName,dGSR="n",GSRs="n"):
    import numpy as np
    import matplotlib.pyplot as plt
    GSRTdata=np.genfromtxt(fileName,skip_header=0,delimiter=',',dtype=float, deletechars='\n')
    media_GSR=0
    GSR=[]
    GSRs=[]
    contatore=0
    for line in GSRTdata:
        gsr=float(line[0])
        media_GSR+=gsr
        if contatore==3:
            GSR.append(media_GSR/(contatore+1))
            media_GSR=0        
            contatore=0
        else:
            contatore+=1
    if dGSR!="n":
        dGSR=[]
        i=0
        diff=0
        while i<len(GSR)-1:
           diff=(GSR[i+1]-GSR[i])
           dGSR.append(diff)
           i+=1
        dGSR=gaussian_filter(dGSR,sigma=4)   
        plt.xlabel("time (s)")
        plt.ylabel("GSR difference")
        plt.title("First forward difference")
        plt.plot(dGSR)
    if GSRs!="n":
        GSRmax=max(GSR)
        time=range(len(GSR))
        for value in GSR:
            s_value=value/GSRmax
            GSRs.append(s_value)
        plt.show()
        plt.scatter(time,GSRs)
        plt.title("Standardized GSR")   
        plt.xlabel("time (s)")
        plt.ylabel("GSRs")

    GSR=gaussian_filter(GSR,sigma=5)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(GSR,label='GSR')   
    plt.legend(loc='upper right')
    plt.ylabel("GSR")
    plt.xlabel("time (s)")
    return GSR
