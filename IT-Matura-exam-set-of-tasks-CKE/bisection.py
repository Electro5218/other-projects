import numpy as np

plik = open("funkcja.txt", "r").readlines()

dane = []

for i in plik:
    i = i.strip()
    i = [float(i) for i in i.split()]
    dane.append(i)

print(dane)

def polowienie_rekurencja(funkcja, dokladnosc=0.00001, x1=10.0, x2=-10.0):
    y1 = funkcja(x1)
    y2 = funkcja(x2)
    # jeśli dwa te same punkty są po tej "samej" stronie wykresu
    if y1 * y2 > 0:
        return False

    # pierwszy x z punkty_x to jest "górny x", a drugi jest "dolnym"
    # pierwszy f(x) > 0, drugi jest < 0

    if abs(x1 - x2) < dokladnosc and (y1*y2<=0):
        return ((x1+x2)/2)
    else:
        x3=(x1+x2)/2
        y3=funkcja(x3)
        if(y1*y3)<0:
            return polowienie_rekurencja(funkcja, dokladnosc, x1, x3)
        else:
            return polowienie_rekurencja(funkcja, dokladnosc, x2, x3)


def funkcjadlazad1(y):
    return dane[1][0] + dane[1][1]*y + dane[1][2]*(y**2) + dane[1][3]*(y**3)

print(funkcjadlazad1(1.5))


wartosc = []

for l in range(0, 1):
    d = l
    while(d<1):
        k = d
        d = k + 0.001
        wartosc.append(dane[l][0] + dane[l][1] * d + dane[l][2] * (d ** 2) + dane[l][3] * (d ** 3))

for t in range(1, 2):
    h = t
    while(h<2):
        k = h
        h = k + 0.001
        wartosc.append(dane[t][0] + dane[t][1] * h + dane[t][2] * (h ** 2) + dane[t][3] * (h ** 3))
for y in range(2, 3):
    j = y
    while (j < 3):
        k = j
        j = k + 0.001
        wartosc.append(dane[y][0] + dane[y][1] * j + dane[y][2] * (j ** 2) + dane[y][3] * (j ** 3))
for c in range(3, 4):
    e = c
    while (e < 4):
        k = e
        e = k + 0.001
        wartosc.append(dane[c][0] + dane[c][1] * e + dane[c][2] * (e ** 2) + dane[c][3] * (e ** 3))
for v in range(4, 5):
    z = v
    while (z < 5):
        k = z
        z = k + 0.001
        wartosc.append(dane[v][0] + dane[v][1] * z + dane[v][2] * (z ** 2) + dane[v][3] * (z ** 3))

def dlajakiegoxnajwiekszawartosc(y):
    for l in range(0, 1):
        d = l
        while (d < 1):
            k = d
            d = k + 0.001
            if dane[l][0] + dane[l][1] * d + dane[l][2] * (d ** 2) + dane[l][3] * (d ** 3) == y:
                return d

    for t in range(1, 2):
        h = t
        while (h < 2):
            k = h
            h = k + 0.001
            if dane[t][0] + dane[t][1] * h + dane[t][2] * (h ** 2) + dane[t][3] * (h ** 3) == y:
                return h
    for g in range(2, 3):
        j = g
        while (j < 3):
            k = j
            j = k + 0.001
            if dane[g][0] + dane[g][1] * j + dane[g][2] * (j ** 2) + dane[g][3] * (j ** 3) == y:
                return j
    for c in range(3, 4):
        e = c
        while (e < 4):
            k = e
            e = k + 0.001
            if dane[c][0] + dane[c][1] * e + dane[c][2] * (e ** 2) + dane[c][3] * (e ** 3) == y:
                return e
    for v in range(4, 5):
        z = v
        while (z < 5):
            k = z
            z = k + 0.001
            if dane[v][0] + dane[v][1] * z + dane[v][2] * (z ** 2) + dane[v][3] * (z ** 3) == y:
                return z

print(round(max(wartosc), 5))
print(round(dlajakiegoxnajwiekszawartosc(3.064950978777574), 5))

print("zad3:")


def funkcja(y):
    return dane[x][3] * (y ** 3) + dane[x][2] * (y ** 2) + dane[x][1] * y + dane[x][0]
for x in range(5):
    if(polowienie_rekurencja(funkcja, dokladnosc=0.001, x1=x, x2=x+0.99999)==False):
        print("BRAK")
    else:
        print(round(polowienie_rekurencja(funkcja, dokladnosc=0.001, x1=x, x2=x+0.99999),5))

