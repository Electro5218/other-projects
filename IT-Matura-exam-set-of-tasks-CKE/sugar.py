import re

plik = open("cukier.txt", "r").readlines()
plik2 = open("cennik.txt", "r").readlines()

dane = []
ceny = []
NIPYiIloscCukru = []

for i in plik:
    i = i.split()
    dane.append(i)
for j in plik2:
    j = j.split()
    ceny.append(j)

iloscKilogramow=0
for element in range(0, len(dane)):
    iloscKilogramow = int(dane[element][2])
    for powtorka in range(element+1, len(dane)):

        if dane[element][1] == dane[powtorka][1]:
            iloscKilogramow += int(dane[powtorka][2])

    NIPYiIloscCukru.append(str(dane[element][1]) +","+ str(iloscKilogramow))
    iloscKilogramow = 0

maksymalnailosccukru = 0
nip =""
for rzecz in NIPYiIloscCukru:
    rzecz = rzecz.split(",")
    if int(rzecz[1]) > maksymalnailosccukru:
        maksymalnailosccukru = int(rzecz[1])
        nip=rzecz[0]


print(maksymalnailosccukru)
print(nip)




