# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:09:50 2020

@author: alex_
"""

#import math 
import numpy as np
#from numpy import random
import pandas as pd
#import matplotlib.pyplot as plt
#from pandas import ExcelWriter
#import string

#Generating the test dataframes
Df2020=pd.DataFrame({})
letters=["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m","n", "o"]
names=[]
for i in range(500):
    name="".join(np.random.choice(letters, size=10))
    names.append(name)
names=list(set(names))

Df2020["Name"]=names
Sending_list=list(range(1,500))
Sending_list.append(0)

Recieving_list=np.array(range(0,500))
Recieving_list=(Recieving_list-1)%500

Df2020["Sending"]=Sending_list
Df2020["Recieving"]=Recieving_list

Df2019=Df2020


for i in range(0,len(Df2020)):
    j=Df2020.loc[i]["Sending"]
    k=Df2019[Df2019["Name"]==Df2020.loc[i]["Name"]]["Sending"]
    sent2020=[]
    sent2020.append(Df2020.loc[j]["Name"])
    sent2019=list(Df2019.loc[k]["Name"])
    if sent2020==sent2019:
        print(Df2020.loc[i]["Name"]+ " is sending to the same person as last year.")
    l=Df2019[Df2019["Name"]==Df2020.loc[i]["Name"]]["Recieving"]
    recieved2019=list(Df2019.loc[l]["Name"])
    if sent2020==recieved2019:
        print(Df2020.loc[i]["Name"]+ " is sending to someone they recieved a gift from last year.")
        

        
    
        


                   
