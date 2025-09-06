plik = open("hasla.txt", "r").readlines()

dane = []

for i in plik:
    i = i.strip()
    dane.append(i)
## zad 1
licznik = 0
liczbahasel = 0
for o in dane:
    for indx in range(0, len(o)):
        if o[indx].isdigit():
           licznik += 1
    if licznik == len(o):
        liczbahasel += 1
    licznik = 0

print(liczbahasel)

zad2odpowiedzi = []
## zad 2

for m in range(0, len(dane)):
    for v in range(m+1, len(dane)-1):
        if dane[m] == dane[v]:
            zad2odpowiedzi.append(dane[m])

x = sorted(zad2odpowiedzi)

for element in x:
    print(element)

## zad 3
iletakichuzytkownikow = 0


for n in dane:
    for indx1 in range(0, len(n)-3):
        tablica = []
        a = n[indx1]
        b = n[indx1+1]
        c = n[indx1+2]
        d = n[indx1+3]
        tablica.append(a)
        tablica.append(b)
        tablica.append(c)
        tablica.append(d)
        tablica = sorted(tablica)
        if ord(tablica[3]) - 1 == ord(tablica[2]) and ord(tablica[2]) - 1 == ord(tablica[1]) and ord(tablica[1]) - 1 == ord(tablica[0]) and len(n) >= 4:
            iletakichuzytkownikow += 1
            break
        tablica = ""

print(iletakichuzytkownikow)

## zad 4
czyzawieracyfre = False
czyzawieramalalitere = False
czyzawieraduzalitere = False

iletakichcospelniawymagania = 0
for o in dane:
    for indx2 in range(0, len(o)):
        if o[indx2].isdigit():
            czyzawieracyfre = True
        if o[indx2].isupper():
            czyzawieraduzalitere = True
        if o[indx2].islower():
            czyzawieramalalitere = True
        if czyzawieraduzalitere and czyzawieramalalitere and czyzawieracyfre:
            iletakichcospelniawymagania += 1
            break
    czyzawieracyfre = False
    czyzawieramalalitere = False
    czyzawieraduzalitere = False

print(iletakichcospelniawymagania)
