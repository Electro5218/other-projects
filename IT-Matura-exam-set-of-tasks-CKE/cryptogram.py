## zad 1
plik = open("szyfrogram.txt", "r")
dane = []
for i in plik:
    i = i.strip()
    dane.append(i)

litery = {}
for l in dane:
    l = sorted(l)
    for g in l:
        if g in litery:
            litery[g] += 1
        elif g not in litery:
            litery[g] = 1

litery['Q'] = 0
litery['G'] = 0
litery['S'] = 0


print(str(litery))

## zad 2
plik2 = open("czestosc.txt", "r")
dane2 = []
for g in plik2:
    g = g.split()
    dane2.append(g)

zaszyfrowaneslowo = [98, 41, 17, 86, 38, 31, 32, 36]
odszyfrowaneslowo = []

for h in zaszyfrowaneslowo:
    for b in dane2:
        if str(h) == b[1]:
            odszyfrowaneslowo.append(b[0])

strodszyfrowaneslowo = ""

for v in odszyfrowaneslowo:
    strodszyfrowaneslowo += v

print(strodszyfrowaneslowo)

## zad 3
slowa = []
slowaoddzielone = []
szyfr = []

for z in litery:
        slowa.append(z + " " + str(litery[z]))

for m in slowa:
    m = m.split()
    slowaoddzielone.append(m)


for x in dane:
    for l in x:
        for t in slowaoddzielone:
            if str(l) == str(t[0]):
                for d in dane2:
                    if str(t[1]) == str(d[1]):
                        szyfr.append(str(d[0]))

strszyfrogram = ""
for e in szyfr:
    strszyfrogram += e

print(strszyfrogram)