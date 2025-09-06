plik = open("dane_obrazki.txt", "r").readlines()

dane = []
dane2 = []
stringtmp = ''
stringtmp2 = ''
stringtmp3 = ''
stringtmp4 = ''
stringtmp5 = ''
tablicaobrazku = []
obrazek = ''
nowatablica = []
string1 = ''
string2 = ''
string3 = ''
string4 = ''

# dane = plik.split('\n\n')

for b in plik:
    b = b.strip()
    stringtmp += b[:-1]
    if b == '':
        nowatablica.append(stringtmp)
        stringtmp = ''


## Zad 1

Obrazekpikseleczarne = 0
obrazekpiskelebiale = 0
makspikseleczarne = 0
numerobrazka = 0
rewers = 0

for l in nowatablica:
    for indx in range(0, len(l)-19):
        if l[indx] == "0":
            obrazekpiskelebiale += 1
        elif l[indx] == "1":
            Obrazekpikseleczarne += 1
    if obrazekpiskelebiale < Obrazekpikseleczarne:
        rewers += 1
        if makspikseleczarne < Obrazekpikseleczarne:
            makspikseleczarne = Obrazekpikseleczarne
    obrazekpiskelebiale = 0
    Obrazekpikseleczarne = 0

print(rewers, makspikseleczarne)

## Zad 2

pierwszaczescobrazka = []
drugaczescobrazka = []
trzeciaczescobrazka = []
czwartaczescobrazka = []

## 1 część n/2 x n/2
o = 0
licznik3 = 0
for y in range(0, len(plik)):
    licznik3 += 1
    if o > 0:
        o = o + 1
        y = o
    if y == 4388:
        break
    if licznik3 == 11:
        y = y + 12
        o = y
        pierwszaczescobrazka.append(stringtmp2)
        stringtmp2 = ''
        licznik3 = 1
    z = plik[y].strip()
    stringtmp2 += z[:-11]


# ## 2 część n/2 x n/2

t = 0
licznik4 = 0
for n in range(0, len(plik)):
    licznik4 += 1
    if t > 0:
        t = t + 1
        n = t
    if n == 4388:
        break
    if licznik4 == 11:
        n = n + 12
        t = n
        drugaczescobrazka.append(stringtmp3)
        stringtmp3 = ''
        licznik4 = 1
    u = plik[n].strip()
    stringtmp3 += u[10:20]

## 3 część n/2 x n/2

m = 0
licznik = 0
for c in range(10, len(plik)):
    licznik += 1
    if m > 0:
        m = m + 1
        c = m
    if c == 4398:
        break
    if licznik == 11:
        c = c + 12
        m = c
        trzeciaczescobrazka.append(stringtmp4)
        stringtmp4 = ''
        licznik = 1
    b = plik[c].strip()
    stringtmp4 += b[0:10]

## 4 część n/2 x n/2

v = 0
licznik2 = 0
for e in range(10, len(plik)):
    licznik2 += 1
    if v > 0:
        v = v + 1
        e = v
    if e == 4398:
        break
    if licznik2 == 11:
        e = e + 12
        v = e
        czwartaczescobrazka.append(stringtmp5)
        stringtmp5 = ''
        licznik2 = 1
    x = plik[e].strip()
    stringtmp5 += x[10:20]

Rekurencyjne = 0
licznikpomoc = 1
for indx4 in range(0, len(pierwszaczescobrazka)):
    if pierwszaczescobrazka[indx4] == drugaczescobrazka[indx4] == trzeciaczescobrazka[indx4] == czwartaczescobrazka[indx4]:
        Rekurencyjne += 1
        if licznikpomoc == 1:
            v = nowatablica[indx4]
            print(v[:-19])
            licznikpomoc += 1

print(Rekurencyjne)

copowinnobyc = 4
bityparzystoscipion = []
bityparzystoscipoziom = []
zliczanie = 0
zle = 0

## Zad 3
licznik6 = 0
zlepoziom = 0
s = 0
zlepoziomobrazy = []

## poziom
for indx5 in range(0, len(plik)):
    if s > 0:
        indx5 = s
        s = indx5 + 1
    licznik6 += 1
    h = plik[indx5].strip()
    for indx2 in range(0, len(h)-1):
        if plik[indx5][indx2] == '1':
            zliczanie += 1
    if zliczanie % 2 == 0:
        copowinnobyc = 0
    else:
        copowinnobyc = 1
    if str(copowinnobyc) != plik[indx5][indx2+1]:
      zlepoziom += 1
    zliczanie = 0
    if licznik6 == 20:
        zlepoziomobrazy.append(zlepoziom)
        s = indx5 + 3
        licznik6 = 0
    if indx5 == 4397:
        break

## pion
licznik7 = 0
licznik8 = 0
zlepion = 0
indeksdobry = 19
pomocniczazindx = 0
iloscpowtorzen = 0
r = 0
r1 = 0
zlepionobrazy = []


for indx6 in range(0, len(plik)):
    r = indx6
    if r >= 20:
        r = indx6 % 20
        indx6 = r
    licznik7 += 1
    iloscpowtorzen += 1
    for indx4 in range(0, len(plik)):
        if r1 >= 400:
            indx4 = indeksdobry + 3
            indeksdobry = indeksdobry + 22
            pomocniczazindx = indx4
            r1 = 0
        if pomocniczazindx > 0 and indx4 % 22 == 0 and indx4 > 20:
            pomocniczazindx = pomocniczazindx - 1
        if pomocniczazindx > 0:
            indx4 = pomocniczazindx + 1
            pomocniczazindx = indx4
        licznik8 += 1
        if licznik8 == 20 and indx4 > 20:
            pomocniczazindx = pomocniczazindx - 21
        if licznik8 == 21 and indx4 >= 20:
            r1 = r1 + (licznik8 - 1)
            licznik8 = 0
            break
        if plik[indx4][indx6].strip() == '1':
            zliczanie += 1
        if licznik8 == 20 and indx4 <= 20:
            r1 = r1 + licznik8
            licznik8 = 0
            break
    if zliczanie % 2 == 0:
        copowinnobyc = 0
        zliczanie = 0
    else:
        copowinnobyc = 1
        zliczanie = 0
    if pomocniczazindx == 0:
        if str(copowinnobyc) != plik[pomocniczazindx+20][indx6]:
            zlepion += 1
    else:
        if str(copowinnobyc) != plik[pomocniczazindx+21][indx6]:
            zlepion += 1
    if licznik7 == 20:
        zlepionobrazy.append(zlepion)
        licznik7 = 0
    if iloscpowtorzen == 4000:
        break

naprawialne = 0
poprawne = 0
nienaprawialne = 0

for kar in range(0, len(zlepionobrazy)):
    z = zlepionobrazy[kar]
    z = int(z)
    q = zlepoziomobrazy[kar]
    q = int(q)
    if z == 0 and q == 0:
        poprawne += 1
    elif (z == 1 or q == 1) and (z <= 1 and q <= 1):
        naprawialne += 1
    elif z > 1 or q > 1 and (z >= 1 and q >= 1):
        nienaprawialne += 1


print(poprawne, naprawialne, nienaprawialne)