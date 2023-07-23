# Encryption and Decryption Methods

This Python script provides two methods for encrypting and decrypting messages: Substitution and Transposition. The user can choose to either encrypt or decrypt a message and select the encryption method accordingly.

## Substitution Encryption and Decryption

### `substitution_encrypt(userMessage, key)`

This function takes two arguments:
- `userMessage`: A string representing the message that needs to be encrypted.
- `key`: An integer representing the substitution key for encryption.

The function performs a simple substitution cipher on the `userMessage`, shifting each alphabet character (both uppercase and lowercase) by the `key` positions in the English alphabet. Non-alphabetic characters remain unchanged. The encrypted message is then returned as a string.

### `substitution_decrypt(encryptedMessage, key)`

This function takes two arguments:
- `encryptedMessage`: A string representing the message that needs to be decrypted.
- `key`: An integer representing the substitution key used for encryption.

The function reverses the substitution cipher by shifting each alphabet character (both uppercase and lowercase) backward by the `key` positions in the English alphabet. Non-alphabetic characters are left unchanged. The decrypted message is then returned as a string.

## Transposition Encryption and Decryption

### `transposition_encrypt(userMessage, key)`

This function takes two arguments:
- `userMessage`: A string representing the message that needs to be encrypted.
- `key`: An integer representing the transposition key for encryption.

The function performs a transposition cipher by rearranging the characters in `userMessage` in a columnar format, based on the `key`. The encrypted message is then returned as a string.

### `transposition_decrypt(encryptedMessage, key)`

This function takes two arguments:
- `encryptedMessage`: A string representing the message that needs to be decrypted.
- `key`: An integer representing the transposition key used for encryption.

The function reverses the transposition cipher and reconstructs the original message from the `encryptedMessage` using the `key`. The decrypted message is then returned as a string.

## Usage

Upon running the script, the user will be prompted to select either encryption or decryption. Depending on the chosen operation, the user will provide the message and the appropriate encryption or decryption method. For encryption, a key must be provided to perform the encryption. For decryption, the same key used for encryption must be provided to decrypt the message.

Note: This code is intended for educational and basic encryption/decryption purposes only and should not be used for sensitive data or real-world security applications.