pierwsza = True

we1 = open("wiadomosci.txt", "r")
we2 = open("podpisy.txt", "r")
wy = open("epodpis_wynik.txt", "w")

def skrot(t):
    global pierwsza
    S = ['65', '76', '71', '79', '82', '89', '84', '77']
    while len(t) % 8 != 0:
        t += '.'
    n = len(t)
    if pierwsza:
        wy.write("Dlugosc pierwszej wiadomosci = " + str(n) + "\n")
    i = 0
    while i < n:
        for j in range(8):
            S[j] = (int(S[j]) + ord(t[i])) % 128
            i += 1
    if pierwsza:
        wy.write("Bajty pierwszej wiadomosci po przetworzeniu: ")
        for j in range(8):
            wy.write(str(S[j]) + " ")
        wy.write("\n")
    wynik = ""
    for o in range(8):
        wynik = wynik + chr(65 + S[o]%26)
    if pierwsza:
        wy.write("Skrot pierwszej wiadomosci: ")
        wy.write(wynik + '\n')
        pierwsza = False
    return wynik

t = ""
s = ""
mojSkrot = ""
n = 200
d = 3

W = [False] * 12

for i in range(1, 12):
    t = we1.readline().strip()
    s = skrot(t)

    mojSkrot = ""
    podpisy = we2.readline().strip().split()  # Rozbijamy ciąg na pojedyncze liczby
    for podpis in podpisy:
        y = int(podpis)  # Konwertujemy pojedynczą liczbę z ciągu na liczbę całkowitą
        x = (y * d) % n
        mojSkrot += chr(x)

    wy.write(str(i) + "\t" + mojSkrot + "\t")
    if s == mojSkrot:
        wy.write("wiarygodna\n")
        W[i] = True
    else:
        wy.write("zmieniona\n")

wy.write("\nNumery wiarygodnych wiadomosci: ")
for i in range(0, 12):
    if W[i]:
        wy.write(str(i) + " ")

we1.close()
we2.close()
wy.close()