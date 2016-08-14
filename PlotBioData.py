# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 11:43:52 2016

@author: F041
"""
from __future__ import division
from scipy.stats.stats import pearsonr   
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter

class GSR_HR():
    gsr=''
    hr=''
    
    def __init__(self,file_GSR,file_HR=0):
        self.GSRdata=np.genfromtxt(file_GSR,skip_header=0,delimiter=',',dtype=int, deletechars='\n')
        if file_HR!=0:            
            self.HR=np.genfromtxt(file_HR,skip_header=1,delimiter=',',dtype=int, deletechars='\n')
        else:
            self.HR=""
        self.GSR=[]
        self.HRvect=[]
        self.HRs=[]
        self.GSRs=[]
    def getData(self):
        media=0
        contatore=0
        for line in self.GSRdata:
            line=int(line)
            media+=line            
            if contatore==3:
                self.GSR.append(media/(contatore+1))
                media=0
                contatore=0
            else:
                contatore+=1
        if self.HR!="":
            self.HRvect=np.asanyarray(self.HR[:,2],int)
        for beat in self.HRvect:
            svalue=beat/(max(self.HRvect))
            self.HRs.append(svalue)
        for resistance in self.GSR:
            svalue=resistance/(max(self.GSR))
            self.GSRs.append(svalue)
        return self.GSR
    def getTemperature(self):  
        R=[]
        for value in self.GSRs:
            skinR=10**5            
            R.append(1/value)
            #return R
            
    def plot(self):
        print len(self.GSRs)
        print len(self.HRs)

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(self.GSRs[0:1407],label='GSR', color='grey')
        ax1.plot(self.HRs[7:1407],marker='x',label='HR',linewidth=0.7, mew=0.4, ms=3, color='r')
        plt.legend(loc='upper right');
        plt.show()
       
        
        print pearsonr(self.GSRs[0:1400],self.HRs[0:1400])

dati=GSR_HR('quora2.txt','2016-4-9_HR_quora.csv')
print dati.getData()
dati.plot()


        