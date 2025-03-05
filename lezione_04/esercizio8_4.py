# esercizio 8-4. Large Shirts:

"""
#  Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message."""

def make_shirt( size, message):
    print(f" the size is {size}, the message is  {message} : ")

make_shirt("M", " I love Python: ")
make_shirt("L", "American first: ")
make_shirt("s", "I love country: ")