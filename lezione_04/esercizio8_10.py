# essercizio8_10. Sending Messages: 

"""
Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message 
and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly. """


def show_messages(messages):
    
    for message in messages:    
        print(message) 

messages:list = ["ciao come stai?", "ciao come ti chiami?", "di dove sei?", "quanti anni hai?"]

print(show_messages(messages))

def send_message( messages):
    for message in messages:
        print(message)
messages:list = ["buongiorno come stai?", "ciao cara vieni oggi?", "dove sta andando?", "arrivederci?"]

print(send_message(messages))