plik = open("dane_napisy.txt", "r").readlines()
dane = []
ilelinijekjestanagrami = 0
ilejednolitychianagramow = 0
wszystkieanagramywjednejtabeli = []
k = 0

def anagramy(a, b):
    if sorted(a) == sorted(b):
        return True
    return False

def jednolite(napis):
    n = len(napis)
    for i in range(1, n):
        if napis[i] != napis[0]:
            return False
    return True

for i in plik:
    i = i.split()
    dane.append(i)

for dodaj in dane:
    for dodaj1 in dodaj:
        wszystkieanagramywjednejtabeli.append(dodaj1)

for element in dane:
    if anagramy(element[0], element[1]):
       ilelinijekjestanagrami += 1
    if jednolite(element[0]) and jednolite(element[1]) and anagramy(element[0], element[1]):
        ilejednolitychianagramow += 1

for skladnik in wszystkieanagramywjednejtabeli:
    templicznik = 0
    for porownywanyskladnik in wszystkieanagramywjednejtabeli:
        if anagramy(skladnik, porownywanyskladnik):
            templicznik += 1
    if templicznik > k:
        k = templicznik

print(ilelinijekjestanagrami, ilejednolitychianagramow, k)

save = open("wynik.txt", "w")
save.write("68.1: 9 | 68.2: 93 | 68.3: 17")