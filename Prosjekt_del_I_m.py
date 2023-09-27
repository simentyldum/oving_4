# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:34:25 2023

@author: Daniel Harbak
"""

from Prosjekt_del_I_f import lengste_sekvensen_av_0
    #Importer funksjonen fra oppgave f


dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

res=lengste_sekvensen_av_0(dogn_nedbor)
print(f"Den lengste perioden uten nedbør er {res} dager.")