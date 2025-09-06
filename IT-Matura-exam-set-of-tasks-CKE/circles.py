from math import sqrt
plik = open("okregi.txt", "r").readlines()
dane = []

for i in plik:
    i = i.split()
    dane.append(i)

ilew1 = 0
ilew2 = 0
ilew3 = 0
ilew4 = 0
ilewgl = 0

def czyOkregimajapunktwspolny(xs, ys, r, xs1, ys1, r1):
    if sqrt((xs1-xs) ** 2 + (ys1-ys) ** 2) == abs(r-r1):
        return True
    elif sqrt((xs1-xs) ** 2 + (ys1-ys) ** 2) == abs(r+r1):
        return True
    elif abs(r-r1) < sqrt((xs1-xs) ** 2 + (ys1-ys) ** 2) < abs(r+r1):
        return True
    else:
        return False


## Zad 1
for l in dane:
    if (float(l[0]) - float(l[2]) > 0) and (float(l[1]) - float(l[2]) > 0) and (float(l[1]) + float(l[2]) > 0) and (float(l[0]) + float(l[2]) > 0):
        ilew1 += 1
    elif (float(l[0]) - float(l[2]) < 0) and (float(l[1]) - float(l[2]) > 0) and (float(l[1]) + float(l[2]) > 0) and (float(l[0]) + float(l[2]) < 0):
        ilew2 += 1
    elif (float(l[0]) - float(l[2]) < 0) and (float(l[1]) - float(l[2]) < 0) and (float(l[1]) + float(l[2]) < 0) and (float(l[0]) + float(l[2]) < 0):
        ilew3 += 1
    elif (float(l[0]) - float(l[2]) > 0) and (float(l[1]) - float(l[2]) < 0) and (float(l[1]) + float(l[2]) < 0) and (float(l[0]) + float(l[2]) > 0):
        ilew4 += 1
    else:
        ilewgl += 1
print(ilew1, ilew2, ilew3, ilew4, ilewgl)
## Zad 2
lustrzanapara = 0
for m in range(0, len(dane)-1):
    for indx in range(m+1, len(dane)):
        if float(dane[m][2]) == float(dane[indx][2]):
            if float(dane[m][0]) == float(dane[indx][0]) * (-1):
                if float(dane[m][1]) == float(dane[indx][1]):
                    lustrzanapara += 1
            elif float(dane[m][1]) == float(dane[indx][1]) * (-1):
                if float(dane[m][0]) == float(dane[indx][0]):
                    lustrzanapara += 1
print(lustrzanapara)

## Zad 3
prostopadla = 0
for c in range(0, len(dane)-1):
    for indx1 in range(c+1, len(dane)):
        if float(dane[c][2]) == float(dane[indx1][2]):
            if (float(dane[c][0]) == float(dane[indx1][1]) * (-1)) and (float(dane[indx1][0]) == float(dane[c][1])):
                prostopadla += 1
            elif (float(dane[c][1]) * (-1) == float(dane[indx1][0])) and (float(dane[c][0]) == float(dane[indx1][1])):
                prostopadla += 1
print(prostopadla)

## Zad 4
lancuch = 1
najwiekszylancuch = 1
for b in range(1, 1000):
        if czyOkregimajapunktwspolny(float(dane[b][0]), float(dane[b][1]), float(dane[b][2]), float(dane[b-1][0]), float(dane[b-1][1]), float(dane[b-1][2])):
            lancuch += 1
            if b == 999 and lancuch > 1:
                print(lancuch)
        else:
            if najwiekszylancuch < lancuch:
                najwiekszylancuch = lancuch
            if lancuch > 1:
                print(str(lancuch) + "\n")
            lancuch = 1
print(najwiekszylancuch)

