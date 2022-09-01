# Question 3 of NA
# CNNAUA001
# 10/6/2020

## Importing Libraries ---------------------------------------------------------
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib import rc
##------------------------------------------------------------------------------

## Initialising Variables & Arrays ---------------------------------------------
n = 1000
a = 0                                       # Intitial value
b = 1                                       # Final value
h = (b - a) / n                             # Increment
i = 0                                       # Index
area = []                                   # Array that stores area
##------------------------------------------------------------------------------

## Defining the Functions ------------------------------------------------------
def f(x):
    y = 4 / (1+x**2)
    return y

def fdp(x):                                 # Second derivative of f(x)
    y = -((8*(-3*x**2+1))/(1+x**2)**3)
    return y

def w(i,a,h):                               # Midpoint function
    y = a + (i + 0.5)*h
    return y 
##------------------------------------------------------------------------------

## Composite Midpoint method ---------------------------------------------------
while i < n:
    area.append(h*f(w(i,a,h)))              # Stores rectangle areas
    i += 1
Area = np.sum(area) + (h**2 / 24)*(fdp(0))  # Finds the total area
##------------------------------------------------------------------------------

## Printing --------------------------------------------------------------------
print('Estimate of pi is: ',Area)
print('pi is actually: ',np.pi)
print('Absolute error is:', abs(np.pi - Area))
##------------------------------------------------------------------------------