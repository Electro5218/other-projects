plik = open("hasla.txt", "r").readlines()
hasla = []

for i in plik:
    i = i.strip()
    hasla.append(i)

def isNumber(n):
    n = str(n)
    numery = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    czyhaslotonumer = False
    for i in range(0, len(n)):
        if n[i] in numery:
            czyhaslotonumer = True
        else:
            czyhaslotonumer = False
            break
    if czyhaslotonumer == True:
        return True
    else:
        return False

def kolejne(a, b, c, d):
    T = {a,b,c,d}
    T = sorted(T)
    if a == b or a == c or a == d or b == a or b == c or b == d or c == a or c == b or c == d or d == a or d == b or d == c:
        return False
    a = ord(T[0])
    b = ord(T[1])
    c = ord(T[2])
    d = ord(T[3])
    return (a+1==b and b+1==c and c+1==d)

def zawiera_4kolejne(s):
    if len(s) < 4:
        return False
    for i in range(3, len(s)):
        if kolejne(s[i-3], s[i-2], s[i-1], s[i]):
            return True
    return False

## zad 1
licznikhasel = 0
for l in hasla:
    if isNumber(l) == True:
        licznikhasel += 1
print("Liczba hasel zlozonych jedynie ze znakow numerycznych :" + " " + str(licznikhasel))
## zad 2
haslaktoresiepowtarzajaconajmniejdwarazy = []
licznikpowtarzajacychsiehasel = 0
for g in range(0, len(hasla)):
    for k in range(0, len(hasla)):
        if hasla[g] == hasla[k]:
            licznikpowtarzajacychsiehasel += 1
        if licznikpowtarzajacychsiehasel >= 2:
            haslaktoresiepowtarzajaconajmniejdwarazy.append(hasla[g])
    licznikpowtarzajacychsiehasel = 0

haslaktoresiepowtarzajaconajmniejdwarazy = set(sorted(haslaktoresiepowtarzajaconajmniejdwarazy))
print("Zad2 :" + " " + str(sorted(haslaktoresiepowtarzajaconajmniejdwarazy)))

# ## zad 3
liczbauzytkownikowzfragmentemzlozonym = 0
for l in hasla:
    if zawiera_4kolejne(l):
        liczbauzytkownikowzfragmentemzlozonym += 1
print("Liczba hasel ze zlozonym fragmentem :" + " " + str(liczbauzytkownikowzfragmentemzlozonym))

## zad 4
liczbahasel = 0
numery = 0
maleznaki = 0
duzeznaki = 0
for c in hasla:
    for indx in range(0, len(c)):
        if isNumber(c[indx]):
            numery += 1
        if ord('A') <= ord(c[indx]) <= ord('Z'):
            duzeznaki += 1
        if ord('a') <= ord(c[indx]) <= ord('z'):
            maleznaki += 1
    if numery >= 1 and duzeznaki >= 1 and maleznaki >= 1:
        liczbahasel += 1
    numery = 0
    maleznaki = 0
    duzeznaki = 0

print("Tyle hasel spelnia kryteria z zad4 :" + " " + str(liczbahasel))

zapis = open("wyniki.txt", "w")
zapis.write("zad1 : 16\n" + "zad2 : ['8Y7JGYXXR5', 'Ehz018657', 'PAsCMQaervw', 'cefdi', 'cek', 'ikfLDegQXj', 'jir', 'yvm249t83o04']\n" + "zad3 : 39\n" + "zad4 : 40")



