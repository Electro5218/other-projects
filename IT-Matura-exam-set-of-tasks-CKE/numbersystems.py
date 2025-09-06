import math

plik = open("dane_systemy1.txt", "r").readlines()
plik2 = open("dane_systemy2.txt", "r").readlines()
plik3 = open("dane_systemy3.txt", "r").readlines()

dane = []
dane2 = []
dane3 = []

for i in plik:
    i = i.split()
    dane.append(i)

for i in plik2:
    i = i.split()
    dane2.append(i)

for i in plik3:
    i = i.split()
    dane3.append(i)

najnizszatemperatura1 = 999999999999
najnizszatemperatura2 = 999999999999
najnizszatemperatura3 = 999999999999
## Zad 1
for o in dane:
    x = int(o[1], 2)
    if x < najnizszatemperatura1:
        najnizszatemperatura1 = x

for o in dane2:
    x = int(o[1], 4)
    if x < najnizszatemperatura2:
        najnizszatemperatura2 = x

for o in dane3:
    x = int(o[1], 8)
    if x < najnizszatemperatura3:
        najnizszatemperatura3 = x

def dectobin(liczba):
    czyujemna = False
    if liczba == 0:
        return 0
    elif liczba < 0:
        liczba = liczba * (-1)
        czyujemna = True
    dec = ""
    decodp = ""
    while liczba != 0:
        if czyujemna:
            decodp = "-"
            czyujemna = False
        dec += str(liczba % 2)
        liczba = liczba // 2
    for i in range(len(dec)-1, -1, -1):
        decodp += dec[i]
    return decodp



print(dectobin(najnizszatemperatura1))
print(dectobin(najnizszatemperatura2))
print(dectobin(najnizszatemperatura3))

## Zad 2

niepoprawne = 0
for y in range(0, len(dane)):
    if int(dane[y][0], 2) % 12 != 0 and int(dane2[y][0], 4) % 12 != 0 and int(dane3[y][0], 8) % 12 != 0:
        niepoprawne += 1

print(niepoprawne)

## Zad 3

dnirekordowe = 0
rekordowatemperatura = int(dane[0][1], 2)
rekordowatemperatura2 = int(dane[0][1], 4)
rekordowatemperatura3 = int(dane[0][1], 8)

for e in range(1, len(dane)):
    if int(dane[e][1], 2) > rekordowatemperatura or int(dane2[e][1], 4) > rekordowatemperatura2 or int(dane3[e][1], 8) > rekordowatemperatura3:
        dnirekordowe += 1
    if int(dane[e][1], 2) > rekordowatemperatura:
        rekordowatemperatura = int(dane[e][1], 2)
    if int(dane2[e][1], 4) > rekordowatemperatura2:
        rekordowatemperatura2 = int(dane2[e][1], 4)
    if int(dane3[e][1], 8) > rekordowatemperatura3:
        rekordowatemperatura3 = int(dane3[e][1], 8)

print(dnirekordowe)

## Zad 4
rij = 0
skok = 0
najwiekszyskok = 0
for b in range(0, len(dane)):
    for z in range(b+1, len(dane)):
       rij = (int(dane[b][1], 2) - int(dane[z][1], 2)) ** 2
       skok = math.ceil(rij / abs((b+1)-(z+1)))
       if skok > najwiekszyskok:
           najwiekszyskok = skok

print(najwiekszyskok)