<#
.SYNOPSIS
    Wykonuje podstawowe operacje na plikach, procesach i wyświetla informacje o systemie.

.DESCRIPTION
    Skrypt:
    - Tworzy i zmienia nazwę pliku,
    - Oblicza jego sumę kontrolną SHA256,
    - Uruchamia Notatnik,
    - Sortuje pliki w katalogu według długości nazw,
    - Zapisuje aktualną lokalizację do pliku,
    - Wyświetla listę pierwszych 5 procesów,
    - Sortuje procesy według zużycia pamięci (największe i najmniejsze),
    - Wyświetla 5 procesów o najmniejszym zużyciu pamięci.

.EXAMPLE
    .\ProcesyIOperacje.ps1
    -> Uruchamia wszystkie opisane operacje i wyświetla dane na ekranie.

.NOTES
    Wymaga: Uprawnień do zapisu w C:\Temp
#>

# Tworzenie nowego pliku
New-Item -Path "C:\Temp\plik1.txt" -ItemType File

# Zmiana nazwy pliku
Rename-Item -Path "C:\Temp\plik1.txt" -NewName "nowy_plik.txt"

# Obliczenie sumy kontrolnej SHA256
Get-FileHash -Path "C:\Temp\nowy_plik.txt" -Algorithm SHA256

# Uruchomienie Notatnika
Start-Process notepad

# Sortowanie plików w bieżącym katalogu według długości nazw
Get-ChildItem | Sort-Object {$_.Name.Length}

# Zapisanie bieżącej lokalizacji do pliku
$lokalizacja = Get-Location
$lokalizacja | Out-File -FilePath "C:\Temp\lokalizacja.txt"

# Wyświetlenie 5 pierwszych procesów
Get-Process | Select-Object -First 5 ProcessName, Id

# 5 procesów o największym zużyciu pamięci (WorkingSet - WS)
Get-Process | Sort-Object -Property WS -Descending | Select-Object -First 5 ProcessName, WS

# 5 procesów o najmniejszym zużyciu pamięci
Get-Process | Sort-Object -Property WS | Select-Object -First 5 `
    @{Name="ProcessName";Expression={$_.ProcessName}}, `
    @{Name="MemoryUsage";Expression={$_.WS}}
