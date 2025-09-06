file = open("liczby2.txt", "r").readlines()

pary = []
ułamki = []
mianowniki = []
NWWmianownikow = []

for i in file:
    i = i.split()
    pary.append(i)

def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    return a

def NWW(T):
    k = len(T)
    while (len(T) > 1):
        n = NWD(int(T[0],), int(T[1]))
        m = (int(T[0])*int(T[1])/(n))
        T[1] = int(m)
        del T[0]
    return int(T[0])

for elementy in pary:
    for element in range(0, len(elementy)-1):
        ułamki.append(int(elementy[element])/int(elementy[element+1]))

sumawszystkichulamkow = 0
for ułamek in range(0, len(ułamki)):
    sumawszystkichulamkow = sumawszystkichulamkow + ułamki[ułamek]

for numer in pary:
    mianowniki.append(numer[1])

NWWmianownikow.append(NWW(mianowniki))


licznikulamkawyniku = round(sumawszystkichulamkow * NWWmianownikow[0])

zapis = open("wynik.txt", "w")
zapis.write(str(licznikulamkawyniku) + "/" + str(NWWmianownikow[0]))
zapis.close()



























