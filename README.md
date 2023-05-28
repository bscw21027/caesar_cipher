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

# Contribution
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments
- The Caesar Cipher app is built using the Python programming language.
- The project structure and code organization are inspired by best practices for Python projects.

# Contact
If you have any questions, suggestions, or issues, please feel free to contact the project maintainer at bsce21027@itu.edu.pk
