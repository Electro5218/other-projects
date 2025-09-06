import copy
plansza = list()
rozwiazanie = 0
rozwiazanie_2 = 0
rozwiazanie_3 = 0
faza = 0
kordy = ((0,1), (0,-1), (1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1))
with open("gra.txt", "r") as file:
    for line in file:
        plansza.append(list(line.rstrip()))

for l in range(2,100):
    ilosc_zywych = 0
    robocza = copy.deepcopy(plansza)
    for i in range(12):
        for j in range(20):
            licznik = 0
            for k in kordy:
                y = k[0] + j
                x = k[1] + i
                if x > 11:
                    x = 0
                elif x < 0:
                    x = 11
                if y > 19:
                    y = 0
                elif y < 0:
                    y = 19
                if plansza[x][y] == 'X':
                    licznik += 1
            if (l == 38 and i == 1 and j == 18 ):
                rozwiazanie = licznik
            if ( licznik in (2,3) and plansza[i][j] =='X') or (licznik == 3 and plansza[i][j] =='.'):
                robocza[i][j] = 'X'
                ilosc_zywych += 1
                if l == 2:
                    rozwiazanie_2 += 1
            else:
                robocza[i][j] = '.'
    if plansza == robocza:
        if faza == 0:
            rozwiazanie_3 = l

    plansza = copy.deepcopy(robocza)
print(rozwiazanie, rozwiazanie_2 , rozwiazanie_3, ilosc_zywych)