plik = open("liczby1.txt", "r").readlines()
dane = []

for i in plik:
    i = i.strip()
    dane.append(i)

najwieksza = 0
najmniejsza = 999999999
odpnajwieksza = 0
odpnajmniejsza = 0

## zad 1
for b in dane:
    if najmniejsza > int(b, 8):
        najmniejsza = int(b, 8)
        odpnajmniejsza = b
    if najwieksza < int(b, 8):
        najwieksza = int(b, 8)
        odpnajwieksza = b

print(odpnajmniejsza, odpnajwieksza)

## zad 2
plik2 = open("liczby2.txt", "r").readlines()
dane2 = []

for z in plik2:
    z = z.strip()
    dane2.append(z)

pocz = 0
poczdl = 0
kon = 0
dlugosc = 0
najwiekszadlugosc = 0

for b in range(0, len(dane2)-1):
    if int(dane2[b], 10) <= int(dane2[b+1], 10) and pocz == 0:
        pocz = b
    if (int(dane2[b], 10) <= int(dane2[b+1], 10)) == False and pocz > 0:
        kon = b
        dlugosc = kon - pocz + 1
        if dlugosc == 6:
            poczdl = pocz
        pocz = 0
        kon = 0
    if dlugosc > najwiekszadlugosc:
        najwiekszadlugosc = dlugosc

print("\n")

print(najwiekszadlugosc)
for b in range(0, len(dane2)-1):
    if poczdl == b:
        for i in range(b, b+najwiekszadlugosc):
            print(dane2[i])

# Zad 3
iletakichwierszy = 0
for b in range(0, len(dane)):
    if int(dane[b], 8) == int(dane2[b]):
        iletakichwierszy += 1
print("\n")
print(iletakichwierszy)

ilewiekszych = 0
for e in range(0, len(dane)):
    if int(dane[e], 8) > int(dane2[e]):
        ilewiekszych += 1

print(ilewiekszych)

## Zad 4
def zamiananaosemkowy(liczba):
    osemkowo = ""
    doosemki = []
    while liczba != 0:
        doosemki.append(liczba%8)
        liczba = liczba // 8
    for i in range(len(doosemki)-1, -1, -1):
        osemkowo += str(doosemki[i])
    return osemkowo


ile6dzies= 0
for b in dane2:
    for indx in range(0, len(b)):
        if b[indx] == "6":
            ile6dzies += 1

print("\n")
print(ile6dzies)

plik3 = open("liczby3.txt", "w")

for i in range(0,len(dane2)):
    x = zamiananaosemkowy(int(dane2[i]))
    plik3.write(x)
    plik3.write("\n")

plik3.close()

plik4 = open("liczby3.txt", "r").readlines()
dane4 = []

for o in plik4:
    o = o.strip()
    dane4.append(o)

ile6wosemkowym = 0
for b in dane4:
    for indx2 in range(0, len(b)):
        if b[indx2] == "6":
            ile6wosemkowym += 1

print(ile6wosemkowym)

