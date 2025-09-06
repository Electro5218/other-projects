from math import sqrt

plik = open("ciagi.txt", "r").readlines()
dane = []

for i in plik:
    i = i.strip()
    dane.append(i)



iledwucyklicznych = 0

for z in dane:
    if len(z) % 2 == 0:
        x = len(z) // 2
        if z[:x] == z[x:]:
            print(z)
            iledwucyklicznych += 1

print(iledwucyklicznych)

niewystepujajedynki = 0
czyniewystepujajedynki = True

for b in dane:
    for indx in range(0, len(b)-1):
        if b[indx] == b[indx+1] == "1":
            czyniewystepujajedynki = False
            break
        else:
            czyniewystepujajedynki = True
    if czyniewystepujajedynki == True:
        niewystepujajedynki += 1
    czyniewystepujajedynki = True


print(niewystepujajedynki)

## Zad 3
def isPrime(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n % 1 == 0:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def czymadwadzielnikipierwsze(liczba):
    for o in range(2, liczba+1):
        if isPrime(o):
            if liczba % o == 0:
                if isPrime(liczba / o):
                    return True
    return False

najmniejsza = 999999999999
najwieksza = 0
iletakich = 0

for b in dane:
    b = int(b, 2)
    if czymadwadzielnikipierwsze(b) == True:
        iletakich += 1
        if najwieksza < b:
            najwieksza = b
        if najmniejsza > b:
            najmniejsza = b

print(iletakich, najwieksza, najmniejsza)