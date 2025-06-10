#Esercizio 1_3:
"""
Si scriva un programma che legge tre numeri interi e visualizza la media dei tre numeri.

"""
x = int(input("inserisci il primo numero "))
y = int(input("inserisci il secondo numero "))
z = int(input("inserisci il terzo numero "))

media:float = (x + y + z)/3
print(f"Media di 3 numeri inseriti è {media:.1f}")