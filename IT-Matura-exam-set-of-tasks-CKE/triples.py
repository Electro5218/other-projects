plik = open("trojki.txt", "r").readlines()
dane = []

for z in plik:
    z = z.split()
    dane.append(z)

suma = 0
iletakichliczb = 0
## Zad 1
for m in dane:
    for indx in range(0, len(m[0])):
        suma += int(m[0][indx])
    for indx2 in range(0, len(m[1])):
        suma += int(m[1][indx2])
    if suma == int(m[2]):
        print(m[0], m[1], m[2])
        iletakichliczb += 1
    suma = 0

print(iletakichliczb)
print("\n")

## Zad 2

def czyPierwsza(x):
    if x < 1:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 1 == 0:
        for i in range(2, x):
            if x % i == 0:
                return False
    else:
        return False
    return True

for b in dane:
    if czyPierwsza(int(b[0])) and czyPierwsza(int(b[1])) and int(b[2]) == int(b[0]) * int(b[1]):
        print(b[0], b[1], b[2])

print("\n")
## Zad 3
for z in dane:
    if (int(z[0]) ** 2 + int(z[1]) ** 2) == int(z[2]) ** 2 or (int(z[1]) ** 2 + int(z[2]) ** 2 == int(z[0]) ** 2) or (int(z[2]) ** 2 + int(z[0]) ** 2 == int(z[1]) ** 2):
        print(z[0], z[1], z[2])

## Zad 4

def czytrojkat(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

dlugosc = 0
ilewierszytrojkatnych = 0
najdluzszyciagtrojkatny = 0
czyciagprawda = False
print("\n")
for t in dane:
    if czytrojkat(int(t[0]), int(t[1]), int(t[2])):
        ilewierszytrojkatnych += 1
    if czytrojkat(int(t[0]), int(t[1]), int(t[2])):
        dlugosc += 1
        czyciagprawda = True
    else:
        czyciagprawda = False
    if czyciagprawda == False:
        if najdluzszyciagtrojkatny < dlugosc:
            najdluzszyciagtrojkatny = dlugosc
        dlugosc = 0

print(ilewierszytrojkatnych, najdluzszyciagtrojkatny)