plik = open("szachy.txt", "r").readlines()
dane = []
tmp = []
## zad 1.1
licznik = 0
for i in plik:
    licznik += 1
    if i == '\n':
        dane.append(tmp)
        tmp = []
        continue
    i = i.strip()
    tmp.append(i)
    if licznik == len(plik):
        dane.append(tmp)
        tmp = []

licznik = 0

print(dane)

ileplansz = 0
najwiekszaliczbapustychkolumn = 0

for m in dane:
    ilepustych = 0
    for x in range(0, 8):
        czyPustakolumna = True
        for y in range(0, 8):
            if m[y][x] != '.':
                czyPustakolumna = False
        if czyPustakolumna == True:
            ilepustych += 1
    if ilepustych >= 1:
        ileplansz += 1
    if najwiekszaliczbapustychkolumn < ilepustych:
        najwiekszaliczbapustychkolumn = ilepustych

print(ileplansz, najwiekszaliczbapustychkolumn)

zapis1 = open("zadanie1_1.txt", "w")
zapis1.write("36" + " " + "3")
zapis1.close()

## Zad 1.2

hetmanczarny = 0
hetmanbialy = 0
krolbialy = 0
krolczarny = 0
wiezabiala = 0
wiezaczarna = 0
skoczekbialy = 0
skoczekczarny = 0
goniecbialy = 0
goniecczarny = 0
pionekbialy = 0
pionekczarny = 0
czarne = 0
biale = 0
najmniejlacznie = 99999999

planszarownowagi = 0

for t in dane:
    stanrownowagi = False
    for y in range(0, 8):
        for x in range(0, 8):
            if t[y][x] == "K":
                krolbialy += 1
                biale += 1
            elif t[y][x] == "k":
                krolczarny += 1
                czarne += 1
            elif t[y][x] == "W":
                wiezabiala += 1
                biale += 1
            elif t[y][x] == "w":
                wiezaczarna += 1
                czarne += 1
            elif t[y][x] == "S":
                skoczekbialy += 1
                biale += 1
            elif t[y][x] == "s":
                skoczekczarny += 1
                czarne += 1
            elif t[y][x] == "H":
                hetmanbialy += 1
                biale += 1
            elif t[y][x] == "h":
                hetmanczarny += 1
                czarne += 1
            elif t[y][x] == "G":
                goniecbialy += 1
                biale += 1
            elif t[y][x] == "g":
                goniecczarny += 1
                czarne += 1
            elif t[y][x] == "P":
                pionekbialy += 1
                biale += 1
            elif t[y][x] == "p":
                pionekczarny += 1
                czarne += 1
    if (krolczarny == krolbialy) and (wiezaczarna == wiezabiala) and (skoczekczarny == skoczekbialy) and (hetmanbialy == hetmanczarny) and (goniecczarny == goniecbialy) and (pionekczarny == pionekbialy) and (czarne == biale):
        stanrownowagi = True
        if stanrownowagi == True:
            planszarownowagi += 1
            laczniebialeiczarne = biale + czarne
            if laczniebialeiczarne < najmniejlacznie:
                najmniejlacznie = laczniebialeiczarne
            stanrownowagi
            laczniebialeiczarne = 0
    biale = 0
    czarne = 0
    krolbialy = 0
    krolczarny = 0
    wiezabiala = 0
    wiezaczarna = 0
    skoczekbialy = 0
    skoczekczarny = 0
    hetmanbialy = 0
    hetmanczarny = 0
    goniecbialy = 0
    goniecczarny = 0
    pionekbialy = 0
    pionekczarny = 0


print(planszarownowagi, najmniejlacznie)

zapis2 = open("zadanie1_2.txt", "w")
zapis2.write("22" + " " + "28")
zapis2.close()

## zad 1.3

szachowaniebialej = 0
szachowaniebialejplansza = 0
y1szachowaniebialej = 0
y2szachowaniebialej = 0
x1szachowaniebialej = 0
x2szachowaniebialej = 0

## biala wieza szachuje czarnego krola

