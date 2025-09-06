plik = open("dane_ulamki.txt", "r").readlines()

dane = []

for i in plik:
    i = i.split()
    dane.append(i)

wartosc = 0
minimalnawartosc = 999999999999999999999999999
for b in dane:
    wartosc = int(b[0]) / int(b[1])
    if wartosc < minimalnawartosc:
        minimalnawartosc = wartosc

minimalnewartosci = []

for e in dane:
    wartosc = int(e[0]) / int(e[1])
    if wartosc == minimalnawartosc:
        minimalnewartosci.append(wartosc)

for t in dane:
    wartosc = int(t[0]) / int(t[1])
    if wartosc == minimalnewartosci[0]:
        print(t)
        break

## Zad 2

def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    return a
def NWW(a,b):
    return (a*b)/NWD(a,b)

def czywzgledniepierwsze(liczba1, liczba2):
    if NWD(liczba1, liczba2) == 1:
        return True
    else:
        return False

ilenieskracalnych = 0
for b in dane:
    if czywzgledniepierwsze(int(b[0]), int(b[1])):
        ilenieskracalnych += 1

print(ilenieskracalnych)

def skrocenieizwrocenielicznika(licznik, mianownik):
    if czywzgledniepierwsze(licznik, mianownik):
        return licznik
    else:
        while czywzgledniepierwsze(licznik, mianownik) != 1:
            nwd = NWD(licznik, mianownik)
            licznik = licznik / nwd
            mianownik = mianownik / nwd
    return licznik



## zad 3
suma = 0
for y in dane:
    x = skrocenieizwrocenielicznika(int(y[0]), int(y[1]))
    suma += x

print(suma)

## zad 4
b = (2**2)*(3**2)*(5**2)*(7**2)*13

suma = 0
for r in dane:
    x = int(r[0]) / int(r[1])
    suma += x * b

print(suma)
