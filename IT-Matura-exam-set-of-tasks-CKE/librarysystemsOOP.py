import csv
import threading
import time
from datetime import datetime
import webbrowser
import pandas as pd


class Ksiazka():
    def __init__(self, tytul, autor, rok, ISBN, dostepnosc="True"):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ISBN = ISBN
        self.dostepnosc = dostepnosc
        self.data = datetime.now()

    def wyswietl_info(self):
        Status = "Dostepny" if self.dostepnosc else "Wypozyczony"
        print(f"{self.tytul}, {self.autor}, {self.rok}, {self.ISBN}, Status: {Status}, Utworzone: {self.data}")


class Biblioteka():
    def __init__(self, plik='ksiazki.csv'):
        self.plik = plik
        self.ksiazki = self.wczytaj_ksiazki()

        self.thread_stop = False
        self.auto_zapis_watek = threading.Thread(target=self.auto_zapis, daemon=True)
        self.auto_zapis_watek.start()

    def wczytaj_ksiazki(self):
        ksiazki = []
        try:
            plik = open("ksiazki.csv", "r", newline='', encoding='utf-8')
            reader = csv.DictReader(plik)
            for row in reader:
                ksiazka = Ksiazka(row['tytul'], row['autor'], row['rok'], row['ISBN'], row['dostepnosc'] == 'True')
                ksiazki.append(ksiazka)
        except FileNotFoundError:
            pass
        return ksiazki

    def zapisz_ksiazke(self):
        plik = open("ksiazki.csv", "w", newline='', encoding='utf-8')
        fieldnames = ['tytul', 'autor', 'rok', 'ISBN', 'data', 'dostepnosc']
        writer = csv.DictWriter(plik, fieldnames=fieldnames)
        writer.writeheader()
        for ksiazka in self.ksiazki:
            writer.writerow({
                'tytul': ksiazka.tytul,
                'autor': ksiazka.autor,
                'rok': ksiazka.rok,
                'ISBN': ksiazka.ISBN,
                'dostepnosc': ksiazka.dostepnosc,
                'data': ksiazka.data
            })

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)
        self.zapisz_ksiazke()
        print("Pomyslnie dodano ksiazke")

    def usun_ksiazke(self, tytul):
        nowe_ksiazki = []
        for ksiazka in self.ksiazki:
            if ksiazka.tytul != tytul:
                nowe_ksiazki.append(ksiazka)
        if len(nowe_ksiazki) == len(self.ksiazki):
            print(f"Ksiazka '{tytul}' nie zostala znaleziona.")
        else:
            self.ksiazki = nowe_ksiazki
            self.zapisz_ksiazke()
            print(f"Ksiazka '{tytul}' zostala usunieta.")

    def znajdz_ksiazke(self, tytul):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul:
                ksiazka.wyswietl_info()
                return ksiazka
        print("Ksiazka nie znaleziona")
        return None

    def wypozycz_ksiazke(self, tytul):
        ksiazka = self.znajdz_ksiazke(tytul)
        if ksiazka and ksiazka.dostepnosc:
            ksiazka.dostepnosc = False
            self.zapisz_ksiazke()
            print(f"Wypozyczono: '{tytul}'")
        else:
            print("Nie znaleziono ksiazki")

    def zwroc_ksiazke(self, tytul):
        ksiazka = self.znajdz_ksiazke(tytul)
        if ksiazka and ksiazka.dostepnosc == False:
            ksiazka.dostepnosc = True
            self.zapisz_ksiazke()
            print(f"Oddano ksiazke '{tytul}'")
        else:
            print("Nie znaleziono ksiazki")

    def znajdz_ksiazke_po_isbn(self, isbn):
        for ksiazka in self.ksiazki:
            if ksiazka.ISBN == isbn:
                ksiazka.wyswietl_info()
                return ksiazka
        print("Ksiazka po isbn nie znaleziona")
        return None

    def auto_zapis(self, interval=10):
        while not self.thread_stop:
            time.sleep(interval)
            print("\n" + "Automatyczny zapis...")
            self.zapisz_ksiazke()

    def zatrzymaj_auto_zapis(self):
        self.thread_stop = True
        self.auto_zapis_watek.join()
        print("Automatyczny zapis zatrzymany.")


