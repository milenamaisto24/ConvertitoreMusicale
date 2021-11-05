import re
melodia = ""
numeri = ""
nota = []
durata = []
numero = []

def ABCtoNum():
    print(" ")
    print('INSERIRE LA MELODIA DA CONVERTIRE IN NUMERI - Attenzione! Inserire valori compresi tra C, e b ')
    print("Melodia: ")
    melodia = input()
    melodia2 = melodia.split(' ')
    print(melodia2)

    for curr in melodia2:
        contatore = 0
        size = len(curr)

        if curr[contatore] == "C":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("13")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("25")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "D":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("15")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("27")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "E":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("17")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("29")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "F":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("18")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("30")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "G":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("20")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("32")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "A":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("22")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("34")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

        elif curr[contatore] == "B":
            if contatore + 1 < size and curr[contatore + 1] == ",":
                nota.append("24")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
            else:
                nota.append("36")
                if contatore == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 1:size:1])
                contatore += 1
                continue

# -----------------------------------------------------------------------------------
        elif curr[contatore] == "^":
            if contatore == size - 1:
                break
            elif curr[contatore + 1] == "C":
                if contatore + 2 < size and curr[contatore + 2] == ",":
                    nota.append("14")
                    if contatore + 2 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 3:size:1])
                    contatore += 3
                    continue
                else:
                    nota.append("26")
                    if contatore + 1 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 2:size:1])
                    contatore += 2
                    continue
            elif curr[contatore + 1] == "c":
                nota.append("38")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue

            elif curr[contatore + 1] == "D":
                if contatore + 2 < size and curr[contatore + 2] == ",":
                    nota.append("16")
                    if contatore + 2 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 3:size:1])
                    contatore += 3
                    continue
                else:
                    nota.append("28")
                    if contatore + 1 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 2:size:1])
                    contatore += 2
                    continue
            elif curr[contatore + 1] == "d":
                nota.append("40")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue

            elif curr[contatore + 1] == "F":
                if contatore + 2 < size and curr[contatore + 2] == ",":
                    nota.append("19")
                    if contatore + 2 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 3:size:1])
                    contatore += 3
                    continue
                else:
                    nota.append("31")
                    if contatore + 1 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 2:size:1])
                    contatore += 2
                    continue
            elif curr[contatore + 1] == "f":
                nota.append("43")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue

            elif curr[contatore + 1] == "G":
                if contatore + 2 < size and curr[contatore + 2] == ",":
                    nota.append("21")
                    if contatore + 2 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 3:size:1])
                    contatore += 3
                    continue
                else:
                    nota.append("33")
                    if contatore + 1 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 2:size:1])
                    contatore += 2
                    continue
            elif curr[contatore + 1] == "g":
                nota.append("45")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue

            elif curr[contatore + 1] == "A":
                if contatore + 2 < size and curr[contatore + 2] == ",":
                    nota.append("23")
                    if contatore + 2 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 3:size:1])
                    contatore += 3
                    continue
                else:
                    nota.append("35")
                    if contatore + 1 == size - 1:
                        durata.append("1")
                    else:
                        durata.append(curr[contatore + 2:size:1])
                    contatore += 2
                    continue
            elif curr[contatore + 1] == "a":
                nota.append("47")
                if contatore + 1 == size - 1:
                    durata.append("1")
                else:
                    durata.append(curr[contatore + 2:size:1])
                contatore += 2
                continue
# --------------------------------------------------------------------
        elif curr[contatore] == "c":
            nota.append("37")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "d":
            nota.append("39")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "e":
            nota.append("41")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "f":
            nota.append("42")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "g":
            nota.append("44")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "a":
            nota.append("46")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "b":
            nota.append("48")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue
        elif curr[contatore] == "|":
            nota.append("|")
            contatore += 1
            continue
        elif curr[contatore] == "z":
            nota.append("0")
            if contatore == size-1:
                durata.append("1")
            else:
                durata.append(curr[contatore+1:size:1])
            contatore += 1
            continue

    print(nota)
    print(durata)
    return 0

def NumtoABC():
    print(" ")
    print("INSERIRE I NUMERI DA CONVERTIRE IN NOTE - Attenzione! Inserire valori compresi tra 13 e 48")
    print("Numeri: ")
    numeri = input()
    numeri2 = numeri.split(' ')
    print(numeri2)

    for curr in numeri2:
        contatore = 0
        size = len(curr)

        if curr[contatore] == "1":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("A,,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "1":
                numero.append("^A,,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "2":
                numero.append("B,,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "3":
                numero.append("C,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "4":
                numero.append("^C,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "5":
                numero.append("D,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "6":
                numero.append("^D,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "7":
                numero.append("E,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "8":
                numero.append("F,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "9":
                numero.append("^F,")
                contatore += 2
                continue
            else:
                numero.append("C,,")
                contatore += 1
                continue

        if curr[contatore] == "2":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("G,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "1":
                numero.append("^G,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "2":
                numero.append("A,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "3":
                numero.append("^A,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "4":
                numero.append("B,")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "5":
                numero.append("C")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "6":
                numero.append("^C")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "7":
                numero.append("D")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "8":
                numero.append("^D")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "9":
                numero.append("E")
                contatore += 2
                continue
            else:
                numero.append("^C,,")
                contatore += 1
                continue

        if curr[contatore] == "3":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("F")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "1":
                numero.append("^F")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "2":
                numero.append("G")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "3":
                numero.append("^G")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "4":
                numero.append("A")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "5":
                numero.append("^A")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "6":
                numero.append("B")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "7":
                numero.append("c")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "8":
                numero.append("^c")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "9":
                numero.append("d")
                contatore += 2
                continue
            else:
                numero.append("D,,")
                contatore += 1
                continue

        if curr[contatore] == "4":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("^d")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "1":
                numero.append("^e")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "2":
                numero.append("f")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "3":
                numero.append("^f")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "4":
                numero.append("g")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "5":
                numero.append("^g")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "6":
                numero.append("a")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "7":
                numero.append("^a")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "8":
                numero.append("b")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "9":
                numero.append("c'")
                contatore += 2
                continue
            else:
                numero.append("^D,,")
                contatore += 1
                continue

        if curr[contatore] == "5":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("^c'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "1":
                numero.append("d'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "2":
                numero.append("^d'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "3":
                numero.append("e'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "4":
                numero.append("f'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "5":
                numero.append("^f'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "6":
                numero.append("g'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "7":
                numero.append("^g'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "8":
                numero.append("a'")
                contatore += 2
                continue
            if contatore + 1 < size and curr[contatore + 1] == "9":
                numero.append("^a'")
                contatore += 2
                continue
            else:
                numero.append("E,,")
                contatore += 1
                continue

        if curr[contatore] == "6":
            if contatore + 1 < size and curr[contatore + 1] == "0":
                numero.append("b'")
                contatore += 2
                continue
            else:
                numero.append("F,,")
                contatore += 1
                continue

        if curr[contatore] == "7":
            numero.append("^F,,")
            contatore += 1
            continue

        if curr[contatore] == "8":
            numero.append("G,,")
            contatore += 1
            continue

        if curr[contatore] == "9":
            numero.append("^G,,")
            contatore += 1
            continue

        if curr[contatore] == "0":
            numero.append("z")
            contatore += 1
            continue

        if curr[contatore] == "|":
            numero.append("|")
            contatore += 1
            continue

    print(numero)
    return 0

