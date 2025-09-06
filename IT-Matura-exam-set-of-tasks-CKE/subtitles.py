plik = open("napisy.txt", "r").readlines()

dane = []

for i in plik:
    i = i.split()
    dane.append(i)
## Zad 1

ile = 0
for z in dane:
    if len(z[0]) * 3 <= len(z[1]) or len(z[1]) * 3 <= len(z[0]):
        ile += 1
        if ile == 1:
            print(z)

print(ile)


## Zad 2
for o in dane:
    if (len(o[0]) > len(o[1])):
        x = len(o[0]) - len(o[1])
        z = o[0][-x:]
        y = o[1] + z
        if y == o[0]:
            print(o, z)
    elif (len(o[1]) > len(o[0])):
        x = len(o[1]) - len(o[0])
        z = o[1][-x:]
        y = o[0] + z
        if y == o[1]:
            print(o, z)
## Zad 3

def koncowka(A, B):
    dl_A = len(A)
    dl_B = len(B)
    k = 0
    while k < dl_A and k < dl_B and A[dl_A - 1 - k] == B[dl_B - 1 - k]:
        k += 1
    return k


dlugosc = 0
pierwszy = []
drugi = []
wspolna = []

for b in plik:
    A, B = b.split()
    pierwszy.append(A)
    drugi.append(B)
    wspolna.append(koncowka(A, B))
    if wspolna[-1] > dlugosc:
        dlugosc = wspolna[-1]

print("maksymalna koncowka:" + str(max(wspolna)))

for i in range(len(drugi)):
    if wspolna[i] == dlugosc:
        print(pierwszy[i], drugi[i])