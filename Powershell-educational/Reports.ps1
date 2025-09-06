<#
.SYNOPSIS
    Generuje pełny raport informacji o systemie i zapisuje go do pliku.

.DESCRIPTION
    Funkcja `Get-SystemInfo` pobiera dane takie jak nazwa komputera, model, producent, procesor, RAM itp.,
    po czym zapisuje je do pliku z datą i godziną w nazwie.

.EXAMPLE
    -> Raport zostanie zapisany jako: ComputerReport_20250415-143000.txt
#>

# Funkcja do zbierania danych o systemie
function Get-SystemInfo {
 $computerInfo = Get-ComputerInfo
 $wmic = Get-WmiObject -Class Win32_ComputerSystem
 # Pobieranie dodatkowych informacji o komputerze
 $manufacturer = Get-ComputerInfo | Select-Object -ExpandProperty CsManufacturer
 $model = Get-ComputerInfo | Select-Object -ExpandProperty CsModel
 $serialNumber = Get-ComputerInfo | Select-Object -ExpandProperty OsSerialNumber
 $cpuname = Get-WmiObject -Class Win32_Processor | Select-Object -First 1 -
ExpandProperty Name
 # Pobieranie pamięci RAM
 $ramInfo = Get-WmiObject -Class Win32_PhysicalMemory
 $ramGB = [math]::round(($ramInfo.Capacity | Measure-Object -Sum).Sum / 1GB, 2)
 # Zwrócenie wyników
 return @{
 Computername = $computerInfo.CsName
 Manufacturer = $manufacturer
 Model = $model
 SerialNumber = $serialNumber
 RAM = "$ramGB GB"
 CPUNAME = $cpuname
 }
}
# Uzyskiwanie informacji o systemie
$systemInfo = Get-SystemInfo
# Generowanie nazwy pliku na podstawie bieżącej daty i godziny
$currentDateTime = Get-Date -Format "yyyyMMdd-HHmmss"
$outputFilePath = "C:\Users\Pawel\ComputerReport_$currentDateTime.txt"
# Przygotowanie zawartości raportu
$outputContent = @"
Computername: $($systemInfo.Computername)
Manufacturer: $($systemInfo.Manufacturer)
Model: $($systemInfo.Model)
SerialNumber: $($systemInfo.SerialNumber)
RAM: $($systemInfo.RAM)
CPUNAME: $($systemInfo.CPUNAME)
"@
# Zapisanie danych do pliku
$outputContent | Out-File -FilePath $outputFilePath
# Wyświetlenie komunikatu z pełną ścieżką do pliku
Write-Host "Raport został zapisany w pliku: $outputFilePath"
Computername: DESKTOP-NP00C64
Manufacturer: ASUS
Model: System Product Name
SerialNumber: 00325-80000-00000-AAОЕ