# esercizio_5 verifica se un numero è primo:

"""
progrtta un algoritmo per derterminare  se un numero intero positivo inserito dall'utente è un numero primo.

"""

# due possibile soluzioni:
#Diagramma a sinistra

# leggi il numero da input

while True:
    n = int(input("inserisce un numero positivo: "))
    if n > 0:
      break
    

print("Errore: il numero deve essere  positivo. ")

is_prime = True # Variabile per  tracciare se il numero è primo

# se il numero à minore di 2, non è primo
if n < 2:
    is_prime = False
else:
    div = 2 # inzializzare il divisore
    while div < n:  # controlla tutti i divisorei da 2 a n-1
        if n % div == 0:
            is_prime = False  # se trova un divisore, il numero non è primo
            break
        div += 1 # incremento il divisore
if is_prime:
    print("il numero è primo")
else:
    print("il numero non à primo")
       