# 🔐 AES Encryption/Decryption

This Python project demonstrates symmetric encryption and decryption using AES (Advanced Encryption Standard) in CBC mode with PKCS7 padding. It uses Python's `cryptography` library to securely encrypt and decrypt text. The script generates a random 256-bit key and a 128-bit IV, encrypts a plaintext message, and then decrypts it back to verify the original text.

To use the script, install the required library with `pip install cryptography`, open the Python file, modify the `data` variable to the text you want to encrypt, and run it. The program will output the encrypted bytes and then the decrypted text, showing that the original message is correctly recovered.

For example, running the script with the message `"Hasło do konta na PayPal Elona Muska to XAE A12"` will produce encrypted bytes like `b'\x93\xab\xcd...'` and then output the decrypted text `"Hasło do konta na PayPal Elona Muska to XAE A12"`.

This project demonstrates key skills in symmetric encryption, handling padding for block ciphers, generating secure random keys and IVs, and using Python’s `cryptography` library for cryptographic operations. It is designed for educational purposes only; do not use this code with real sensitive data in production without proper key management and secure practices. Possible improvements include allowing input/output via files, supporting different AES modes, implementing secure key storage, and extending the script for batch encryption or decryption.

✅ This project is part of my security-focused portfolio, showcasing practical cryptography skills relevant for SOC Analyst, Security Engineer, Pentester, and Security Analyst roles.
