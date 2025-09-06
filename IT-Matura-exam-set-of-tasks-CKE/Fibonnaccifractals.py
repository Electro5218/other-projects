def fib(n):
    t = [1, 1]
    for i in range(2, n):
        t.append(t[i - 2] + t[i - 1])
    return t[-1]


def pierwsza(g):
    if g == 2:
        return True
    if g % 2 == 0:
        return False
    if g == 1:
        return False
    for l in range(2, g):
        if g % l == 0:
            return False
    return True


## Zad 1

print(fib(10), fib(20), fib(30), fib(40))

## Zad 2

for i in range(1, 41):
    if pierwsza(fib(i)) == True:
        print(fib(i))

## Zad 3
fraktalniebinarnyFibonnaci = []
fraktalbinarny = []
fraktalbinarny1 = []
potrzebnedozad6 = []

for l in range(1, 41):
    fraktalniebinarnyFibonnaci.append(fib(l))

for v in fraktalniebinarnyFibonnaci:
    x = bin(v)
    fraktalbinarny.append(x[2:])
    fraktalbinarny1.append(x[2:])

for m in range(0, 39):
    r = len(fraktalbinarny[39]) - len(fraktalbinarny[m])
    if r > 0:
        for j in range(0, r):
            fraktalbinarny[m] = "0" + fraktalbinarny[m]
    print(fraktalbinarny[m])
    potrzebnedozad6.append(fraktalbinarny[m])

print("  ")

tylesamozer = []
szescjedynek = []
licznik = 0
licznik2 = 0
for k in fraktalbinarny1:
    for indx1 in range(0,len(k)):
        if k[indx1] == "1":
            licznik += 1
        if k[indx1] == "0":
            licznik2 += 1
    if licznik == 6:
        szescjedynek.append(k)
    if licznik == licznik2:
        tylesamozer.append(k)
    licznik = 0
    licznik2 = 0

print(szescjedynek)
print(tylesamozer)


plik4 = open("wyniki2.txt", "w")


for n in potrzebnedozad6:
    for indx4 in range(0, len(n)):
        plik4.write(n[indx4] + ";")
    if indx4 == len(n)-1:
        plik4.write("\n")

plik4.close()