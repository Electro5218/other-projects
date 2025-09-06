plik = open("wielomiany.txt", "r").readlines()

wspolczynniki = []
wartoscx = []
dane = []
liczby = []


for k in plik:
    k = k.strip()
    wspolczynniki.append(k)

for b in wspolczynniki:
    b = b.split('; ')
    wartoscx.append(b)

for l in wartoscx:
    x = l[0].split()
    h = l[1]
    dane.append(x)
    liczby.append(h)

element = []

## Wypisywanie dzielenia przez wielomian (x-liczby[v])
print("Rozkład wielomianów")
print()
for v in range(0, 29):
    wartosc = int(liczby[v])
    n = len(dane[v])
    w = int(dane[v][n-1])
    for k in range(n-2, -1, -1):
        w = (wartosc*w)+int(dane[v][k])
        g = str(k)
        j = str(w) + "x" + "^" + g
        element.append(j)
    print("(" + "x" + "-" + str(liczby[v]) + ")", element)
    element = []
    print("----------------------------------------------------------------------------------------------------------------")

## Obliczanie wartosci
print("Obliczanie wartości wielomianu dla danego pierwiastka")
print()
wartoscwielomianu = 0
for o in range(0, 29):
    n = 0
    f = int(dane[o][n])
    wartosc = int(liczby[o])
    for u in range(0, len(dane[o])):
        f = f*(wartosc**u)
        wartoscwielomianu += f
        if len(dane[o]) == u+1:
            break
        f = int(dane[o][u+1])
    print(wartoscwielomianu)
    print("----------------------------------------------------------------------------------------------------------------")
    wartoscwielomianu = 0






