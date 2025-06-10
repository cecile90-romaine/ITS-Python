# Esercizio_4:
"""
ext Analysis:

    Create a function that takes a paragraph and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.

"""
def count_word_occurrences(paragraph: str) -> None:
    # Convert the text to lowercase
    paragraph = paragraph.lower()

    # Split the text into individual words
    words: list[str] = paragraph.split()

    # Dictionary to store word occurrences
    word_count: dict[str, int] = {}

    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print the word frequency report
    print("Word frequency report:\n")
    for word in word_count:
        print(f"{word}: {word_count[word]}")

# Example usage:
text: str = "this is an example this is simple"
count_word_occurrences(text)