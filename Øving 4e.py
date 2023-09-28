#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:51:55 2023

@author: kimnguyen
"""

def beregn_differanser(liste):
    differanser = []  # Opprett en tom liste for differansene
    for i in range(len(liste) - 1):
        differans = liste[i + 1] - liste[i]  # Regn ut differansen mellom neste tall og dette tallet
        differanser.append(differans)  # Legg til differansen i listen
    return differanser

# Eksempel på bruk av funksjonen:
min_liste = [2, 4, 6, 8, 10]
differanser = beregn_differanser(min_liste)
print("Differansene er:", differanser)

