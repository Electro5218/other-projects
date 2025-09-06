plik = open("slowa.txt", "r").readlines()
dane = []

## Zad 1

for i in plik:
    i = i.split()
    dane.append(i)

odwrocone = []
strtmp = ""
for o in dane:
    for z in o:
        for indx in range(len(z)-1, -1, -1):
            strtmp += z[indx]
    odwrocone.append(strtmp)
    strtmp = ""



zapis = open("hasla_a.txt", "w")

for b in odwrocone:
    zapis.write(b + "\n")

zapis.close()

najdluzsze = 0
najkrotsze = 9999999
najdluzszetstring = ""
najkrotszestring = ""

for n in odwrocone:
    if len(n) > najdluzsze:
        najdluzszetstring = n
        najdluzsze = len(n)
    if len(n) < najkrotsze:
        najkrotszestring = n
        najkrotsze = len(n)

zapis2 = open("slowa_a.txt", "w")

zapis2.write(najdluzszetstring + " ")
zapis2.write(str(najdluzsze) + " ")
zapis2.write(najkrotszestring + " ")
zapis2.write(str(najkrotsze))

zapis2.close()

## Zad 2

def czyPalindrom(slowo):
    string = ""
    for i in range(len(slowo)-1 , -1, -1):
        string += slowo[i]
    if string == slowo:
        return True, slowo, len(slowo)
    else:
        return False


najdluzszy = ""
najdluzsze = 0
stringtmp = ""
nowehasla = []
w2 = ""
w3 = ""
pomoc = ""

for o in dane:
    for z in o:
        if czyPalindrom(z):
            nowehasla.append(z)
            continue
        for u in range(0, len(z)):
            stringtmp = z[:u]
            if czyPalindrom(stringtmp) and len(czyPalindrom(stringtmp)[1]) > najdluzsze:
                najdluzsze = czyPalindrom(stringtmp)[2]
                najdluzszy = czyPalindrom(stringtmp)[1]
        w2 = z.replace(najdluzszy, "")
        for indx2 in range(len(w2)-1, -1, -1):
            w3 += w2[indx2]
        w2 = ""
        pomoc = str(w3) + str(z)
        nowehasla.append(pomoc)
        pomoc = ""
        w3 = ""
        najdluzsze = 0
        najdluzszy = ""

zapis3 = open("hasla_b.txt", "w")

for u in nowehasla:
    zapis3.write(u + "\n")

zapis3.close()


dlugosc12 = []
najdluzsze = 0
najkrotsze = 99999
najdluzszestring = ""
najkrotszestring = ""
sumadlugosciwszystkichhasel = 0

for r in nowehasla:
    if len(r) == 12:
        dlugosc12.append(r)
    if len(r) > najdluzsze:
        najdluzsze = len(r)
        najdluzszestring = r
    if len(r) < najkrotsze:
        najkrotsze = len(r)
        najkrotszestring = r
    sumadlugosciwszystkichhasel += len(r)

zapis4 = open("slowa_b.txt", "w")
zapis4.write("1.")
for b in dlugosc12:
    zapis4.write(b + "\n")

zapis4.write("2." + "\n" + "Najdlusze haslo: " + str(najdluzszestring) + "\n")
zapis4.write("Najkrotsze haslo: " + str(najkrotszestring) + "\n")
zapis4.write("3." + "\n" + str(sumadlugosciwszystkichhasel))