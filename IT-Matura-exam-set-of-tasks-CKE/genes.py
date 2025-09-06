plik = open("dane_geny.txt", "r").readlines()
dane_geny=[]
gatunki = set()
maksymalnaliczba = 0
geny = []

def znajdzGen(dane_geny):
    geny = []
    ostatniapozycja = 0
    for i in range(0, len(dane_geny) - 1):
        if dane_geny[i] == "A" and dane_geny[i + 1] == "A":
            gen = ""
            if i >= ostatniapozycja:
                k = i
                for k in range(i, len(dane_geny) - 1):
                    if (dane_geny[k] == "B" and dane_geny[k + 1] == "B"):
                        ostatniapozycja = k
                        gen += "BB"
                        break
                    else:
                        gen += dane_geny[k]
            if gen.find("BB") > 0:
                geny.append(gen)

            gen = ""

    return geny

for i in plik:
    i = i.strip()
    dane_geny.append(i)
    geny.append(znajdzGen(i))


for l in range(0, len(dane_geny)):
    gatunki.add(len(dane_geny[l]))

for gat in gatunki:
    licznik = 0
    for gen in dane_geny:
        if len(gen) == gat:
            licznik += 1

    if licznik > maksymalnaliczba:
        maksymalnaliczba = licznik

print(len(gatunki), maksymalnaliczba)

## zad 2
licznik = 0

for wszystkiegeny in geny:
    for gen in wszystkiegeny:
        if gen.find("BCDDC") > -1:
            licznik += 1
            break
print(licznik)

## zad 3
liczbagenowujednegoosobnika = 0
najdluzszadlugoscgenu = 0

for m in geny:
    if len(m) > liczbagenowujednegoosobnika:
        liczbagenowujednegoosobnika = len(m)
for d in geny:
    for g in d:
        if len(g) > najdluzszadlugoscgenu:
            najdluzszadlugoscgenu = len(g)

print(liczbagenowujednegoosobnika, najdluzszadlugoscgenu)

## zad 4
odporny = 0
silnieodporny = 0

for f in range(0, len(dane_geny)):
    genotyp = dane_geny[f]
    licznik = 0
    for gen in geny[f]:
        if genotyp.find(gen[::-1]) > -1:
            licznik += 1

    if licznik == len(geny[f]):
        odporny += 1

for genotyp1 in dane_geny:
    if genotyp1[::] == genotyp1[::-1]:
        silnieodporny += 1
print(odporny, silnieodporny)

