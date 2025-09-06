plik = open("szyfr1.txt", "r").readlines()

dane = []

for i in plik:
    i = i.split()
    dane.append(i)

klucz = dane[6]




for b in dane[:-1]:
    for c in b:
        string = c
        string = list(string)
        stringnormalny = ""
        for indx1 in range(0, len(c)):
            x = int(klucz[indx1]) - 1
            string[indx1], string[x] = string[x], string[indx1]
    for l in string:
        stringnormalny += l
    print(stringnormalny)
    stringnormalny = ""
    string = ""

## Zad 2

plik2 = open("szyfr2.txt", "r").readlines()

tekst = plik2[0].strip()
tekst = list(tekst)
klucz = plik2[1].split()
ktorywziac = 0
print("\n")
for b in range(0, len(tekst)):
    if ktorywziac == 15:
        ktorywziac = 0
    x = int(klucz[ktorywziac]) - 1
    tekst[b], tekst[x] = tekst[x], tekst[b]
    ktorywziac += 1

zaszyfrowanystring = ""
for z in tekst:
    zaszyfrowanystring += z

print(zaszyfrowanystring)

## Zad 3
plik3 = open("szyfr3.txt", "r").readlines()

tekst = plik3[0].strip()
tekst = list(tekst)
klucz = "624153"
print("\n")
ktorywziac = 1

for b in range(len(tekst) - 1, -1, -1):
    if ktorywziac == -1:
        ktorywziac = 5
    x = int(klucz[ktorywziac]) - 1
    tekst[x], tekst[b] = tekst[b], tekst[x]
    ktorywziac -= 1

zaszyfrowanystring = ""
for z in tekst:
    zaszyfrowanystring += z

print(zaszyfrowanystring)
