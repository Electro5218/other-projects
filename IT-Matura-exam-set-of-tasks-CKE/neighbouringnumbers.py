file = open("liczby.txt", "r").read().split()

liczby = []
for i in file:
    liczby.append(i)


def NWD(a, b):
    b = int(b)
    a = int(a)
    if b>0:
        return NWD(b, a%b)
    return a


liczbysasiadujaceznwd1 = []
liczbywzgledniepierwsze = []

for i in range(0, len(liczby)-1):
    czyNWDrowne1 = True
    for l in range(0, len(liczby)-1):
        if NWD(liczby[i], liczby[l+1]) != 1:
            if liczby[i] != liczby[l+1]:
                czyNWDrowne1 = False
    if czyNWDrowne1 == True:
        liczbywzgledniepierwsze.append(liczby[i])
    czyNWDrowne1 = True


print(max(liczbywzgledniepierwsze))















