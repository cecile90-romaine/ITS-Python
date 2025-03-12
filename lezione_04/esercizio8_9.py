 # esercizio8_9. Messages:

"""
 Make a list containing a series of short text messages. 
 Pass the list to a function called show_messages(), which prints each text message """

def show_messages(message):
    
    for message in messages:    
        print(message) 

messages:list = ["ciao come stai?", "ciao come ti chiami?", "di dove sei?", "quanti anni hai?"]

print(show_messages(messages))
