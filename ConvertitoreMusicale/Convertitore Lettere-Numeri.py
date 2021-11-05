import ABCtoNum
import TrasportoTonalità
import Armonizzazione

sceltaMenu1 = ""
sceltaAggiungiVoce = ""
import re

while sceltaMenu1 != "5":
    print(" ")
    print("MENU' PRINCIPALE")
    print("Scegli quale operazione eseguire: ")
    print("1. Conversione Lettere in Numeri ")
    print("2. Conversione Numeri in Lettere")
    print("3. Trasporta una melodia in un'altra tonalità")
    print("4. Crea una melodia a più voci")
    print("5. Esci dal programma")
    print("Scelta: ")
    sceltaMenu1 = input()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    if sceltaMenu1 == "1":
        ABCtoNum.ABCtoNum()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    elif sceltaMenu1 == "2":
        ABCtoNum.NumtoABC()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    elif sceltaMenu1 == "3":
        TrasportoTonalità.TrasportoTonalità()


        print(" ")
        print("INSERIRE MELODIA DA TRASPORTARE (Attenzione! Puo inserire valori compresi tra C, e b)")
        print("Melodia: ")
        var = input()
        var2 = " "
        var3 = " "
        size = len(var)
        contatore = 0

        while contatore < size:
            if var[contatore] == "C":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "25 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "13 "
                    contatore += 2
                    continue
            elif var[contatore] == "D":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "27 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "15 "
                    contatore += 2
                    continue
            elif var[contatore] == "E":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "29 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "17 "
                    contatore += 2
                    continue
            elif var[contatore] == "F":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "30 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "18 "
                    contatore += 2
                    continue
            elif var[contatore] == "G":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "32 "
                elif var[contatore + 1] == ",":
                    var2 += "20 "
                    contatore += 2
                    continue
            elif var[contatore] == "A":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "34 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "22 "
                    contatore += 2
                    continue
            elif var[contatore] == "B":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "36 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "24 "
                    contatore += 2
                    continue
            # -----------------------------------------------------------------------------------
            elif var[contatore] == "^":
                if contatore == size - 1:
                    break
                elif var[contatore + 1] == "C":
                    if contatore + 2 < size and var[contatore + 2] == ",":
                        var2 += "14 "
                        contatore += 3
                        continue
                    else:
                        var2 += "26 "
                        contatore += 2
                        continue
                elif var[contatore + 1] == "c":
                    var2 += "38 "
                    contatore += 2
                    continue
                elif var[contatore + 1] == "D":
                    if contatore + 2 < size and var[contatore + 2] == ",":
                        var2 += "16 "
                        contatore += 3
                        continue
                    else:
                        var2 += "28 "
                        contatore += 2
                        continue
                elif var[contatore + 1] == "d":
                    var2 += "40 "
                    contatore += 2
                    continue
                elif var[contatore + 1] == "F":
                    if contatore + 2 < size and var[contatore + 2] == ",":
                        var2 += "19 "
                        contatore += 3
                        continue
                    else:
                        var2 += "31 "
                        contatore += 2
                        continue
                elif var[contatore + 1] == "f":
                    var2 += "43 "
                    contatore += 2
                    continue
                elif var[contatore + 1] == "G":
                    if contatore + 2 < size and var[contatore + 2] == ",":
                        var2 += "21 "
                        contatore += 3
                        continue
                    else:
                        var2 += "33 "
                        contatore += 2
                        continue
                elif var[contatore + 1] == "g":
                    var2 += "45 "
                    contatore += 2
                    continue
                elif var[contatore + 1] == "A":
                    if contatore + 2 < size and var[contatore + 2] == ",":
                        var2 += "23 "
                        contatore += 3
                        continue
                    else:
                        var2 += "35 "
                        contatore += 2
                        continue
                elif var[contatore + 1] == "a":
                    var2 += "47 "
                    contatore += 2
                    continue

            # --------------------------------------------------------------------
            elif var[contatore] == "c":
                var2 += "37 "
                contatore += 1
                continue
            elif var[contatore] == "d":
                var2 += "39 "
                contatore += 1
                continue
            elif var[contatore] == "e":
                var2 += "41 "
                contatore += 1
                continue
            elif var[contatore] == "f":
                var2 += "42 "
                contatore += 1
                continue
            elif var[contatore] == "g":
                var2 += "44 "
                contatore += 1
                continue
            elif var[contatore] == "a":
                var2 += "46 "
                contatore += 1
                continue
            elif var[contatore] == "b":
                var2 += "48 "
                contatore += 1
                continue
            elif var[contatore] == "|":
                var2 += "| "
                contatore += 1
                continue

            contatore += 1
        print("Melodia originale in numeri:" + var2)
        print(" ")

        print("Di quanti semitoni vuoi trasportare? Attenzione! Puoi trasportare al massimo di +12 o -12 ")
        print("Scelta: ")
        sceltaTrasporto = input()

        var5 = var2.split()
        for nota1 in var5:
            sceltaTrasporto1 = int(sceltaTrasporto)
            nota1 = int(nota1) + sceltaTrasporto1
            var3 += str(nota1) + " "

        print(" ")
        print("Melodia originale:" + var2)
        print("Melodia trasportata:" + var3)

        var4 = " "
        contatore1 = 0
        size1 = len(var3)

        while contatore1 < size1:
            if contatore1 == size1 - 1:
                break
            if var3[contatore1] == "1":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "A,, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                    var4 += "^A,, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                    var4 += "B,, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                    var4 += "C, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                    var4 += "^C, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                    var4 += "D, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                    var4 += "^D, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                    var4 += "E, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                    var4 += "F, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                    var4 += "^F, "
                    contatore1 += 2
                    continue
                else:
                    var4 += "C,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "2":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "G, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                    var4 += "^G, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                    var4 += "A, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                    var4 += "^A, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                    var4 += "B, "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                    var4 += "C "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                    var4 += "^C "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                    var4 += "D "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                    var4 += "^D "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                    var4 += "E "
                    contatore1 += 2
                    continue
                else:
                    var4 += "^C,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "3":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "F "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                    var4 += "^F "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                    var4 += "G "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                    var4 += "^G "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                    var4 += "A "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                    var4 += "^A "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                    var4 += "B "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                    var4 += "c "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                    var4 += "^c "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                    var4 += "d "
                    contatore1 += 2
                    continue
                else:
                    var4 += "D,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "4":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "^d "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                    var4 += "^e "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                    var4 += "f "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                    var4 += "^f "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                    var4 += "g "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                    var4 += "^g "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                    var4 += "a "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                    var4 += "^a "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                    var4 += "b "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                    var4 += "c' "
                    contatore1 += 2
                    continue
                else:
                    var4 += "^D,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "5":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "^c' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                    var4 += "d' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                    var4 += "^d' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                    var4 += "e' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                    var4 += "f' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                    var4 += "^f' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                    var4 += "g' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                    var4 += "^g' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                    var4 += "a' "
                    contatore1 += 2
                    continue
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                    var4 += "^a' "
                    contatore1 += 2
                    continue
                else:
                    var4 += "E,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "6":
                if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                    var4 += "b' "
                    contatore1 += 2
                    continue
                else:
                    var4 += "F,, "
                    contatore1 += 1
                    continue

            if var3[contatore1] == "7":
                var4 += "^F,, "
                contatore1 += 1
                continue

            if var3[contatore1] == "8":
                var4 += "G,, "
                contatore1 += 1
                continue

            if var3[contatore1] == "9":
                var4 += "^G,, "
                contatore1 += 1
                continue

            if var3[contatore1] == "|":
                var4 += "| "
                contatore1 += 1
                continue

            contatore1 += 1
        print("Melodia trasportata in ABC:" + var4)
        print(" ")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    elif sceltaMenu1 == "4":
        Armonizzazione.Armonizzazione()

        print(" ")
        print("Inserire la melodia originale: ")
        print("N.B. Puoi inserire valori compresi da C, a b. Questa funzione trasporta solo in tonalità di Do Mag")
        var = input()
        var2 = ""
        var4 = ""
        var3 = ""
        var6 = ""
        var7 = ""
        var8 = ""
        var9 = ""
        var10 = ""
        var11 = ""

        size = len(var)
        contatore = 0

        while contatore < size:
            if var[contatore] == "C":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "15 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "8 "
                    contatore += 2
                    continue
            elif var[contatore] == "D":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "16 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "9 "
                    contatore += 2
                    continue
            elif var[contatore] == "E":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "17 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "10 "
                    contatore += 2
                    continue
            elif var[contatore] == "F":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "18 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "11 "
                    contatore += 2
                    continue
            elif var[contatore] == "G":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "19 "
                elif var[contatore + 1] == ",":
                    var2 += "12 "
                    contatore += 2
                    continue
            elif var[contatore] == "A":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "20 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "13 "
                    contatore += 2
                    continue
            elif var[contatore] == "B":
                if contatore + 1 == size \
                        or re.match('[A-Ga-g_^= ]', var[contatore + 1]):
                    var2 += "21 "
                    contatore += 1
                    continue
                elif var[contatore + 1] == ",":
                    var2 += "14 "
                    contatore += 2
                    continue
        # --------------------------------------------------------------------
            elif var[contatore] == "c":
                var2 += "22 "
                contatore += 1
                continue
            elif var[contatore] == "d":
                var2 += "23 "
                contatore += 1
                continue
            elif var[contatore] == "e":
                var2 += "24 "
                contatore += 1
                continue
            elif var[contatore] == "f":
                var2 += "25 "
                contatore += 1
                continue
            elif var[contatore] == "g":
                var2 += "26 "
                contatore += 1
                continue
            elif var[contatore] == "a":
                var2 += "27 "
                contatore += 1
                continue
            elif var[contatore] == "b":
                var2 += "28 "
                contatore += 1
                continue
            elif var[contatore] == "|":
                var2 += "| "
                contatore += 1
                continue

            contatore += 1
        print("Melodia numerica: " + var2)

        while sceltaAggiungiVoce != "5":
            print(" ")
            print("Quale voce vuoi aggiungere? ")
            print("1. Aggiungi una terza sotto")
            print("2. Aggiungi una terza sopra")
            print("3. Aggiungi un'ottava sopra")
            print("4. Aggiungi un'ottava sotto")
            print("5. Indietro")

            print("Scelta: ")
            sceltaAggiungiVoce = input()

            if sceltaAggiungiVoce == "1":
                var5 = var2.split()
                for nota in var5:
                    nota = int(nota) + -2
                    var3 += str(nota) + " "

                print(" ")
                print("Voce originale numerica: " + var2)
                print("Voce una terza sotto: " + var3)

                contatore1 = 0
                size1 = len(var3)

                while contatore1 < size1:
                    if contatore1 == size1 - 1:
                        break
                    if var3[contatore1] == "1":
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                            var4 += "E, "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                            var4 += "F, "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                            var4 += "G, "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                            var4 += "A, "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                            var4 += "B, "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                            var4 += "C "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                            var4 += "D "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                            var4 += "E "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                            var4 += "F "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                            var4 += "G "
                            contatore1 += 2
                            continue
                        else:
                            var4 += "C,, "
                            contatore1 += 1
                            continue

                    if var3[contatore1] == "2":
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                            var4 += "A "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                            var4 += "B "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                            var4 += "c "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                            var4 += "d "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                            var4 += "e "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                            var4 += "f "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "6":
                            var4 += "g "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "7":
                            var4 += "a "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "8":
                            var4 += "b "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "9":
                            var4 += "c' "
                            contatore1 += 2
                            continue
                        else:
                            var4 += "D,, "
                            contatore1 += 1
                            continue

                    if var3[contatore1] == "3":
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "0":
                            var4 += "d' "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "1":
                            var4 += "e' "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "2":
                            var4 += "f' "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "3":
                            var4 += "g' "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "4":
                            var4 += "a' "
                            contatore1 += 2
                            continue
                        if contatore1 + 1 < size1 and var3[contatore1 + 1] == "5":
                            var4 += "b' "
                            contatore1 += 2
                            continue
                        else:
                            var4 += "E,, "
                            contatore1 += 1
                            continue

                    if var3[contatore1] == "4":
                        var4 += "F,, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "5":
                        var4 += "G,, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "6":
                        var4 += "A,, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "7":
                        var4 += "B,, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "8":
                        var4 += "C, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "9":
                        var4 += "D, "
                        contatore1 += 1
                        continue

                    if var3[contatore1] == "|":
                        var4 += "| "
                        contatore1 += 1
                        continue

                    contatore1 += 1
                print("Melodia trasportata in ABC: " + var4)


            if sceltaAggiungiVoce == "2":
                var5 = var2.split()
                for nota in var5:
                    nota = int(nota) + 2
                    var10 += str(nota) + " "

                print(" ")
                print("Voce originale numerica: " + var2)
                print("Voce una terza sopra: " + var10)

                contatore4 = 0
                size4 = len(var10)

                while contatore4 < size4:
                    if contatore4 == size4 - 1:
                        break
                    if var10[contatore4] == "1":
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "0":
                            var11 += "E, "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "1":
                            var11 += "F, "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "2":
                            var11 += "G, "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "3":
                            var11 += "A, "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "4":
                            var11 += "B, "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "5":
                            var11 += "C "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "6":
                            var11 += "D "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "7":
                            var11 += "E "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "8":
                            var11 += "F "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "9":
                            var11 += "G "
                            contatore4 += 2
                            continue
                        else:
                            var11 += "C,, "
                            contatore4 += 1
                            continue

                    if var10[contatore4] == "2":
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "0":
                            var11 += "A "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "1":
                            var11 += "B "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "2":
                            var11 += "c "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "3":
                            var11 += "d "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "4":
                            var11 += "e "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "5":
                            var11 += "f "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "6":
                            var11 += "g "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "7":
                            var11 += "a "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "8":
                            var11 += "b "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "9":
                            var11 += "c' "
                            contatore4 += 2
                            continue
                        else:
                            var11 += "D,, "
                            contatore4 += 1
                            continue

                    if var10[contatore4] == "3":
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "0":
                            var11 += "d' "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "1":
                            var11 += "e' "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "2":
                            var11 += "f' "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "3":
                            var11 += "g' "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "4":
                            var11 += "a' "
                            contatore4 += 2
                            continue
                        if contatore4 + 1 < size4 and var10[contatore4 + 1] == "5":
                            var11 += "b' "
                            contatore4 += 2
                            continue
                        else:
                            var11 += "E,, "
                            contatore4 += 1
                            continue

                    if var10[contatore4] == "4":
                        var11 += "F,, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "5":
                        var11 += "G,, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "6":
                        var11 += "A,, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "7":
                        var11 += "B,, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "8":
                        var11 += "C, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "9":
                        var11 += "D, "
                        contatore4 += 1
                        continue

                    if var10[contatore4] == "|":
                        var11 += "| "
                        contatore4 += 1
                        continue

                    contatore4 += 1
                print("Melodia trasportata in ABC: " + var11)


            if sceltaAggiungiVoce == "3":
                var5 = var2.split()
                for nota in var5:
                    nota = int(nota) + 7
                    var6 += str(nota) + " "

                print(" ")
                print("Voce originale numerica: " + var2)
                print("Voce un'ottava sopra: " + var6)

                contatore2 = 0
                size2 = len(var6)

                while contatore2 < size2:
                    if contatore2 == size2 - 1:
                        break
                    if var6[contatore2] == "1":
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "0":
                            var7 += "E, "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "1":
                            var7 += "F, "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "2":
                            var7 += "G, "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "3":
                            var7 += "A, "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "4":
                            var7 += "B, "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "5":
                            var7 += "C "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "6":
                            var7 += "D "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "7":
                            var7 += "E "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "8":
                            var7 += "F "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "9":
                            var7 += "G "
                            contatore2 += 2
                            continue
                        else:
                            var7 += "C,, "
                            contatore2 += 1
                            continue

                    if var6[contatore2] == "2":
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "0":
                            var7 += "A "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "1":
                            var7 += "B "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "2":
                            var7 += "c "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "3":
                            var7 += "d "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "4":
                            var7 += "e "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "5":
                            var7 += "f "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "6":
                            var7 += "g "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "7":
                            var7 += "a "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "8":
                            var7 += "b "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "9":
                            var7 += "c' "
                            contatore2 += 2
                            continue
                        else:
                            var7 += "D,, "
                            contatore2 += 1
                            continue

                    if var6[contatore2] == "3":
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "0":
                            var7 += "d' "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "1":
                            var7 += "e' "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "2":
                            var7 += "f' "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "3":
                            var7 += "g' "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "4":
                            var7 += "a' "
                            contatore2 += 2
                            continue
                        if contatore2 + 1 < size2 and var6[contatore2 + 1] == "5":
                            var7 += "b' "
                            contatore2 += 2
                            continue
                        else:
                            var7 += "E,, "
                            contatore2 += 1
                            continue

                    if var6[contatore2] == "4":
                        var7 += "F,, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "5":
                        var7 += "G,, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "6":
                        var7 += "A,, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "7":
                        var7 += "B,, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "8":
                        var7 += "C, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "9":
                        var7 += "D, "
                        contatore2 += 1
                        continue

                    if var6[contatore2] == "|":
                        var7 += "| "
                        contatore2 += 1
                        continue

                    contatore2 += 1
                print("Melodia trasportata in ABC: " + var7)


            if sceltaAggiungiVoce == "4":
                var5 = var2.split()
                for nota in var5:
                    nota = int(nota) + -7
                    var8 += str(nota) + " "

                print(" ")
                print("Voce originale numerica: " + var2)
                print("Voce un'ottava sotto: " + var8)

                contatore3 = 0
                size3 = len(var8)

                while contatore3 < size3:
                    if contatore3 == size3 - 1:
                        break
                    if var8[contatore3] == "1":
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "0":
                            var9 += "E, "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "1":
                            var9 += "F, "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "2":
                            var9 += "G, "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "3":
                            var9 += "A, "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "4":
                            var9 += "B, "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "5":
                            var9 += "C "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "6":
                            var9 += "D "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "7":
                            var9 += "E "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "8":
                            var9 += "F "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "9":
                            var9 += "G "
                            contatore3 += 2
                            continue
                        else:
                            var9 += "C,, "
                            contatore3 += 1
                            continue

                    if var8[contatore3] == "2":
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "0":
                            var9 += "A "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "1":
                            var9 += "B "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "2":
                            var9 += "c "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "3":
                            var9 += "d "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "4":
                            var9 += "e "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "5":
                            var9 += "f "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "6":
                            var9 += "g "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "7":
                            var9 += "a "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "8":
                            var9 += "b "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "9":
                            var9 += "c' "
                            contatore3 += 2
                            continue
                        else:
                            var9 += "D,, "
                            contatore3 += 1
                            continue

                    if var8[contatore3] == "3":
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "0":
                            var9 += "d' "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "1":
                            var9 += "e' "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "2":
                            var9 += "f' "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "3":
                            var9 += "g' "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "4":
                            var9 += "a' "
                            contatore3 += 2
                            continue
                        if contatore3 + 1 < size3 and var8[contatore3 + 1] == "5":
                            var9 += "b' "
                            contatore3 += 2
                            continue
                        else:
                            var9 += "E,, "
                            contatore3 += 1
                            continue

                    if var8[contatore3] == "4":
                        var9 += "F,, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "5":
                        var9 += "G,, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "6":
                        var9 += "A,, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "7":
                        var9 += "B,, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "8":
                        var9 += "C, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "9":
                        var9 += "D, "
                        contatore3 += 1
                        continue

                    if var8[contatore3] == "|":
                        var9 += "| "
                        contatore3 += 1
                        continue

                    contatore3 += 1
                print("Melodia trasportata in ABC: " + var9)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    elif sceltaMenu1 == "5":
        exit()

