<#
.SYNOPSIS
    Oblicza pole trójkąta na podstawie podanej podstawy i wysokości.

.DESCRIPTION
    Skrypt przyjmuje dwa parametry: podstawę i wysokość, po czym oblicza pole trójkąta za pomocą wzoru (1/2 * podstawa * wysokość).

.PARAMETER podstawa
    Długość podstawy trójkąta (w jednostkach dowolnych).

.PARAMETER wysokosc
    Wysokość opuszczona na podstawę trójkąta.

.EXAMPLE
    .\Trianglearea.ps1 -podstawa 5 -wysokosc 10
#>
param(
 [double]$podstawa,
 [double]$wysokosc
)
$pole = 0.5 * $podstawa * $wysokosc
Write-Host "Pole trójkąta o podstawie $podstawa i wysokości $wysokosc wynosi: $pole"