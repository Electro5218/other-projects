from math import sqrt

plik = open("wspolrzedne.txt", "r").readlines()
dane = []

for i in plik:
    i = i.split()
    dane.append(i)

czyniepoprawne = False
iletakich = 0
## zad 1
for m in dane:
    for indx1 in range(0, len(m)):
        if int(m[indx1]) != 0 and int(m[indx1]) > 0:
            czyniepoprawne = False
        else:
            czyniepoprawne = True
            break
    if czyniepoprawne == False:
        iletakich += 1

print(iletakich)

## zad 2

def wspolczynnikkierunkowy(xa, ya, xb, yb, xc, yc):

    if xa - xb != 0:
        a_ab = (ya - yb) / (xa - xb)
    else:
        a_ab = 0
    if xa - xc != 0:
        a_ac = (ya - yc) / (xa - xc)
    else:
        a_ac = 0
    return a_ab, a_ac


iletakich2 = 0
iteracja3 = 0
for v in dane:
    iteracja3 += 1
    if v[0] == v[2] == v[4]:
        iletakich2 += 1
        continue
    elif v[0] == v[2] and v[0] != v[4]:
        if v[1] == v[3]:
            iletakich2 += 1
            continue
        else:
            continue
    else:

        if wspolczynnikkierunkowy(int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4]), int(v[5]))[0] == wspolczynnikkierunkowy(int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4]), int(v[5]))[1] != 0:
            iletakich2 += 1
            continue
        elif wspolczynnikkierunkowy(int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4]), int(v[5]))[0] == wspolczynnikkierunkowy(int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4]), int(v[5]))[1] == 0:
            if v[1] == v[3] == v[5]:
                iletakich2 += 1
                continue


print(iletakich2)

## zad 3

## boki
bok1 = []
bok2 = []
bok3 = []

plik2 = open("wspolrzedneTR.txt", "r").readlines()
dane2 = []

for x in plik2:
    x = x.split()
    dane2.append(x)

for m in dane2:
    bok1.append(sqrt((int(m[2])-int(m[0]))**2+(int(m[3])-int(m[1]))**2))
    bok2.append(sqrt((int(m[4])-int(m[0]))**2+(int(m[5])-int(m[1]))**2))
    bok3.append(sqrt((int(m[4])-int(m[2]))**2+(int(m[5])-int(m[3]))**2))

obw = 0
najwobw = 0
wspolrzednenajwobw = ''

for indx2 in range(0, len(dane2)):
    obw = round(bok1[indx2] + bok2[indx2] + bok3[indx2], 2)
    if obw > najwobw:
        najwobw = obw
        wspolrzednenajwobw = dane2[indx2]

print(najwobw, wspolrzednenajwobw)

## Zad 4
ilosctrojkatowprostokatnychwpliku = 0

for indx3 in range(0, len(dane2)):
    kw1 = (int(dane2[indx3][4]) - int(dane2[indx3][2])) * (int(dane2[indx3][4]) - int(dane2[indx3][2])) + (int(dane2[indx3][5]) - int(dane2[indx3][3])) * (int(dane2[indx3][5]) - int(dane2[indx3][3]))
    kw2 = (int(dane2[indx3][4]) - int(dane2[indx3][0])) * (int(dane2[indx3][4]) - int(dane2[indx3][0])) + (int(dane2[indx3][5]) - int(dane2[indx3][1])) * (int(dane2[indx3][5]) - int(dane2[indx3][1]))
    kw3 = (int(dane2[indx3][0]) - int(dane2[indx3][2])) * (int(dane2[indx3][0]) - int(dane2[indx3][2])) + (int(dane2[indx3][1]) - int(dane2[indx3][3])) * (int(dane2[indx3][1]) - int(dane2[indx3][3]))

    if (kw1==kw2+kw3) or (kw2==kw1+kw3) or (kw3==kw2+kw1):
        ilosctrojkatowprostokatnychwpliku += 1

print(ilosctrojkatowprostokatnychwpliku)

## Zad 5
iletakichpunktowd = 0

for indx4 in range(0, len(dane2)):
    xd = int(dane2[indx4][0]) + int(dane2[indx4][4]) - int(dane2[indx4][2])
    yd = int(dane2[indx4][1]) + int(dane2[indx4][5]) - int(dane2[indx4][3])

    if (xd == yd):
        iletakichpunktowd += 1
        print(dane2[indx4])

print(iletakichpunktowd)