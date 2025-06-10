# Esercizio_6:
"""
Password Generator:

    Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.

"""

# Importing necessary modules
import random   # Used for selecting random characters
import string   # Provides string constants like ascii_letters, digits, punctuation

# Function to generate a random password
def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    # Start with lowercase letters
    characters: str = string.ascii_lowercase

    # Add uppercase letters if requested
    if use_upper:
        characters += string.ascii_uppercase

    # Add digits if requested
    if use_digits:
        characters += string.digits

    # Add symbols/punctuation if requested
    if use_symbols:
        characters += string.punctuation

    # Initialize the password as an empty string
    password: str = ""

    # Generate password by randomly selecting characters from the pool
    for i in range(length):
        password += random.choice(characters)

    # Return the final generated password
    return password

# Example usage: Generate a 12-character password using all character types
print(f'The generated password is: {generate_password(12, True, True, True)}')