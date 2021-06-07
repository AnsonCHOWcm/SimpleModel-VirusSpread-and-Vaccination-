#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:05:18 2021

@author: ccm
"""
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

## Entering the parameter for Developed Market Case and Emerging Market

Daily_Infection_Rate = [1.25222e-06 , 0.000124373]
Recovery_Rate = [0.997 , 0.937]
Daily_Vaccination_Rate = [0.003187608 , 0.0014465]
Dealth_Rate = [0.018 , 0.012]

## Setting the Length for the Stimulation

days = 30

paths = 100

## Setting the Population , Immuned People (Vaccinated + Recovered case) , Infected case , Dealth Case

Population = 1000000

Immuned = np.array([[0] * days] * paths)

Infected = np.array([[0] * days] * paths)

Dealth = np.array([[0] * days] * paths)


## Setting the Case ( 0 = Developed Marlet , 1 = Emerging Market)

cases = 0

## Initialize the Variable used in the stimulation

U = np.zeros(3)

Daily_Dealth_Case = 0 

Daily_Infected_Case = 0 

Daily_Recovery_Case = 0

Possible_infection_Population = Population

## Start the Stimulation for 100 times

for i in range(paths) :
    
    for d in range(days):
        
        U = np.random.uniform(size = 3)
        
        Daily_Dealth_Case = stats.binom.ppf(U[0] , Infected[i][d-1] ,Dealth_Rate[cases] ) if  d > 0 and Infected[i][d-1] >0 else 0
        
        Daily_Recovery_Case = stats.binom.ppf(U[1] , Infected[i][d-1] ,Recovery_Rate[cases] ) if d>0 and Infected[i][d-1] >0 else 0
        
        Daily_Infected_Case = stats.binom.ppf(U[2] , Possible_infection_Population ,Daily_Infection_Rate[cases] ) 
        
        Immuned[i][d] = (Immuned[i][d-1] if d > 0 else 0) + Possible_infection_Population * Daily_Vaccination_Rate[cases] + Daily_Recovery_Case
        
        Possible_infection_Population = Possible_infection_Population * (1 - Daily_Vaccination_Rate[cases]) - Daily_Infected_Case
        
        Infected[i][d] = (Infected[i][d-1] if d > 0 else 0) + Daily_Infected_Case -  Daily_Recovery_Case - Daily_Dealth_Case
        
        Dealth[i][d] = (Dealth[i][d-1] if d > 0 else 0) + Daily_Dealth_Case
        
        
## Computing the Daily Average 

Average_Immuned = np.mean(Immuned , axis = 0) / Population * 100

Average_Dealth = np.mean(Dealth , axis = 0) / Population * 100

Average_Infected = np.mean(Infected , axis = 0) / Population * 100

## Plotting the Garph to show the trend

plt.plot(Average_Immuned)

plt.plot(Average_Dealth)

plt.plot(Average_Infected)

plt.title('Pandamic Development in Developed Market')

plt.xlabel('Days')

plt.ylabel('Rate')

plt.legend(['Immuned Case' , 'Dealth_Case' , 'Infected Case'] , loc = 'upper left')


## Finding the 95% Worse Case
        
        


 


