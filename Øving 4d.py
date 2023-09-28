#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:25:27 2023

@author: kimnguyen
"""

"""
Skriv en funksjon som tar inn ei liste med flyttall og en enkeltverdi. 
Funksjonen skal telle antall elementer i lista som er større enn eller 
lik den oppgitte verdien og returnere dette. 
"""

def tell_storre_enn_eller_lik(liste, verdi):
    antall_storre_enn_eller_lik = 0
    for element in liste:
        if element >= verdi:
            antall_storre_enn_eller_lik += 1
    return antall_storre_enn_eller_lik

# Eksempel på bruk av funksjonen:
min_liste = [1.2, 2.5, 3.7, 4.1, 5.8, 6.3]
verdi = 5
resultat = tell_storre_enn_eller_lik(min_liste, verdi)
print(f"Antall elementer større enn eller lik {verdi}: {resultat}")

