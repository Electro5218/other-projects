plik = open("dokad.txt", "r").readlines()

tekst = ""
for l in plik:
    l = l.strip()
    tekst = l

print(tekst)

klucz = "LUBIMYCZYTAC"
zaszyfrowanytekst = ""
ileprzesunac = 0

licznik = 0
powtorzenia = 0

## Zad 1
for m in range(0, len(tekst)):
    if tekst[m] == ',' or tekst[m] == '.':
        zaszyfrowanytekst += tekst[m]
        continue
    if licznik == 12:
        licznik = 0
        powtorzenia += 1
    if ord(tekst[m]) != 32:
        x = ord(klucz[licznik])
        licznik += 1
    elif ord(tekst[m]) == 32:
        x = 0
    if x >= 65:
        ileprzesunac = x - 65
    else:
        ileprzesunac = x
    if ord(tekst[m]) + ileprzesunac > 90:
        zaszyfrowanytekst += chr(((ord(tekst[m]) + ileprzesunac) - 91) + 65)
        continue
    zaszyfrowanytekst += chr(ord(tekst[m]) + ileprzesunac)

print(zaszyfrowanytekst)
print(powtorzenia + 1)

klucz = 0
tekst = 0

plik2 = open("szyfr.txt", "r").readlines()


klucz = plik2[1]
tekst = plik2[0].strip()
licznik = 0
zaszyfrowanytekst = ""
## Zad 2
for b in range(0, len(tekst)):
    if tekst[b] == ',' or tekst[b] == '.':
        zaszyfrowanytekst += tekst[b]
        continue
    if licznik == 13:
        licznik = 0
    if ord(tekst[b]) != 32:
        x = ord(klucz[licznik])
        licznik += 1
    elif ord(tekst[b]) == 32:
        x = 0
    if x >= 65:
        ileprzesunac = x - 65
    else:
        ileprzesunac = x
    if ord(tekst[b]) - ileprzesunac < 65 and ileprzesunac != 0 and x != 0:
        zaszyfrowanytekst += chr((91 - (65 - (ord(tekst[b]) - ileprzesunac))))
        continue
    elif ileprzesunac == 0 and x == 0:
        zaszyfrowanytekst += chr(32)
        continue
    zaszyfrowanytekst += chr(ord(tekst[b]) - ileprzesunac)

print(zaszyfrowanytekst)

## Zad 3
ile = {}

for t in range(0, len(tekst)):
    if tekst[t] != " " and tekst[t] != "," and tekst[t] != "." and tekst[t] in ile:
        ile[tekst[t]] += 1
    elif tekst[t] != " " and tekst[t] != "," and tekst[t] != "." and tekst[t] not in ile:
        ile[tekst[t]] = 1

klucze = list(ile.keys())
klucze.sort()
posortowanyslownik = {}

for i in klucze:
    posortowanyslownik[i] = ile[i]

ileliter = 0

for o in range(0, len(tekst)):
    if tekst[o] != " " and tekst[o] != "," and tekst[o] != ".":
        ileliter += 1

licznikulamek = 0
for v in posortowanyslownik.values():
    licznikulamek += v * (v-1)

ko = float(licznikulamek / ((ileliter) * (ileliter - 1)))

d = round(0.0285 / (ko - 0.0385), 2)

print(d)
print(len(klucz))

