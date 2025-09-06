import math

plik = open("liczby.txt").readlines()
dane = []

for add in plik:
    add = add.strip()
    dane.append(add)


def sitoerastotenesa(n):
    primers = []
    primers.append(False) # miejsce 0 czyli 0 # nie jest liczba pierwsza
    primers.append(False) # miejsce 1 czyli 1 nie jest liczba pierwsza

    for i in range(2, n + 1):
        primers.append(True)

    for i in range(2, n + 1):
        if primers[i] == True:
            j = i * 2
            while j <= n:
                primers[j] = False
                j = j + i
    return primers ## Zwraca informacje czy liczba z rozkladu danej liczby jest liczba pierwsza

Pierwsza = sitoerastotenesa(1000000)


def ile_rozkładów_goldbacha(liczba, Pierwsza):
    ile_rozkładów = 0
    for k in range(2, liczba // 2 + 1): ## do polowy dlatego ze maja byc unikalne wartosci
        if Pierwsza[k] == True and Pierwsza[liczba - k] == True: ##sprawdzamy czy obie liczby z rozkladu sa pierwsze
            ile_rozkładów += 1
    return ile_rozkładów



## zad 3 sito

max_rozkładów = -1 ## liczba na minusie aby znalezc maksimum
max_rozkładów_liczba = 0
min_rozkładów = 99999999999999 ## trzeba ustawic duza liczbe dlatego, zeby na pewno znalezc minimum
min_rozkładów_liczba = 0

for h in dane:
    liczba = int(h)
    ile_rozkładów = ile_rozkładów_goldbacha(liczba, Pierwsza)

    if ile_rozkładów > max_rozkładów:
        max_rozkładów = ile_rozkładów
        max_rozkładów_liczba = liczba
    if ile_rozkładów < min_rozkładów:
        min_rozkładów = ile_rozkładów
        min_rozkładów_liczba = liczba

print(max_rozkładów_liczba, max_rozkładów)
print(min_rozkładów_liczba, min_rozkładów)

