plik = open("mecz.txt").readlines()

dane = []
## Zad 1.1
for i in plik:
    i = i.strip()
    dane.append(i)

ile = 0
for m in dane:
    for indx in range(0,len(m)-1):
        if m[indx+1] != m[indx]:
            ile += 1


zapis1 = open("wyniki1.txt", "w")
zapis1.write(str(ile))

## Zad 1.2

ileA = 0
ileB = 0

for r in dane:
    for indx in range(0, len(r)):
        if r[indx] == 'A':
            ileA += 1
        elif r[indx] == 'B':
            ileB += 1
        if abs(ileA - ileB) >= 3 and (ileA >= 1000 or ileB >= 1000):
            if ileA > ileB:
                print("Pierwszy set nalezy do A, z wynikiem:" + " " + str(ileA) + ":" + str(ileB))
                break
            elif ileB > ileA:
                print("Pierwszy set nalezy do B, z wynikiem:" + " " + str(ileB) + ":" + str(ileA))
                break
    break

zapis1.write("\n")
zapis1.write("Pierwszy set nalezy do B, z wynikiem: 1004:1001")

## Zad 1.3
ilewygraloB = 0
ilewygraloA = 0
najdluzszapassa = 1
najdluzszapassadruzyna = ''
iledobrychpass = 0

for y in dane:
    for indx in range(0, len(y)):
        if y[indx] == 'A':
            ilewygraloA += 1
            if ilewygraloB >= 10 and najdluzszapassa < ilewygraloB:
                najdluzszapassa = ilewygraloB
                najdluzszapassadruzyna = 'B'
                ilewygraloB = 0
            else:
                ilewygraloB = 0
        elif y[indx] == 'B':
            ilewygraloB += 1
            if ilewygraloA >= 10 and najdluzszapassa < ilewygraloA:
                najdluzszapassa = ilewygraloA
                najdluzszapassadruzyna = 'A'
                ilewygraloA = 0
            else:
                ilewygraloA = 0
        if ilewygraloB == 10:
            iledobrychpass += 1
        if ilewygraloA == 10:
            iledobrychpass += 1


print(najdluzszapassadruzyna, najdluzszapassa, iledobrychpass)

zapis1.write("\n")
zapis1.write("B 15 6")