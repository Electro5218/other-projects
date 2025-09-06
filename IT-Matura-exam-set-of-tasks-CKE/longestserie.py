plik = open("mecz.txt", "r").readlines()
licznik = 0
punktyA = 0
punktyB = 0
ciagA = 0
ciagB = 0
tA = []
tB = []



## ZAD 1
for i in range(0, 9999):
    for l in plik:
        if l[i] != l[i+1]:
            licznik += 1

print(licznik)

##ZAD 2
for i in range(0, 9999):
    for l in plik:
        if l[i] == 'A':
            punktyA += 1
        else:
            punktyB += 1
    if punktyA >= 1000 and abs(punktyA - punktyB) >= 3 and punktyA > punktyB:
        print("W pierwszym secie wygrywa drużyna A")
        print(str(punktyA) + ":" + str(punktyB))
        break
    elif punktyB >= 1000 and abs(punktyB - punktyA) >= 3 and punktyB > punktyA:
        print("W pierwszym secie wygrywa drużyna B")
        print(str(punktyB) + ":" + str(punktyA))
        break

## ZAD 3
for i in range(0, 9999):
    for l in plik:
        if l[i] == 'A':
            if ciagB >= 10:
                tB.append(ciagB)
            ciagB = 0
            ciagA += 1
        else:
            if ciagA >= 10:
                tA.append(ciagA)
            ciagA = 0
            ciagB += 1
print("Passa A:", len(tA), "Passa B:", len(tB), "ilość dobrych pass:", len(tB) + len(tA))
if max(tA) > max(tB):
    print("najdłuższa passa wynosi:", max(tA), "i należy do drużyny A")
else:
    print("najdłuższa passa wynosi:", max(tB), "i należy do drużyny B")


odpowiedzi = open("wyniki1.txt", "w")
odpowiedzi.write("Zad 1.1" + "\n" + "tyle razy rozgrywke wygrala druzyna niz druzyna ktora wygrala poprzednio: 5030" + "\n" + "Zad 1.2" + "\n" + "Drużyna B wygrała w pierwszym secie wynikiem 1004:1001" + "\n" + "Zad 1.3" + "\n" + "Najdłuższa passa wynosi 15 i należy do drużyny B, ilość dobrych pass w tym meczu wynosi 6")




