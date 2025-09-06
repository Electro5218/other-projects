plik = open("pary.txt", "r").readlines()
dane=[]
liczby = []
wyrazy = []
liczbyparzyste = []
slowaotejsamejdlugoscicoliczba=[]

for i in plik:
    i=i.split()
    liczby.append(i[0])
    wyrazy.append(i[1])
    dane.append(i)

for el in liczby:
    el = int(el)
    if el%2 == 0:
        liczbyparzyste.append(el)

def isPrime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

## zad 1
for l in liczbyparzyste:
    roznica = 0
    if l % 2 == 0 and l > 4:
        for f in range(3, l, 2):
            if isPrime(f) and isPrime(l-f):
                if ((l-f)-f) < roznica:
                    continue
                elif ((l-f)-f) > roznica:
                    roznica = (l - f) - f
                    print(l,f, l-f)
        roznica = 0

## zad 2

for m in wyrazy:
    ciag = 1
    max_literka = m[0]
    najwiekszyciag = 1
    for index in range(0, len(m)-1):
        if m[index] == m[index+1]:
            ciag += 1
        else:
            ciag = 1
        if ciag > najwiekszyciag:
            najwiekszyciag = ciag
            max_literka = m[index]
    print("\n" + max_literka*najwiekszyciag, najwiekszyciag)

## zad 3
for element in dane:
    if int(element[0]) == len(element[1]):
        slowaotejsamejdlugoscicoliczba.append(element)

minimalnapara = slowaotejsamejdlugoscicoliczba[0]
for k in range(0, len(slowaotejsamejdlugoscicoliczba)-1):
    if slowaotejsamejdlugoscicoliczba[k][0] < slowaotejsamejdlugoscicoliczba[k+1][0] or (slowaotejsamejdlugoscicoliczba[k][0] == slowaotejsamejdlugoscicoliczba[k+1][0] and slowaotejsamejdlugoscicoliczba[k][1] < slowaotejsamejdlugoscicoliczba[k+1][1]):
        minimalnapara = slowaotejsamejdlugoscicoliczba[k]

print("\n" + minimalnapara[0], minimalnapara[1])









   







