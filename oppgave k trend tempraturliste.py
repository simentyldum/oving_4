#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:25:13 2023

@author: marius
"""

def beregn_trend(x_liste, y_liste):
    x_gjennomsnitt = sum(x_liste)
    y_gjennomsnitt = sum(y_liste)
    
    teller = 0
    nevner = 0
    
    for i in range(len(x_liste)): 
        teller += (x_liste[i] - x_gjennomsnitt) * (y_liste[i] - y_gjennomsnitt)
        nevner += (x_liste[i] - x_gjennomsnitt)**2
        
    a = teller/nevner 
    b = y_gjennomsnitt - a * x_gjennomsnitt
    
    return a, b


temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
                21, 26, 21, 31, 15, 4, 1, -2]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

a, b = beregn_trend(temperaturer_tidspunkter, temperaturer)
print(a)