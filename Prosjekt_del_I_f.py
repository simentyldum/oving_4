# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:04:53 2023

@author: Daniel Harbak
"""

def lengste_sekvensen_av_0(liste):
    lengste_sekvens = 0
    current_lengde = 0
    
    for tall in liste:
        # Her sjekker vi stegvis om tallet i rekken er = 0, hvis legges det til enda en current lengde og går videre til nytt tall til det treffer et tall som diffirensiere seg fra null.
        if tall == 0:
            current_lengde +=1
            
        else:
        # Her sjekker vi om sekvensen av null tall er større en tidligere sekvenser. Hvis dette er tilfelle, erstatter denne nye høyre current serkvensen til den lengste serkvensen slik at vi kan lagre dette nummeret. 
            if current_lengde > lengste_sekvens:
                lengste_sekvens = current_lengde
        # Her restarter vi current lengde slik at vi ikke bare får sumen av null tall.
            current_lengde = 0
    
    if current_lengde > lengste_sekvens:
        lengste_sekvens = current_lengde
        # Her kjører vi if setningen en siste gang for å sjekke om høyeste sekvensen av nuller er i slutten av rekken ettersom den tidligere if loopen ikke ville registrert/aktivert dette om det ikke ville vært etterfølgt av et ikke null tall.
    
    return lengste_sekvens
        # Her angir vi hva verdi funksjonen skal resultere med.
        
if __name__ == "__main__":
    
    liste = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19,0 , 0 ,0 ,0]
    res = lengste_sekvensen_av_0(liste)
    print(f" Den lengste sammenhengende sekvensen av 0-ere i listen er: {res}")