def automatyzacja(link):
    webbrowser.open('https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + str(link) + '&search_type=books')


def analiza_ksiazek(plik_csv):
    try:
        df = pd.read_csv(plik_csv)
        print(f"Dane załadowane pomyślnie z pliku: {plik_csv}\n")

        if 'dostepnosc' not in df.columns:
            print("Błąd: Kolumna 'dostepna' nie została znaleziona w danych.")
            return

        liczba_dostepnych = df['dostepnosc'].value_counts().get(True, 0)
        liczba_wypozyczonych = df['dostepnosc'].value_counts().get(False, 0)

        liczba_ksiazek = liczba_dostepnych + liczba_wypozyczonych

        # Wyświetlenie wyników
        print(f"Liczba dostępnych książek: {liczba_dostepnych}")
        print(f"Liczba wypożyczonych książek: {liczba_wypozyczonych}")
        print(f"Całkowita liczba książek: {liczba_ksiazek}")

        # Obliczanie procentów
        if liczba_ksiazek > 0:
            procent_dostepnych = (liczba_dostepnych / liczba_ksiazek) * 100
            procent_wypozyczonych = (liczba_wypozyczonych / liczba_ksiazek) * 100
            print(f"Procent dostępnych książek: {procent_dostepnych:.2f}%")
            print(f"Procent wypożyczonych książek: {procent_wypozyczonych:.2f}%")
        else:
            print("Brak książek w zbiorze.")

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{plik_csv}'.")
    except pd.errors.EmptyDataError:
        print(f"Błąd: Plik '{plik_csv}' jest pusty.")
    except pd.errors.ParserError:
        print(f"Błąd: Nie można przetworzyć pliku '{plik_csv}'. Sprawdź format CSV.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


def main_menu():
    biblioteka = Biblioteka()
    while True:
        try:
            print("Witam w programie Biblioteki książek z analizą danych oraz automatyzacją")
            print(
                "Wybierz jedną z opcji \n 1 - Dodaj Ksiazke \n 2 - Usun ksiazke \n 3 - Znajdz ksiazke po tytule \n 4 - Wypozycz ksiazke \n 5 - Zwroc ksiazke \n 6 - Znajdz ksiazke po isbn \n 7 - Wyswietl dane wszystkich ksiazek \n 8 - Wyszukanie ksiazki w good reads \n 9 - Wyswietl Dane Analityczne \n 10 - Zakoncz prace programu \n 11 - Zatrzymaj auto zapis")
            decyzja = int(input("Twoja decyzja:"))
            if decyzja == 1:
                tytul = input("Podaj tytul ksiazki:")
                autor = input("Podaj autora ksiazki:")
                rok = input("Podaj rok utworzenia ksiazki:")
                isbn = input("Podaj isbn ksiazki:")
                ksiazka = Ksiazka(tytul, autor, rok, isbn)
                biblioteka.dodaj_ksiazke(ksiazka)
            elif decyzja == 2:
                tytul = input("Podaj tytul ksiazki:")
                biblioteka.usun_ksiazke(tytul)
            elif decyzja == 3:
                tytul = input("Podaj tytul ksiazki:")
                biblioteka.znajdz_ksiazke(tytul)
            elif decyzja == 4:
                tytul = input("Podaj tytul ksiazki ktora chcesz wypozyczyc:")
                biblioteka.wypozycz_ksiazke(tytul)
            elif decyzja == 5:
                tytul = input("Podaj tytul ksiazki ktora chcesz zwrocic:")
                biblioteka.zwroc_ksiazke(tytul)
            elif decyzja == 6:
                ISBN = input("Podaj isbn ksiazki ktora chcesz znalezc:")
                biblioteka.znajdz_ksiazke_po_isbn(ISBN)
            elif decyzja == 7:
                for ksiazka in biblioteka.ksiazki:
                    ksiazka.wyswietl_info()
            elif decyzja == 8:
                tytul = input("Podaj tytul ksiazki ktora chcesz wyszukac w goodreads.com:")
                tytul = tytul.replace(' ', '+')
                automatyzacja(tytul)
            elif decyzja == 9:
                plik = 'ksiazki.csv'
                analiza_ksiazek(plik)
            elif decyzja == 10:
                break
            elif decyzja == 11:
                biblioteka.zatrzymaj_auto_zapis()
            else:
                print("Zła decyzja spróbuj ponownie")
                continue
        except:
            print("To nie numer")
            continue


if __name__ == '__main__':
    main_menu()