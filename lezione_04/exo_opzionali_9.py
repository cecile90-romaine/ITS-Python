# Esercizio_9:
"""
Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
     Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.


"""
from typing import Any

# Function to encrypt or decrypt text using the Caesar cipher
def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    result: str = ""  # Initialize the result string

    # If decrypting, reverse the direction of the shift
    if decrypt:
        shift = -shift

    # Iterate over each character in the input text
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            # Determine the ASCII base (A or a) for correct case handling
            if char.isupper():
                base: int = ord('A')
            else:
                base: int = ord('a')

            # Shift the character within the alphabet range and append to result
            # (ord(char) - base) gives a 0–25 index in the alphabet
            # Adding shift and taking modulo 26 wraps around the alphabet
            # Adding base back converts index to a character again
            # Shift the character and append it to the result
            shifted_char_code: int = (ord(char) - base + shift) % 26 + base
            shifted_char: str = chr(shifted_char_code)
            result += shifted_char
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result  # Return the final encrypted or decrypted string

# Example usage
msg: str = "Hello World"
encrypted: str = caesar_cipher(msg, 3)  # Encrypt the message with a shift of 3
decrypted: str = caesar_cipher(encrypted, 3, decrypt=True)  # Decrypt using the same shift

# Output the results
print("Encrypted:", encrypted)  # Should print something like: Khoor Zruog
print("Decrypted:", decrypted)  # Should print: Hello World