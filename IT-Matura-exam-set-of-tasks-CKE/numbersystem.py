plik = open("liczby.txt", "r").readlines()
liczby = []
zamiananaszestnastkowy = []
systemszesnastkowyznaki = {}

for i in plik:
    i = i.strip()
    liczby.append(i)

for i in plik:
    i = int(i)
    i = hex(i)
    zamiananaszestnastkowy.append(i[2::])


for element in zamiananaszestnastkowy:
    for element1 in element:
        if element1 not in systemszesnastkowyznaki:
            systemszesnastkowyznaki[element1] = 1
        else:
            systemszesnastkowyznaki[element1] = systemszesnastkowyznaki[element1] + 1

print(systemszesnastkowyznaki)

def sito(n):
    tab = []
    tab.append(False)
    tab.append(False)

    for i in range(2, n + 1):
        tab.append(True)

    for i in range(2, n + 1):
        if tab[i] == True:
            j = i * 2
            while j <= n:
                tab[j] = False
                j = j + i
    return tab

sito = sito(1000000)

def ile_rozkładów_goldbacha(liczba, sito):
    ile_rozkładów = 0
    for i in range(2, liczba // 2 + 1):
        if sito[i] == True and sito[liczba - i] == True:
            ile_rozkładów = ile_rozkładów + 1
    return ile_rozkładów

max_rozkładów = -1
max_rozkładów_liczba = 0
min_rozkładów = 99999999999999
min_rozkładów_liczba = 0

for wiersz in liczby:
    liczba = int(wiersz)
    ile_rozkładów = ile_rozkładów_goldbacha(liczba, sito)

    if ile_rozkładów > max_rozkładów:
        max_rozkładów = ile_rozkładów
        max_rozkładów_liczba = liczba

    if ile_rozkładów < min_rozkładów:
        min_rozkładów = ile_rozkładów
        min_rozkładów_liczba = liczba

print(max_rozkładów_liczba, max_rozkładów)
print(min_rozkładów_liczba, min_rozkładów)

zapis = open("wyniki3.txt", "w")
zapis.write("3.3 odpowiedz" + "\n" + "910620 9932 | 18676 195" + "\n" + "3.4 odpowiedz" + "\n" + "{'1': 26, 'b': 33, 'e': 44, '8': 38, '4': 43, '2': 37, '0': 32, 'a': 45, 'c': 29, '3': 31, '6': 28, '9': 28, '7': 23, 'd': 23, '5': 25, 'f': 10}")


