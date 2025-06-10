# Esercizio_10:
"""
Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.


"""

# Function to check whether two strings are anagrams
def are_anagrams(str1: str, str2: str) -> bool:
    clean1: str = ""  # Initialize cleaned version of the first string
    clean2: str = ""  # Initialize cleaned version of the second string

    # Process the first string: keep only alphabetic characters and convert to lowercase
    for c in str1:
        if c.isalpha():           # Check if the character is a letter
            clean1 += c.lower()   # Convert to lowercase and add to clean1

    # Process the second string similarly
    for c in str2:
        if c.isalpha():           # Check if the character is a letter
            clean2 += c.lower()   # Convert to lowercase and add to clean2

    # Sort both cleaned strings and compare them
    # If the sorted characters match, the strings are anagrams
    return sorted(clean1) == sorted(clean2)

# Example usage
print(are_anagrams("Listen!", "Silent"))     # Output: True (they are anagrams)
print(are_anagrams("Hello", "World"))        # Output: False (not anagrams)