plik = open("funkcja.txt", "r").readlines()

dane = []

for i in plik:
    i = i.split()
    dane.append(i)

def obliczaniewartoscifunkcji(x, a0, a1, a2, a3):
    return round(float(a0) + (float(a1)*x) + (float(a2)*(x**2)) + (float(a3)*(x**3)), 5)

def obliczaniewartoscifunkcji1(x):
    for m in range(0, len(dane)):
        if 0<=x<1:
         return float(dane[m][0]) + (float(dane[m][1]) * x) + (float(dane[m][2]) * (x ** 2)) + (float(dane[m][3]) * (x ** 3))
        elif 1<=x<2:
         return float(dane[m+1][0]) + (float(dane[m+1][1]) * x) + (float(dane[m+1][2]) * (x ** 2)) + (float(dane[m+1][3]) * (x ** 3))
        elif 2<=x<3:
         return float(dane[m+2][0]) + (float(dane[m+2][1]) * x) + (float(dane[m+2][2]) * (x ** 2)) + (float(dane[m+2][3]) * (x ** 3))
        elif 3<=x<4:
         return float(dane[m+3][0]) + (float(dane[m+3][1]) * x) + (float(dane[m+3][2]) * (x ** 2)) + (float(dane[m+3][3]) * (x ** 3))
        elif 4<=x<5:
         return float(dane[m+4][0]) + (float(dane[m+4][1]) * x) + (float(dane[m+4][2]) * (x ** 2)) + (float(dane[m+4][3]) * (x ** 3))

x = 1.5
## Zad 1
for o in range(0, len(dane)):
    if 0<=x<1:
        print(obliczaniewartoscifunkcji(x, dane[o][0], dane[o][1], dane[o][2], dane[o][3]))
        break
    elif 1<=x<2:
        print(obliczaniewartoscifunkcji(x, dane[o+1][0], dane[o+1][1], dane[o+1][2], dane[o+1][3]))
        break
    elif 2<=x<3:
        print(obliczaniewartoscifunkcji(x, dane[o + 2][0], dane[o + 2][1], dane[o + 2][2], dane[o + 2][3]))
        break
    elif 3<=x<4:
        print(obliczaniewartoscifunkcji(x, dane[o + 3][0], dane[o + 3][1], dane[o + 3][2], dane[o + 3][3]))
        break
    elif 4<=x<5:
        print(obliczaniewartoscifunkcji(x, dane[o + 4][0], dane[o + 4][1], dane[o + 4][2], dane[o + 4][3]))
        break

## Zad 2

wartosc = 0
wartoscnajwieksza = -9999999999999
x = 0
najwiekszyx = 0

for o in range(0, len(dane)):
    while x < 6:
        if 0<=x<1:
            wartosc = obliczaniewartoscifunkcji(x, dane[o][0], dane[o][1], dane[o][2], dane[o][3])
        elif 1<=x<2:
            wartosc = obliczaniewartoscifunkcji(x, dane[o+1][0], dane[o+1][1], dane[o+1][2], dane[o+1][3])
        elif 2<=x<3:
            wartosc = obliczaniewartoscifunkcji(x, dane[o + 2][0], dane[o + 2][1], dane[o + 2][2], dane[o + 2][3])
        elif 3<=x<4:
            wartosc = obliczaniewartoscifunkcji(x, dane[o + 3][0], dane[o + 3][1], dane[o + 3][2], dane[o + 3][3])
        elif 4<=x<5:
            wartosc = obliczaniewartoscifunkcji(x, dane[o + 4][0], dane[o + 4][1], dane[o + 4][2], dane[o + 4][3])
        if wartosc > wartoscnajwieksza:
            wartoscnajwieksza = wartosc
            najwiekszyx = x
        x += 0.001
    break


print(wartoscnajwieksza, round(najwiekszyx, 3))

## Zad 3

x = 0

def miejscazerowepolowienie(dokladnosc = 0.00001, x1= 0, x2 = 4.99999):
    if obliczaniewartoscifunkcji1(x1) * obliczaniewartoscifunkcji1(x2) > 0:
        return False
    roznica = abs(x2 - x1)
    while roznica > dokladnosc:
        roznica = abs(x2 - x1)
        c = (x1+x2) / 2
        y = obliczaniewartoscifunkcji1(c)
        if y * obliczaniewartoscifunkcji1(x1) <= 0:
            x2 = c
        else:
            x1 = x2
            x2 = c
    return c

for t in range(0, 5):
    if miejscazerowepolowienie(dokladnosc=0.000001, x1=t, x2=t+0.99999) == False:
        print("Ni ma na przedziale" + " " + str(t) + " " + str(t+0.99999))
    else:
        y = round(miejscazerowepolowienie(dokladnosc=0.000001, x1=t, x2=t+0.99999), 5)
        print(y)

