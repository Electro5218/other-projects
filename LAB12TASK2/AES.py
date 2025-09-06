from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Przygotowanie klucza i IV
key = os.urandom(32)  # 256-bitowy AES
iv = os.urandom(16)   # 128-bitowy IV, AES CBC

# Tekst do zaszyfrowania
data = "Hasło do konta na PayPal Elona Muska to XAE A12".encode("utf-8")

# Padding (AES wymaga bloków 16 bajtów)
padder = padding.PKCS7(128).padder()
padded_data = padder.update(data) + padder.finalize()

# Szyfrowanie
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
encrypted = encryptor.update(padded_data) + encryptor.finalize()

# Deszyfrowanie
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()

# Usunięcie paddingu
unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

print("Zaszyfrowane:", encrypted)
print("Odszyfrowane:", decrypted.decode())
