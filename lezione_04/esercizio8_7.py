# esercizio 8-7. Album:
"""
#  Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the  dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.
"""
def make_album(myalbum:str, artist:str) -> dict[str, str]:
    return {"album": myalbum, "artist": artist}

print(make_album("natura" , "Cecile")) # ho creato il primo dizionario
print(make_album("cavolo", "marius"))  # ho creato il secondo dizionario
print(make_album("caramella", "Natalia"))  # ho creato il terzo dizionario


#edf make_dict(name_album: str, artist:str, song_title:str):
#    return{"album": name_album, "artist":artist, "song":song_title}



 