<#
.SYNOPSIS
    Generuje ciąg adresów IP w zakresie 192.168.1.1–192.168.1.10

.DESCRIPTION
    Używa pętli for, by wypisać 10 adresów IP z rosnącym czwartym oktetem.

.EXAMPLE
    -> 192.168.1.1
       192.168.1.2
       ...
       192.168.1.10
#>
for($i = 1; $i -le 10; $i++) {
 $ip = "192.168.1.$i"
 Write-Host $ip
}