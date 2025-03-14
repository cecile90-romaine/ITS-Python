# esercizio_6. Calcolo del fattoriale di un numero
"""
Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente."""


# inserire un numero intero positivo

while True:
    n:int = int(input("inserisci un numero intero positico: "))
    if n % 1 == 0 and  n > 0:
        break
    print("il numero deve essere intero positivo")

# calcolo del fattoriale usando il ciclo for
fattoriale = 1

for i in range(1, n + 1):
    
    fattoriale *= i
    # stampa il risultato
print(f" il fattoriale di  {n} è:  {fattoriale} ")



         


