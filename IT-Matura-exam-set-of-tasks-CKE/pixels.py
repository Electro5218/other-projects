plik = open("dane.txt", "r").readlines()
dane = []

for i in plik:
    i = i.split()
    dane.append(i)

iletakichpikseli = 0
for y in range(0, len(dane)):
    for x in range(0, len(dane[y])):
        if x==0 and y == 0:
            if abs(int(dane[y][x+1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif y == 0 and x>0 and x < len(dane[y])-1:
            if abs(int(dane[y][x-1]) - int(dane[y][x])) > 128 or abs(int(dane[y][x+1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif y == 0 and x == len(dane[y]) - 1:
            if abs(int(dane[y][x-1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif 0 < y < len(dane) - 1 and x == 0:
            if abs(int(dane[y-1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x+1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif 0< y < len(dane)-1 and 0 < x < len(dane[y])-1:
            if abs(int(dane[y-1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x+1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x-1]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif 0 < y < len(dane)-1 and x == len(dane[y])-1:
            if abs(int(dane[y-1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x-1]) - int(dane[y][x])) > 128 or abs(int(dane[y+1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif y == len(dane) - 1 and x == 0:
            if abs(int(dane[y-1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x+1]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif y == len(dane) - 1 and 0 < x < len(dane[y]) - 1:
            if abs(int(dane[y-1][x]) - int(dane[y][x])) > 128 or abs(int(dane[y][x-1]) - int(dane[y][x])) > 128 or abs(int(dane[y][x+1]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1
        elif y == len(dane) - 1 and x == len(dane[y]) - 1:
            if abs(int(dane[y][x-1]) - int(dane[y][x])) > 128 or abs(int(dane[y-1][x]) - int(dane[y][x])) > 128:
                iletakichpikseli += 1


print(iletakichpikseli)
