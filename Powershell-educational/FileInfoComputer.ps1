<#
.SYNOPSIS
    Eksportuje dane o komponentach systemu do pliku CSV i wyświetla wybrane informacje.

.DESCRIPTION
    Tworzy strukturę danych o komponentach systemu, zapisuje ją do pliku CSV,
    a następnie na podstawie wartości "GenerateReport" wyświetla szczegółowe dane techniczne.

.EXAMPLE
    -> Plik CSV zostanie zapisany jako input_file.csv, a dane o systemie będą wypisane na podstawie konfiguracji.
#>

# Dane w postaci obiektów
$data = @(
 [PSCustomObject]@{ Component = "Computername"; GenerateReport = "True" }
 [PSCustomObject]@{ Component = "Manufacturer"; GenerateReport = "True" }
 [PSCustomObject]@{ Component = "Model"; GenerateReport = "True" }
 [PSCustomObject]@{ Component = "SerialNumber"; GenerateReport = "True" }
 [PSCustomObject]@{ Component = "CpuName"; GenerateReport = "True" }
 [PSCustomObject]@{ Component = "RAM"; GenerateReport = "True" }
)
# Zapis do CSV
$csvFilePath = "C:\Users\Pawel\input_file.csv"
$data | Export-Csv -Path $csvFilePath -NoTypeInformation -Delimiter ';'
Write-Host "Plik input_file.csv został utworzony w ścieżce $csvFilePath"
# Wczytanie CSV i Operacje
$inputFile = $csvFilePath
$dataFromCsv = Import-Csv -Path $inputFile -Delimiter ';'
# Pobranie dodatkowych inforrmacji o prroducencie z Computterinfo
$manufacturer = Get-ComputerInfo | Select-Object -ExpandProperty CsManufacturer
# Pobranie modelu z ComputerInfo
$model = Get-ComputerInfo | Select-Object -ExpandProperty CsModel
# Pobranie numeru seryjnego z ComputerInfo
$serialNumber = Get-ComputerInfo | Select-Object -ExpandProperty OsSerialNumber
# Pobierz pamięć RAM używając Win32_PhysicalMemory
$ramInfo = Get-WmiObject -Class Win32_PhysicalMemory
$ramGB = [math]::round(($ramInfo.Capacity | Measure-Object -Sum).Sum / 1GB, 2)
#Pobranie nazwy procesora z Win32
$cpuname = Get-WmiObject -Class Win32_Processor | Select-Object -First 1 -
ExpandProperty Name
# Iteracja po wierszach w pliku CSV
foreach ($row in $dataFromCsv) {
 # Sprawdzanie, czy GenerateReport jest ustawione na True
 if ($row.GenerateReport -eq "True") {
 # Wyświetlanie odpowiednich informacji w zależności od komponentu
 switch ($row.Component) {
 "Computername" {
 Write-Host "Computername: $($computerInfo.CsName)"
 }
 "Manufacturer" {
 Write-Host "Manufacturer: $manufacturer"
 }
 "Model" {
 Write-Host "Model: $model"
 }
 "SerialNumber" {
 Write-Host "SerialNumber: $serialNumber"
 }
 "CpuName" {
 Write-Host "Cpuname: $cpuname"
 }
 "RAM" {
 Write-Host "RAM: $ramGB GB"
 }
 }
 }
}