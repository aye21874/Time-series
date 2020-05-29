# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:57:56 2020

@author: HP ProBook
"""

import numpy as np

years = np.array([1901,1911,1921,1931,1941,1951,1961,1971])
y = np.array([238.3,252,251.2,278.9,318.5,361,439.1,547.9])
intv = years[1] - years[0]
sum_y = np.sum(y)
print(sum_y)
n = len(years)
if(n%2 == 1):
    diff = years[int(n/2)]
    u = (years - diff)/intv
else:
    diff = (years[int(n/2)] + years[int(n/2) - 1])/2
    u = years - diff
    u = 2*u
    u = u/intv
print("u::::")
print(u)
print("uy::::")
uy = u*y
print(uy)
print("u2:::")
u_2 = u*u
print(u_2)
sum_u = np.sum(u)
print(u_2)
if(sum_u == 0):
    a = sum_y/n
b = (np.sum(uy) - a*sum_u)/(np.sum(u_2))
print(a,b)
trend = a + b*u
print("trend::::::::")
print(trend)

print("additive model:::::::::")
print(y - trend)
print("multiplicative model::::::::")
print(y/trend)
