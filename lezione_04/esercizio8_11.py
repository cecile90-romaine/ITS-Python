# esercizio8_11. Archived Messages:

"""
Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages.
 After calling the function, print both of your lists to show that 
 the original list has retained its messages."""

def send_message( messages):
    for message in messages:
        print(message)
messages:list = ["buongiorno come stai?", "ciao cara vieni oggi?", "dove sta andando?", "arrivederci?"]

print(send_message(messages))