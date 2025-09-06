plik = open("instrukcje.txt")

dane = []

for i in plik:
    i = i.split()
    dane.append(i)

licznik = 0
for l in dane:
    if l[0] == "DOPISZ":
        licznik += 1
    elif l[0] == "USUN":
        licznik -= 1

print(licznik)

## zad 4.2

ciag = 0
maksciag = 0
nazwategociagu = ''
for ind in range(0, len(dane)-1):
    m = dane[ind]
    if m[0] == dane[ind+1][0]:
        ciag += 1
    else:
        if ciag >= maksciag:
            maksciag = ciag
            nazwategociagu = m[0]
        ciag = 0

print(maksciag+1, nazwategociagu) ## Jeszcze sama ze soba

dopisanelitery = []
## zad 4.3
for x in dane:
    if x[0] == "DOPISZ":
        dopisanelitery.append(x[1])

all_freq = {}

for i in dopisanelitery:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

najwiekszy = 0
jeszczewiekszy = 0
litera = ''
for k, v in all_freq.items():
    najwiekszy = v
    if najwiekszy >= jeszczewiekszy:
        jeszczewiekszy = najwiekszy
        litera = k

print(jeszczewiekszy, litera)

## Zad 4

odpowiedz = []

for o in range(0, len(dane)):
    if dane[o][0] == "DOPISZ":
        odpowiedz.append(dane[o][1])
    elif dane[o][0] == "ZMIEN":
        odpowiedz.pop()
        odpowiedz.append(dane[o][1])
    elif dane[o][0] == "USUN":
        odpowiedz.pop()
    elif dane[o][0] == "PRZESUN":
        for t in range(0, len(odpowiedz)):
            if odpowiedz[t] == dane[o][1] == "Z":
                x = 'A'
                odpowiedz[t] = x
                break
            elif odpowiedz[t] == dane[o][1]:
                x = chr(ord(dane[o][1])+1)
                odpowiedz[t] = x
                break


tekst = ""

for e in odpowiedz:
    tekst += e

print(tekst)
