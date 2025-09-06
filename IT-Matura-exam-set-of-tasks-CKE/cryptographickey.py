plik = open("tekst.txt", "r").readlines()
dane = []

for i in plik:
    i = i.split()
    dane.append(i)

for z in dane:
    for indx in range(0,len(z)):
        if z[indx][0] == 'd' and z[indx][-1] == 'd':
            print(z[indx])
## zad 2
klucz = ['5', '2']
print("\n")
zaszyfrowanystring = ""
for b in dane:
    for indx1 in range(0, len(b)):
        if len(b[indx1]) >= 10:
            for len1 in range(0, len(b[indx1])):
                x = (int(klucz[0]) * (ord(b[indx1][len1]) - 97)) + int(klucz[1])
                if x > 25:
                    x = (x % 26) + 97
                    zaszyfrowanystring += chr(x)
                elif x <=25:
                    zaszyfrowanystring += chr(x+97)
            print(zaszyfrowanystring)
            zaszyfrowanystring = ""
## zad 3
plik3 = open("probka.txt", "r").readlines()
dane3 = []

for n in plik3:
    n = n.split()
    dane3.append(n)

zaszyfrowanystring = ""

for k in dane3:
    for j in range(0, 26):
        for z in range(0, 26):
            A = j
            B = z
            for u in range(0,len(k[0])):
                x = (((ord(k[0][u]) - 97) * A) + B)
                if x > 25:
                    x = (x % 26) + 97
                    zaszyfrowanystring += chr(x)
                else:
                    zaszyfrowanystring += chr(x+97)
            if zaszyfrowanystring == k[1]:
                print("znaleziono klucz szyfrujacy:" + " " + str(A) + " " + str(B))
            zaszyfrowanystring = ""

odszyfrowanystring = ""
for c in dane3:
    for l in range(0, 26):
        for m in range(0, 26):
            A = l
            B = m
            for n in range(0,len(c[1])):
                x = (((ord(c[1][n]) - 97) * A) + B)
                if x > 25:
                    x = (x % 26) + 97
                    odszyfrowanystring += chr(x)
                else:
                    odszyfrowanystring += chr(x+97)
            if odszyfrowanystring == c[0]:
                print("znaleziono klucz deszyfrujący:" + " " + str(A) + " " + str(B))
            odszyfrowanystring = ""