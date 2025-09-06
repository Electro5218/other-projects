from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

# 1. Generowanie kluczy RSA 
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,#2048bitow
)

public_key = private_key.public_key()

# Zapis kluczy do pliku
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

# 2. Wczytaj plik do podpisania
file_path = "LAB12TASK3/file_to_sign.txt"
with open(file_path, "rb") as f:
    file_data = f.read()

# 3. Podpisz plik kluczem prywatnym
signature = private_key.sign(
    file_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Zapisz podpis do pliku
with open("plik_do_podpisania.sig", "wb") as f:
    f.write(signature)

print("Plik został podpisany cyfrowo.")

# 4. Weryfikacja podpisu (na podstawie publicznego klucza)
try:
    public_key.verify(
        signature,
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Podpis jest poprawny — plik nie został zmieniony.")
except Exception:
    print("Błąd: podpis jest niepoprawny lub plik został zmieniony.")
