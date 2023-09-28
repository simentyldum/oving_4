#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:24:14 2023

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

liste1 = [1,2, 5, 9]
liste2 = [1,2, 3, 7]

a, b = beregn_trend(liste1, liste2)
print(a)