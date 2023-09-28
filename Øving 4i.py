#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:00:08 2023

@author: kimnguyen
"""

# Importer funksjonen fra oppgave d)
def tell_storre_enn_eller_lik(liste, verdi):
    antall_storre_enn_eller_lik = 0
    for element in liste:
        if element >= verdi:
            antall_storre_enn_eller_lik += 1
    return antall_storre_enn_eller_lik

# Data fra filen "lister_for_del_1.py"
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
                21, 26, 21, 31, 15, 4, 1, -2]

# Finn antall sommerdager (over 20 grader)
antall_sommerdager = tell_storre_enn_eller_lik(temperaturer, 20)

# Finn antall høysommerdager (over 25 grader)
antall_hoysommerdager = tell_storre_enn_eller_lik(temperaturer, 25)

# Finn antall tropedager (over 30 grader)
antall_tropedager = tell_storre_enn_eller_lik(temperaturer, 30)

# Skriv ut resultatene
print(f"Antall sommerdager: {antall_sommerdager}")
print(f"Antall høysommerdager: {antall_hoysommerdager}")
print(f"Antall tropedager: {antall_tropedager}")
