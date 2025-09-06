from string import ascii_uppercase
from math import ceil

plik = open("tekst.txt", "r").readlines()
dane = []
dane2 = []

for i in plik:
    c = i.strip()
    i = i.split()
    dane.append(i)
    dane2.append(c)

iletakich = 0
for o in dane:
    for b in o:
        for indx in range(0, len(b)-1):
            if b[indx] == b[indx+1]:
                iletakich += 1
                break

print(iletakich)

## Zad 2

ileliter = {}

for z in dane2:
    for indx1 in range(0, len(z)):
        if z[indx1] in ileliter and z[indx1] != " ":
            ileliter[z[indx1]] += 1
        elif z[indx1] not in ileliter and z[indx1] != " ":
            ileliter[z[indx1]] = 1

uporzodkowanelitery = {}

klucze = sorted(ileliter.keys())

for s in klucze:
    uporzodkowanelitery[s] = ileliter[s]

for l in ascii_uppercase:
    if l not in uporzodkowanelitery:
        uporzodkowanelitery[l] = 0

suma = 0
procentlit = []
string = ""
tmp = 0
for procent in uporzodkowanelitery.values():
    suma += procent

klucze = []
wartosci = []



for z in ascii_uppercase:
    b = uporzodkowanelitery[z]
    tmp = round(float((uporzodkowanelitery[z] / suma) * 100), 2)
    string = str(z) + ": " + str(b) + " " + str(tmp) + "%"
    procentlit.append(string)

print(procentlit)


najdluzszadlugosc = 0
dlugosc = 1
aktualnanajwiekszadlugosc = 1

samogloski = ['A', 'E', 'I', 'O', 'U', 'Y']
for t in dane:
    for element in t:
        for indx2 in range(0, len(element)-1):
            if element[indx2] not in samogloski and element[indx2+1] not in samogloski:
                dlugosc += 1
            else:
                if dlugosc >= aktualnanajwiekszadlugosc:
                    aktualnanajwiekszadlugosc = dlugosc
                dlugosc = 1
        if aktualnanajwiekszadlugosc > najdluzszadlugosc:
            najdluzszadlugosc = aktualnanajwiekszadlugosc
        dlugosc = 1
        aktualnanajwiekszadlugosc = 1

print(najdluzszadlugosc)
licznik = 0
for t in dane:
    for element in t:
        for indx2 in range(0, len(element)-1):
            if element[indx2] not in samogloski and element[indx2+1] not in samogloski:
                dlugosc += 1
            else:
                if dlugosc >= aktualnanajwiekszadlugosc:
                    aktualnanajwiekszadlugosc = dlugosc
                dlugosc = 1
        if aktualnanajwiekszadlugosc == najdluzszadlugosc:
            licznik += 1
            if licznik == 1:
                print(element)
        dlugosc = 1
        aktualnanajwiekszadlugosc = 1

print(licznik)