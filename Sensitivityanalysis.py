#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:40:04 2020

@author: coenminderhoud
"""
import numpy as np
import csv
from optimize import optimizepy
from main import sensitivityanalysis
######### Sensitivity analysis verhouding weights ###########

fuel_weight = 5
Noiselist = []
Fuelburnlist = []
Ratio = []
for noise_weight in np.arange(0.1,1,10):
    sensitivityanalysis(fuel_weight, noise_weight, 1)
    optimizepy()
    with open('model.sol', newline='\n') as csvfile:
        reader = csv.reader((line.replace('  ', ' ') for line in csvfile), delimiter=' ')
        next(reader)  # skip header
        sol = {}
        for var, value in reader:
            sol[var] = float(value)
    Noiselist.append(sol["total_noise"])
    Fuelburnlist.append(sol["total_fuel_burned"])
    Ratio.append(noise_weight/fuel_weight)
