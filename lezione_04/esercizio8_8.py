# esercizio 8-8. User Albums:
"""
Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop. """


def make_album(myalbum:str, artist:str) -> dict[str, str]:
    return {"album": myalbum, "artist": artist}

print(make_album("natura" , "Cecile")) # ho creato il primo dizionario
print(make_album("cavolo", "marius"))  # ho creato il secondo dizionario
print(make_album("caramella", "Natalia"))  # ho creato il terzo dizionario

while True:
    artist = input("inserire il none di un artisto")
    title = input("inserire un title ")
    if artist.lower() == " quit":
        break
    else:
        print("quit at any time to exit the programm")
print(make_album)

