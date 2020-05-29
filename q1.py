# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:00:56 2020

@author: HP ProBook
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(num=None, figsize=(18, 18), dpi=80, facecolor='w', edgecolor='k')
df = pd.read_csv(r'D:\Downloads\CO2_Data.csv')
n = int(input("enter the time period:"))
years = df['Year'].values
value = df['Average CO2 concentration (ppmv)'].values

if(n%2 == 1):
    iter = len(years) - n + 1
    ttl = np.empty(iter);
    n_year = np.empty(iter);
    for i in range(iter):
        ttl[i] = sum(value[i:i+n])
        n_year[i] = years[i+int(n/2)]
    MA = ttl/n
    
    #print(n_year)
    #print(MA)
else:
    iter = len(years) - n + 1
    ttl_1 = np.empty(iter);
    n_year = np.empty(iter-1);
    for i in range(iter):
        ttl_1[i] = sum(value[i:i+n])
    ttl_1 = ttl_1/n
    #print(ttl_1)
    iter_2 = iter - 1
    ttl_2 = np.empty(iter_2);
    for i in range(iter_2):
        ttl_2[i] = sum(ttl_1[i:i+2])
    MA = ttl_2/2
    #print(years)
    for i in range(iter-1):
        n_year[i] = years[int(n/2)+i]
    
plt.title('Moving Average')
plt.xlabel('Years') 
plt.ylabel('Average CO2 concentration (ppmv)') 
plt.plot(years,value,label = 'original')
plt.xticks(np.arange(min(years), max(years)+1, 2.0))
plt.yticks(np.arange(min(value), max(value)+1, 2.0))
plt.plot(n_year,MA,label = 'MA values (window size = 3)')
plt.legend(loc="upper left")
plt.grid()
plt.show()
    