for c in dane:
    czyBreak = False
    for x in range(0, 8):
        for y in range(0, 8):
            if c[y][x] == "W":
                y1szachowaniebialej = y
                x1szachowaniebialej = x
                for y in range(0,8):
                    if c[y][x1szachowaniebialej] == "k":
                        y2szachowaniebialej = y
                        if y1szachowaniebialej > y2szachowaniebialej:
                            for y in range(y2szachowaniebialej, y1szachowaniebialej+1):
                                if c[y][x1szachowaniebialej] != "." and c[y][x1szachowaniebialej] != "W" and c[y][x1szachowaniebialej] != "k":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowaniebialej += 1
                        elif y2szachowaniebialej > y1szachowaniebialej:
                            for y in range(y1szachowaniebialej, y2szachowaniebialej+1):
                                if c[y][x1szachowaniebialej] != "." and c[y][x1szachowaniebialej] != "W" and c[y][x1szachowaniebialej] != "k":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowaniebialej += 1
                for x in range(0,8):
                    if c[y1szachowaniebialej][x] == "k":
                        x2szachowaniebialej = x
                        if x1szachowaniebialej > x2szachowaniebialej:
                            for x in range(x2szachowaniebialej, x1szachowaniebialej+1):
                                if c[y1szachowaniebialej][x] != "." and c[y1szachowaniebialej][x] != "W" and c[y1szachowaniebialej][x] != "k":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowaniebialej += 1
                        elif x2szachowaniebialej > x1szachowaniebialej:
                            for x in range(x1szachowaniebialej, x2szachowaniebialej+1):
                                if c[y1szachowaniebialej][x] != "." and c[y1szachowaniebialej][x] != "W" and c[y1szachowaniebialej][x] != "k":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowaniebialej += 1
    if szachowaniebialej >= 1:
        szachowaniebialejplansza += 1
        szachowaniebialej = 0
    czyBreak = False

print(szachowaniebialejplansza)

## czarny krol szachuje biala wieze

szachowanieczarnej = 0
szachowanieczarnejplansza = 0

for c in dane:
    czyBreak = False
    for x in range(0, 8):
        for y in range(0, 8):
            if c[y][x] == "w":
                y1szachowaniebialej = y
                x1szachowaniebialej = x
                for y in range(0,8):
                    if c[y][x1szachowaniebialej] == "K":
                        y2szachowaniebialej = y
                        if y1szachowaniebialej > y2szachowaniebialej:
                            for y in range(y2szachowaniebialej, y1szachowaniebialej+1):
                                if c[y][x1szachowaniebialej] != "." and c[y][x1szachowaniebialej] != "w" and c[y][x1szachowaniebialej] != "K":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowanieczarnej += 1
                        elif y2szachowaniebialej > y1szachowaniebialej:
                            for y in range(y1szachowaniebialej, y2szachowaniebialej+1):
                                if c[y][x1szachowaniebialej] != "." and c[y][x1szachowaniebialej] != "w" and c[y][x1szachowaniebialej] != "K":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowanieczarnej += 1
                for x in range(0,8):
                    if c[y1szachowaniebialej][x] == "K":
                        x2szachowaniebialej = x
                        if x1szachowaniebialej > x2szachowaniebialej:
                            for x in range(x2szachowaniebialej, x1szachowaniebialej+1):
                                if c[y1szachowaniebialej][x] != "." and c[y1szachowaniebialej][x] != "w" and c[y1szachowaniebialej][x] != "K":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowanieczarnej += 1
                        elif x2szachowaniebialej > x1szachowaniebialej:
                            for x in range(x1szachowaniebialej, x2szachowaniebialej+1):
                                if c[y1szachowaniebialej][x] != "." and c[y1szachowaniebialej][x] != "w" and c[y1szachowaniebialej][x] != "K":
                                    czyBreak = True
                                    break
                            if czyBreak == False:
                                szachowanieczarnej += 1
    if szachowanieczarnej >= 1:
        szachowanieczarnejplansza += 1
        szachowanieczarnej = 0
    czyBreak = False

print(szachowanieczarnejplansza)

zapis3 = open("zadanie1_3.txt", "w")
zapis3.write("3" + " " + "1")
zapis3.close()