#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:54:20 2023

@author: kimnguyen
"""

def beregn_differanser(lista):
    differanser = []
    for i in range(len(lista) - 1):
        differanse = lista[i+1] - lista[i]
        differanser.append(differanse)
    return differanser

def vurder_temperaturendringer(temperaturliste):
    differanser = beregn_differanser(temperaturliste)
    
    for i, differanse in enumerate(differanser):
        if differanse > 0:
            print(f"Tidspunkt {i}: stigende")
        elif differanse < 0:
            print(f"Tidspunkt {i}: synkende")
        else:
            print(f"Tidspunkt {i}: uforandret")

# Eksempel på bruk av funksjonen:
temperaturliste = [11, 15, 10, 8, 11, 12]
vurder_temperaturendringer(temperaturliste)




