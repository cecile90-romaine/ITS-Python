# Esercizio_1: Riconoscere numeri.
'''
1. Riconoscere numeri

Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

 Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).
'''
import re 

# RegEx che riconosca un numero intero positivo.

text:int = "123"
parttern: r"^\d+$" #("Match, una, o, più, cifre, solo, numeri, interi, positivi")
result = re.match(r'^\d+s', text)
print(result)

# Modifica la RegEx per accettare anche numeri negativi.
text:int = "-45"
parttern: r"^-?\d+$" #("-? rende il segno meno opzionale, permette numeri negativi e lo zero") 
result = re.match(r'^-?\d+s', text)
print(result) 
 
 

