# Caesar Cipher in Python
This is a simple implementation of the Caesar Cipher encryption algorithm in Python. The Caesar Cipher, also known as the shift cipher, is one of the earliest and simplest encryption techniques. It works by shifting each letter in the plaintext by a certain number of positions down the alphabet.

# Usage
To use the Caesar Cipher, follow these steps:

- Clone the repository or download the caesar_cipher.py file.

- Import the caesar_cipher module into your Python script:
  ```python
   from caesar_cipher import encrypt, decrypt
  ```
- **Encryption:** To encrypt a plaintext, use the caesar_encrypt function:
  ```python
  ciphertext = encrypt(plaintext, shift)
  ```
  - **plaintext:** The text you want to encrypt.
  - **shift:** The number of positions to shift each letter. A positive value for shifting to the right, and a negative value for shifting to the left.

- **Decryption:** To decrypt a ciphertext, use the caesar_decrypt function:
  ```python
  plaintext = decrypt(ciphertext, shift)
  ```
  - **ciphertext:** The text you want to decrypt.
  - **shift:** The number of positions the letters were shifted during encryption. Make sure to use the same shift value used during encryption.
