# esrcizio 8-2. Favorite Book: 
"""
Write a function called favorite_book() that accepts one parameter, title. 
 The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
 Call the function, making sure to include a book title as an argument in the function call."""

# definisco funzione favourite_book(), passando in input un titolo generico
def favorite_book(title:str) -> None:
    print(f"One of my favorite books is {title}")

# chiamare la funzione favourite_book, passando in input il nome del mio libro preferito,
# ovvero Alice in WONDERLAND.
favorite_book("Alice in Wonderland")
favorite_book("Harry Potter")

