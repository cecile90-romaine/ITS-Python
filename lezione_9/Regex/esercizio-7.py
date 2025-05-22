# Esercizio_7:Comprensione di RegEx
'''
Data la RegEx, occorre interpretarla.

    Esercizio 7.1: Cosa fa questa RegEx? ^[A-Z][a-z]{2,}$
    Esercizio 7.2: Quali stringhe sono accettate da \d{3}-\d{2}-\d{4}?
    Esercizio 7.3: Qual è l’effetto del simbolo ? in questa RegEx: colou?r


'''
# Esercizio 7.1:
^[A-Z][a-z]{2,}$
Inizia con una lettera maiuscola, seguita da almeno due lettere minuscole → minimo 3 caratteri totali.
# Esercizio 7.2: \d{3}-\d{2}-\d{4}
Matcha stringhe nel formato 123-45-6789 .
# Esercizio 7.3: colou?r
Matcha sia color che colour (la “u” è opzionale grazie al simbolo ?)
