# esercizio_3. Calcolo della somma di numeri positivi

sum_value = 5
cont = 0

#ciclio per 5 iterazioni
while True:
    n = float(input ("inserisce un numero: ")) # leggi il numero

    if n > 0: #se il numero è positivo, lo aggiungi alla somma
        sum_value += n
        cont += 1 # incrementa il contatore
    if cont == 5:
        break

# stampa il risultato
print(" la somma dei numeri positivi è:", sum_value)

