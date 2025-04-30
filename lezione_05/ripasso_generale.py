
# esercizio_ simulazione: La tartaruga e la lepre.

import random
import time

# visualizzare lo stato della corsa


    # creare la lista dei 70 posti
percorso:list = ["quadrato 1"] 
x = len(percorso)
    # controllo il valore di x
print(x)
while x <= 70:
        n = x
        y = f"quadrato{n}"
        percorso.append(y)
        x+=1
        print(percorso)

        # percentuale delle mosse
def mossa_T():
     mossa = random.randint(1, 10)
     if mossa <= 1:
    
      return 3 # passo veloce

def posizione(posizione_T, posizione_l):
   # posizione_T
   
    if posizione_T <= 70:
        percorso[posizione_T - 1] = "T"

        # posizione_l
    if posizione_l <= 70:
        if posizione_T ==posizione_l:
             percorso[posizione_l- 1] = "OUCH"
    else:
        percorso[posizione_l- 1] = "H"
    print(" ".join(percorso))




