plik = open("pi.txt", "r").readlines()
dane = []

for b in plik:
    b = b.strip()
    dane.append(b)

licznik = 0
ciagi = []

for i in range(len(dane) - 5):
    rosnie = True
    maleje = True
    poprzednia = int(dane[i])
    for j in range(1,6):
        badana = int(dane[i+j])
        if rosnie and badana <= poprzednia:
            if i + 1 == i + j:
                rosnie = False
                maleje = False
                break
            rosnie = False
        elif not rosnie and maleje and badana >= poprzednia:
            maleje = False
            break
        poprzednia = badana
    if rosnie == False and maleje == True:
        mal = False
        ciag = dane[i:i+j+1]
        for k in range(len(ciag)-1):
            if int(ciag[k+1]) < int(ciag[k]):
                mal = True
        if mal:
            licznik += 1
            ciagi.append(dane[i:i+j+1])

print(licznik)
print(ciagi)