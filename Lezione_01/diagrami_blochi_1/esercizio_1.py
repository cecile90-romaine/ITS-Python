#esercizio_1. Calcolo cateto di un triangolo rettangolo:

"""Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, 
conoscendo quelle dell’ipotenusa a e dell’altro cateto b.
"""
# Il controllo che verifica se a > b è necessario per evitare di calcolare la radice quadrata 
# di un numero negativo, che porterebbe a un errore matematico se ci si limita ai numeri reali. Se a < b, 
# il risultato di (a2 - b2) sarebbe negativo, il che renderebbe impossibile calcolare la radice quadrata nei numeri reali. 
# Non c'è errore se a == b, ma il controllo è stato implementato con a > b per evitare il caso specifico di √0 = 0​.


#leggi a e b

a = float(input ("inserisci il valore di a: "))
b = float(input ("inserisci il valore di b: "))

#controlla la condizione a > b

if a > b:
    c = (a**2 - b**2) ** (1/2)
    print("il valore di c è:", c)
else:
    print("errore")

