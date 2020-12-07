# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:23:46 2020

@author: alex_
"""

import math 
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
from pandas import ExcelWriter
import string



Df=pd.DataFrame({})

country_list=["Canada", "USA", "Mexico", "UK", "Germany", "China", "Australia", "Brazil", "Norway"]
shipping_permission=["Yes", "No"]
colour_list=["Pink", "Yellow", "Green", "Blue", "Red", "Orange", "Purple", "Black", "Grey", "Brown"]
letters=["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m","n", "o"]
names=[]
for i in range(500):
    name="".join(np.random.choice(letters, size=10))
    names.append(name)
names=list(set(names))

Df["Name"]=names
Df["Country"]=np.random.choice(country_list, size=len(Df))
Df["Shipping"]=np.random.choice(shipping_permission, size=len(Df))
Df["Colour"]=np.random.choice(colour_list, size=len(Df))
print(Df)

matches=[]
matched=[]
notmatched=[]
while len(matches)<len(Df):
    for i in range(0, len(Df)):
        if Df.loc[i]["Name"] not in matches:
            if Df.loc[i]["Shipping"]=="No":
                Dfi=Df[(Df["Country"]==Df.loc[i]["Country"]) & (Df["Shipping"]=="No") & (Df["Colour"]==Df.loc[i]["Colour"]) &(Df.index != i) & (~Df["Name"].isin(matches))]
                if len(Dfi)>1:
                        Dfi=Dfi[:1]
                if len(Dfi)==0:
                        Dfi=Df[(Df["Country"]==Df.loc[i]["Country"])  & (Df["Shipping"]=="No") & (Df.index != i) & (~Df["Name"].isin(matches))]
                        if len(Dfi)>1:
                            Dfi=Dfi[:1]
                        if len(Dfi)==0:
                            Dfi=Df[(Df["Country"]==Df.loc[i]["Country"])  & (Df.index != i) & (~Df["Name"].isin(matches))]
                            if len(Dfi)>1:
                                Dfi=Dfi[:1]
                            if len(Dfi)==0:
                                notmatched.append(Df.loc[i]["Name"])
                                matches.append(Df.loc[i]["Name"])
                if len(Dfi)==1:
                    matches.append(Df.loc[i]["Name"])
                    matches.extend(Dfi["Name"].values.tolist())
                    matched.extend(Df.loc[i]["Name"]+ " , "+Dfi["Name"].values) 
            if Df.loc[i]["Shipping"]=="Yes":
                Dfi=Df[((Df["Country"]==Df.loc[i]["Country"]) | (Df["Shipping"]=="Yes")) & (Df["Colour"]==Df.loc[i]["Colour"]) &(Df.index != i) & (~Df["Name"].isin(matches))]
                if len(Dfi)>1:
                    Dfi=Dfi[:1]
                if len(Dfi)==0:
                    Dfi=Df[(Df["Colour"]==Df.loc[i]["Colour"]) & (Df["Shipping"]=="Yes") & (Df.index != i) & (~Df["Name"].isin(matches))]
                    if len(Dfi)>1:
                        Dfi=Dfi[:1]
                    if len(Dfi)==0:
                        Dfi=Df[((Df["Country"]==Df.loc[i]["Country"])  | (Df["Shipping"]=="Yes")) & (Df.index != i) & (~Df["Name"].isin(matches))]
                        if len(Dfi)>1:
                            Dfi=Dfi[:1]
                        if len(Dfi)==0:
                            Dfi=Df[(Df.index != i) & (~Df["Name"].isin(matches))]
                            if len(Dfi)>1:
                                Dfi=Dfi[:1]
                            if len(Dfi)==0:
                                notmatched.append(Df.loc[i]["Name"])
                                matches.append(Df.loc[i]["Name"])
                if len(Dfi)==1:
                    matches.append(Df.loc[i]["Name"])
                    matches.extend(Dfi["Name"].values.tolist())
                    matched.extend(Df.loc[i]["Name"]+ " , "+Dfi["Name"].values)
          
matched.extend(notmatched)
matchesdf=pd.DataFrame(matched, columns=["matches"])
print(matchesdf)

#writer = pd.ExcelWriter('matches.xlsx', engine="xlsxwriter")
#matchesdf.to_excel(writer,sheet_name='Sheet1')
#writer.save()