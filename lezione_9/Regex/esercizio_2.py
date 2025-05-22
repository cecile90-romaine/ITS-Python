# esericizio_2: Riconoscere parole.

'''
Obiettivo: Lavorare con lettere e lunghezze di stringhe.

    Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
    Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
    Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

'''
import re
# Esercizio 2.1
text: str = "buongiorno"

parola:str = re.search(r'^[a-z]+$', text) #una o più lettere minuscole)
print(parola)


# Esercizio 2.2
text:str = "congraTUlaZioni"
parola:str = re.search(r'^[a-zA-Z]+$ ',text) # Lettere maiuscole e minuscole)
print(parola)

# esercizio2.3
text:str = "Buona"

parola:str = re.search(r'^[a-zA-Z]{5,10}$', text) #Tra 5 e 10 lettere, senza numeri)
print(parola)
