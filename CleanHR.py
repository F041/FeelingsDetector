# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:40:49 2016

@author: F041
"""
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


data =open('2016-5-20_RR_birthday.csv','r')
cleaning_position=1
DataGross=[]
DataClean=[]
for line in data:    
    lst=line.split('\r')
    for string in lst:
        string=string.split(', ')
        if string not in DataGross:
            DataGross.append(string)

for line in DataGross: #Data problem: or too few or too much
    if line[0] in DataGross and line[1] in DataGross :
        DataGross.remove(line)
        DataGross.sort()
 
"""number_of_writings=0 
indicator=0
for lst in DataGross:
    if lst in DataGross:
        DataGross.remove(lst)
        if number_of_writings==1 and lst[1]!="00:00:05":
        DataClean.append(int(lst[cleaning_position]))
    indicator+=1"""

        
