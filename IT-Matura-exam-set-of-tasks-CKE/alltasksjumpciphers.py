import math

#deszyfrowanie mieszane

def deszyfrowaniemieszane(klucz, tekst):
    m = math.ceil(len(tekst)/klucz)
    tabela = []
    i = 0
    # tworzenie tabeli - jest pusta!
    while i < m:
        tabela.append([])
        a = 0
        while a < klucz:
            tabela[i].append([])
            a += 1
        i += 1
    i = 0
    gdzie_dodajemy = 0
    flaga = True
    # uzupelnianie tabeli
    while i < len(tekst):
        # ktora kolumna w tabeli
        a = i // klucz
        tabela[a][gdzie_dodajemy] = tekst[i]
        i += 1
        # jesli koniec - ostatnie pole - zawracamy
        if gdzie_dodajemy == klucz-1 and flaga:
            flaga = False
            gdzie_dodajemy = klucz-1
            continue
        # jesli start - ostatnie pole - zawracamy
        if gdzie_dodajemy == 0 and not flaga:
            flaga = True
            gdzie_dodajemy = 0
            continue
        if flaga:
            gdzie_dodajemy += 1
        else:
            gdzie_dodajemy -= 1
    # usuwanie pustych pól
    for kolumna in tabela:
        if [] in kolumna:
            kolumna.remove([])
    # odczyt z tabeli
    tekst_deszyfrowany = ''
    i = 0
    y = 0
    while y < len(tabela[0]):
        i = 0
        while i < len(tabela):
            if len(tabela[i]) <= y:
                return tekst_deszyfrowany
            tekst_deszyfrowany += tabela[i][y]
            i += 1
        y += 1
    return tekst_deszyfrowany
    pass

print(deszyfrowaniemieszane(3, 'SRNIOZYWEAF'))


## Algorytm odszyfrowania skokowego

def deszyfrskokowy(klucz, tekst):
    tekstdeszyfrowany = ''
    tmp = 0
    numeriteracji = 0
    r = math.ceil(len(tekst) / klucz)
    sekwencje = len(tekst) // klucz
    for l in range(0, len(tekst)):
        if tmp > 0 and sekwencje != 0 and klucz % 2 == 0: ## dla kluczów parzystych
            l = tmp
        elif tmp > 0 and klucz % 2 != 0: ## dla kluczów nieparzystych
            l = tmp
        if sekwencje == 0 and klucz % 2 == 0: ## dla kluczów parzystych
            l = tmp + r
            tmp = l
        if len(tekst) - tmp < 0:
            numeriteracji += 1
            tmp = numeriteracji
            l = tmp
        tekstdeszyfrowany += tekst[l]
        if sekwencje != 0:
            sekwencje -= 1
        else:
            sekwencje = len(tekst) // klucz
        if sekwencje != 0 and klucz % 2 == 0: ## dla kluczów parzystych
            tmp += klucz
        elif klucz % 2 != 0: ## dla kluczów nieparzystych
            tmp += klucz
    return tekstdeszyfrowany


print(deszyfrskokowy(4, 'DRJTOZEBES'))
print(deszyfrskokowy(3, 'UDOMEWIKAEOĆMD'))

## szyfrowanie skokowe z polecenia przepisane

def szyfrowanieskokowe(k, W):
    n = len(W)
    szukanystring2 = ''
    m = n // k
    if n % k != 0:
        m += 1
    for i in range(0, m):
        j = i
        while j < n:
            szukanystring2 += W[j]
            j = j + m
    print(szukanystring2)

szyfrowanieskokowe(3, "ZADANIE1JESTŁATWE")
szyfrowanieskokowe(4, "ZADANIE1JESTPROSTE")

## szyfrowanie mieszane

def szyfrowaniemieszane(klucz, tekst):
    m = math.ceil(len(tekst)/klucz)
    stringszukany = ''
    tabela = []
    i = 0
    # tworzenie tabeli - jest pusta!
    while i < m:
        tabela.append([])
        a = 0
        while a < klucz:
            tabela[i].append([])
            a += 1
        i += 1
    i = 0
    tmp = 0
    a = 0
    iteracja1 = 0
    znaki = 0
    while a < m:
        for l in range(0, klucz):
            if len(tekst) - znaki == 0:
                break
            if a % 2 == 0:
                tabela[a][l] = tekst[tmp]
                tmp += m
                znaki += 1
            elif a % 2 != 0:
                tabela[a][l] = tekst[tmp]
                tmp += m
                znaki += 1
        a += 1
        iteracja1 += 1
        tmp = iteracja1
        liczbakolumny = 0
    for kolumna in tabela:
        if [] in kolumna:
            kolumna.remove([])
        if liczbakolumny % 2 == 0:
            for litery in kolumna:
                stringszukany += litery
        elif liczbakolumny % 2 != 0:
            pomockolumna = reversed(kolumna)
            for litery1 in pomockolumna:
                stringszukany += litery1
        liczbakolumny += 1
    print(stringszukany)


szyfrowaniemieszane(3, 'SZYFROWANIE')