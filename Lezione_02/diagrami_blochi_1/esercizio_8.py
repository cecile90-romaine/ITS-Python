# esercizio_8 Trovare i numeri maggiori di un valore soglia
"""
Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.

"""
# leggi il valore della soglia

soglia = float(input("inserisci il valore della soglia: "))
# iterazione per 7 volte

for cont in range(7):
    #leggi il numero
    n = float(input("inserisci un numero: "))
    # stampa il numero se è maggiore della soglia
    if n > soglia:
        print(f"numero maggiore della soglia: {n}")