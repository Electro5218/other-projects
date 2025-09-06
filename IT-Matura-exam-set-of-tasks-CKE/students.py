# def pobierz_produkty():
#     produkty = []
#     while True:
#         dane = input("Podaj nazwe produktu, kategorię oraz cenę(wszystko po przecinku), a jak skończysz to napisz 'koniec': ")
#         if dane.lower() == 'koniec':
#             break
#         else:
#             czesci = dane.split(',')
#             nazwa = czesci[0].strip()
#             kategoria = czesci[1].strip()
#             cena = float(czesci[2].strip())
#             produkt = (nazwa, kategoria, cena)
#             produkty.append(produkt)
#     return produkty
#
#
# def kategorie(produkty):
#     slownik = {}
#     for produkt in produkty:
#         nazwa, kategoria, cena = produkt
#         if kategoria in slownik:
#             slownik[kategoria].append(nazwa)
#         else:
#             slownik[kategoria] = [nazwa]
#     return slownik
#
#
# def wyswietl_produkty(slownik_kategorii):
#     kategoria = input("Podaj kategorie jaka chcesz wyswietlic?: ").strip()
#     if kategoria in slownik_kategorii:
#         print(f"Produkty w kategorii {kategoria}")
#         for nazwa in slownik_kategorii[kategoria]:
#             print(f"- {nazwa}")
#     else:
#         print(f"Brak produktów w kategorii '{kategoria}")
#
# def main():
#     produkty = pobierz_produkty()
#     slownik_kat = kategorie(produkty)
#     wyswietl_produkty(slownik_kat)
#
# if __name__ == "__main__":
#     main()

def pobierz_studentow():
    studenci = []
    while True:
        decyzja = input("Czy chcesz dodac studenta? T/N ").strip().lower()
        if decyzja == 't':
            imie_nazwisko = input("Podaj imie i nazwisko studenta: ").strip()
            wiek = int(input("Podaj wiek studenta: ").strip())
            oceny_input = input("Podaj oceny w formacie" "Przedmiot1:ocena1, Przedmiot2:ocena2").strip()
            oceny_lista = oceny_input.split(',')
            oceny = {}
            for ocena_str in oceny_lista:
                przedmiot,ocena = ocena_str.split(':')
                przedmiot = przedmiot.strip()
                oceny[przedmiot] = int(ocena.strip())
                student = {'imie': imie_nazwisko, 'wiek': wiek, 'oceny': oceny}
                studenci.append(student)
        elif decyzja == 'n':
            break
        else:
            print("wpisz poprawnie")
    return studenci

def obliczsrednia(oceny):
    if len(oceny) == 0:
        return 0
    suma = sum(oceny.values())
    srednia = suma / len(oceny)
    return srednia

def znajdz_najlepszego_studenta(studenci):
    najlepszy_student = None
    najwyzsza_srednia = -1
    for student in studenci:
        srednia = obliczsrednia(student['oceny'])
        if srednia > najwyzsza_srednia:
            najwyzsza_srednia = srednia
            najlepszy_student = student
    return najlepszy_student, najwyzsza_srednia

def main():
    studenci = pobierz_studentow()
    for student in studenci:
        srednia = obliczsrednia(student['oceny'])
        print(f"\nStudent: {student['imie']}, Wiek: {student['wiek']}")
        print("oceny:")
        for przedmiot,ocena in student['oceny'].items():
            print(f" - {przedmiot}: {ocena}")
        print(f"Średnia ocen: {srednia:.2f}")
    najlepszy_student, najwyzsza_srednia = znajdz_najlepszego_studenta(studenci)
    if najlepszy_student:
        print(f"\nNajwyzsza srednia ma {najlepszy_student['imie']}" f" - {najwyzsza_srednia:.2f}")
    else:
        print("Brak danych o studentach")

if __name__ == "__main__":
    main()

