# Vigenere cipher encryption and decryption in Python

def encrypt(plain_text, key):
    """Encrypts the given plaintext using the Vigenere cipher with the given key"""
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            # Shift the character by the corresponding key value, wrapping around the alphabet if necessary
            shifted_char = chr((ord(char) - ord('a') + ord(key[key_index % len(key)]) - ord('a')) % 26 + ord('a'))
            cipher_text += shifted_char
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    """Decrypts the given ciphertext using the Vigenere cipher with the given key"""
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            # Shift the character backwards by the corresponding key value, wrapping around the alphabet if necessary
            shifted_char = chr((ord(char) - ord('a') - (ord(key[key_index % len(key)]) - ord('a'))) % 26 + ord('a'))
            plain_text += shifted_char
            key_index += 1
        else:
            plain_text += char
    return plain_text

# Example usage
key = "lemon"
plain_text = "attackatdawn"
cipher_text = encrypt(plain_text, key)
print("Encrypted text:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)
