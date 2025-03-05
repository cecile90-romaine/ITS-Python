# esercizio_4. Controllo della parità di un numero

"""Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari."""

#leggi un numero dall'utente
n = int(input (" inserisce un numero:"))

# controllo se il numero è pari o dispari
if n % 2 == 0:
    print("il numero è pari")
else:
    print("il numero è dispari")
