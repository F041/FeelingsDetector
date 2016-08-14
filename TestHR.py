# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 12:57:19 2016

@author: F041
"""

file1=open('2016-4-2_HR_musicPlusGSR.csv','r')
for line in file1:
    field=line.strip(u'\n').split(u';')
    HRvalue=field[2]
    print HRvalue
    
    