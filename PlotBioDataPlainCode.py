# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 12:57:19 2016

@author: F041
"""
from __future__ import division
from scipy.stats.stats import pearsonr  
from scipy.ndimage.filters import gaussian_filter

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scisig
import math
def cleaning(NameOfTheFile,cleaning_position=0):
    data =open(NameOfTheFile,'r')
    DataGross=[]
    DataClean=[]
    for line in data:    
        lst=line.split('\r')
        for string in lst:
            string=string.split(', ')
            DataGross.append(string)
    DataGross.remove(DataGross[-1])   
    number_of_writings=0 
    for lst in DataGross:
        if lst[1]=="00:00:05":
            number_of_writings+=1
        elif number_of_writings==1 and lst[1]!="00:00:05":
            DataClean.append(int(lst[cleaning_position]))
    return DataClean

GSRTdata=np.genfromtxt('darksouls2.txt',skip_header=0,delimiter=',',dtype=float, deletechars='\n')
HR=cleaning('2016-5-20_HR_birthday.csv',2)
#HR = np.genfromtxt('2016-5-20_HR_birthday.csv',skip_header=1,delimiter=',',dtype=int, deletechars='\n')[:,2]
RR= cleaning('2016-5-20_RR_birthday.csv',1)
media_GSR=0
media_Temp=0
GSR=[]
TEMPERATURE=[]
R=[]

contatore=0
if len(GSRTdata)==len(HR)-math.log(len(HR)):
    for line in GSRTdata:
        gsr=int(line[0])
        temp=int(line[1])
        media_GSR+=gsr
        media_Temp+=temp
        if contatore==3:
            GSR.append(media_GSR/(contatore+1))
            media_GSR=0        
            TEMPERATURE.append(media_Temp/(contatore+1))
            media_Temp=0
            contatore=0
        else:
            contatore+=1
    plt.close

dHR=[]
Ts=[]
GSRs=[]
HRs=[]
RRs=[]
if len(RR)!=0:
    RRmax=max(RR)
    for value in RR:
        x=value/RRmax
        RRs.append(x)
if len(HR)!=0:
    HRmax=max(HR)
    for beat in HR:
        x=beat/HRmax
        HRs.append(x)
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
if len(TEMPERATURE)!=0:
    Tmax=max(TEMPERATURE)
    for value in TEMPERATURE:
        x=value/Tmax
        Ts.append(x)

GSR=gaussian_filter(GSR,sigma=5)

dGSR=[]
i=0
diff=0
while i<len(GSR)-1:
   diff=(GSR[i+1]-GSR[i])
   dGSR.append(diff)
   i+=1
   
diffhr=0   
i=0
while i<len(HR)-1:
    diffhr=(HR[i+1]-HR[i])
    dHR.append(diffhr)
    i+=1

HRs=gaussian_filter(HRs,sigma=4)
"""fs=4
cutoff=1
order=5
nyq = 0.5 * fs
normal_cutoff = cutoff / nyq
dGSR = scisig.butter(order, normal_cutoff, btype='low', analog=False) #????
y = scisig.lfilter()"""
#plt.plot(dGSR)
#plt.plot(dHR, marker='x',linewidth=0.7, mew=0.4, ms=3)



fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.plot(GSRs,label='GSR')
#ax1.plot(Ts, label='Temp',marker='x')
ax1.plot(HRs,marker='x',label='HR',linewidth=0.7, mew=0.4, ms=3, color='red')
ax1.plot(RRs,marker='o',label='RR',linewidth=0.3, mew=0.4, ms=3, color='orange')
plt.legend(loc='upper right');
plt.show()

"""len_diff=abs(len(GSRs)-len(HRs))
len_diff2=abs(len(dGSR)-len(dHR))
if len(GSRs)>len(HRs):
    print 'correlazione GSR e HR'
    print np.corrcoef(GSRs[0:(len(GSRs)-len_diff)],HRs)
    print 'correlazione dGSR e dHR'
    print np.corrcoef(dGSR[0:(len(dGSR)-len_diff2)],dHR)
else:
    print 'correlazione GSR e HR'
    print np.corrcoef(GSRs,HRs[0:(len(HRs)-len_diff)])
    print 'correlazione HR e T'
    print np.corrcoef(HRs[0:(len(HRs)-len_diff)],Ts)
    print 'correlazione dHR e dGSR'
    print np.corrcoef(dHR,dGSR[0:(len(dGSR)-len_diff2)])
print 'correlazione GSR e T'"""
#print np.corrcoef(GSRs,Ts)

    

    
    