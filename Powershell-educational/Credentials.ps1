<#
.SYNOPSIS
    Prosty mechanizm logowania.

.DESCRIPTION
    Pobiera nazwę użytkownika i hasło, a następnie weryfikuje, czy są zgodne z domyślnymi wartościami ('admin', 'password').

.EXAMPLE
    Podaj nazwę użytkownika: admin
    Podaj hasło: password
    -> Dostęp przyznany!
#>

$username = Read-Host "Podaj nazwę użytkownika"
$password = Read-Host "Podaj hasło"
if ($username -eq "admin" -and $password -eq "password") {
 Write-Host "Dostęp przyznany!"
} else {
 Write-Host "Nieprawidłowa nazwa użytkownika lub hasło."
}