from math import sqrt

plik = open("liczby1.txt", "r")
dane = []

for i in plik:
    i = i.strip()
    dane.append(int(i))

## Zad 1
iletakich1= 0
for t in dane:
    licznik = 0
    k = 2
    while t != 1:
        while t % k == 0:
            t //= k
            licznik += 1
        k += 1
    if licznik > 5:
        iletakich1 += 1

czynniki = []

print(iletakich1)

def rozloz(n):
    czynniki1 = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki1.append(k)
        k += 1

    return czynniki1

czynniki2 = []

for b in range(0, len(dane)):
    czynniki2.append(rozloz(dane[b]))

odpowiedz = 0
for v in range(0, len(czynniki2)):
    unikalne = set(czynniki2[v])
    if len(unikalne) > 4:
        odpowiedz += 1

print(odpowiedz)

flaga = True
odpowiedz2 = 0
for l in czynniki2:
    for indx in range(0, len(l)-1):
        if l[indx] == l[indx+1]:
            flaga = False
    if flaga == True:
        odpowiedz2 += 1
    flaga == True

print(odpowiedz2)


## Zad 2

def rozloz(n):
    czynniki = []
    skladnik = 0
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
            skladnik += 1
        k += 1
    return czynniki, skladnik

najwieksza = 0
czynniki_najwieksze = 0

for z in dane:
    if rozloz(z)[1] >= najwieksza:
        najwieksza = rozloz(z)[1]
        czynniki_najwieksze = rozloz(z)[0]

def rozloz2(n):
    czynniki = []
    skladnik = 0
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki

liczba = 0

for a in dane:
    dlugosc = 0
    dlugosc = len(rozloz2(a))
    dlugoscporownywania = len(czynniki_najwieksze)
    if dlugosc == dlugoscporownywania:
        liczba = a


print(liczba, najwieksza)

## Zad 3
def isPrime(n):
    if n < 2:
        return False
    for y in range(2, n):
        if n % y == 0:
            return False
    return True

licznik4 = 0
for z in dane:
    if isPrime(z) == True:
        licznik4 += 1

print(licznik4)

## Zad 4
def pierwszydzielnik(a):
    for i in range(2, int(sqrt(a))+1):
        if(a%i == 0):
            return i
    return 0

def liczbapolpierwsza(a):
    dzielnik = pierwszydzielnik(a)
    return (dzielnik != 0 and pierwszydzielnik(a / dzielnik) == 0)

licznik6 = 0
for e in dane:
    if liczbapolpierwsza(e) == True:
        licznik6 += 1

print(licznik6)

## Zad 5

plik2 = open("liczby2.txt", "r")
dane2 = []
for n in plik2:
    n = n.strip()
    dane2.append(int(n))

czynniki3 = []
for f in dane2:
    czynniki3.append(rozloz2(f))


licznikodp = 0
for v in range(0, len(czynniki2)):
    if len(czynniki2[v]) == len(czynniki3[v]):
        licznikodp += 1

print(licznikodp)

czynniki2bezpowtorzen = []
czynniki3bezpowtorzen = []

for d in czynniki2:
    d = set(d)
    czynniki2bezpowtorzen.append(d)

for u in czynniki3:
    u = set(u)
    czynniki3bezpowtorzen.append(u)

odp5b = 0
for y in range(0, len(czynniki3bezpowtorzen)):
    if czynniki3bezpowtorzen[y] == czynniki2bezpowtorzen[y]:
        odp5b += 1

print(odp5b)

##zad 6
def nwd(a, b):
    if b>0:
        return nwd(b, a%b)
    else:
        return a

wzgledniepierwsze = 0
for r in range(0, len(dane)):
    if nwd(dane[r], dane2[r]) == 1:
        wzgledniepierwsze += 1

print(wzgledniepierwsze)

## zad 7
najwiekszanwd = 0
najwiekszanwdmax = 0
liczba1 = 0
liczba2 = 0

for l in range(0, len(dane)):
    najwiekszanwd = nwd(dane[l], dane2[l])
    if najwiekszanwdmax < najwiekszanwd:
        najwiekszanwdmax = najwiekszanwd
        liczba1 = dane[l]
        liczba2 = dane2[l]

print(najwiekszanwdmax, liczba1, liczba2)

najwiekszynwd = 0
najwiekszynwdmax = 0
liczba1zad7b = 0
liczba2zad7b = 0
for z in range(0, len(dane2)-1):
    for b in range(0, len(dane2)-1):
        if dane2[z] != dane2[b+1]:
            najwiekszynwd = nwd(dane2[z], dane2[b+1])
        if najwiekszynwd > najwiekszynwdmax:
            najwiekszynwdmax = najwiekszynwd
            liczba1zad7b = dane2[z]
            liczba2zad7b = dane2[b+1]

print(najwiekszynwdmax, liczba1zad7b, liczba2zad7b)

