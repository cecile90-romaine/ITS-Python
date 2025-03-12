#  esercizio_7 Conta i numeri pari e dispari
"""
Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari."""

pari = 0

dispari = 0
cont = 0
# ciclo per 10 iterazioni
for cont in range(10):
    
    n = int( input(" inserisce un numero: "))  # leggi il numero
    
    if n % 2 == 0:  # controlla se è pari
        
        pari == pari + 1
    else:
        dispari += 1
        # stampa i risultati
print(f"Numeri pari inseriti:  {pari}")
print(f"Numeri dispari inseriti:  {dispari}")
