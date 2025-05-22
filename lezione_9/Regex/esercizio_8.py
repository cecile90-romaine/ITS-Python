# Esercizio_8:Errori comuni
'''
Obiettivo: Trovare errori in RegEx sbagliate.
    Esercizio 8.1: Qual è l’errore nella RegEx ^\d{2,5}?$ se voglio matchare da 2 a 5 cifre?
    Esercizio 8.2: La RegEx [A-z] funziona per lettere? Perché può essere rischiosa?


''' 
# Esecrcizio 8.1
^\d{2,5}?$
Errore: il punto interrogativo dopo le graffe ({2,5}?) attiva la modalità lazy, che non è utile in questo caso.
Corretto: ^\d{2,5}$
# Esercizio 8.2
[A-z]
Errore: questa include anche caratteri non alfabetici come [, \, ], ^, _
Corretto: usare [A-Za-z] oppure [a-zA-Z] per solo lettere.
