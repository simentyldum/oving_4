from lister_for_del_1 import temperaturer

oppgave_tekts_tall = [4, 7, -1, 15, -2]


def sum_over_5_kalk(tall):
    vekst_sum = 0

    # For alle tall i listen
    for x in tall:
        # Hvis tallet er over 5 -->
        if x > 5:
            # Summerer ekstra grader over 5 til en variabel
            vekst_sum = vekst_sum + x - 5
        # Oppgave a) frivillig) planten tar skade av minusgrader og dør om
        # den får <= 0 vekstpoeng

        # ------------------ Ta vekk denne delen om du vil ha svar på oppgave L -------
        elif x < 0:
            vekst_sum = vekst_sum + x
            if vekst_sum <= 0:
                print("Planten døde")
                break
        # -----------------------------------------------------------------------------
    return vekst_sum


sum_over_5 = sum_over_5_kalk(oppgave_tekts_tall)
print(sum_over_5)

oppgave_h = sum_over_5_kalk(temperaturer)
print(oppgave_h)



