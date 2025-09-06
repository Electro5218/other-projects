<#
.SYNOPSIS
    Wyświetla podstawowe informacje o systemie, użytkowniku i aktualnej dacie.

.DESCRIPTION
    Skrypt pobiera i wyświetla:
      - aktualną datę i godzinę,
      - nazwę systemu operacyjnego,
      - wersję systemu,
      - nazwę użytkownika,
      - adresy IP przypisane do interfejsu Ethernet.

.EXAMPLE
    .\Get-SystemSnapshot.ps1
    -> Zwraca datę, nazwę użytkownika, nazwę systemu, wersję systemu i IP (jeśli dostępne).
#>
$data = Get-Date
$system = Get-ComputerInfo | Select-Object -ExpandProperty OsName
$version = Get-ComputerInfo | Select-Object -ExpandProperty OsVersion
$user = $env:USERNAME
$ip = Get-NetIPAddress | Where-Object {$_.InterfaceAlias -eq "Ethernet"}
Write-Host "Aktualna data na $user to $data" dla tego napisz get-help