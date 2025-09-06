<#
.SYNOPSIS
    Sprawdza, czy podana liczba jest większa, mniejsza lub równa 10.

.DESCRIPTION
    Skrypt pobiera liczbę od użytkownika i porównuje ją z wartością 10. Informuje o wyniku porównania.

.EXAMPLE
    Podaj liczbę: 12
    -> Liczba jest większa od 10
#>

$liczba = Read-Host "Podaj liczbę"
if ($liczba -as [double]) {
 $liczba = [double]$liczba
} else {
 Write-Host "Proszę podać poprawną liczbę"
 exit
}
if ($liczba -gt 10) {
 Write-Host "Liczba jest większa od 10"
} else {
 Write-Host "Liczba jest mniejsza lub równa 10"
}