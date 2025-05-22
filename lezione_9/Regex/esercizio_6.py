# Esercizio_6:Codice personalizzati.
'''
Obiettivo: Unire lettere, numeri e caratteri speciali.

    Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.
    Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere lettere maiuscole e numeri (es. AB12CD34).

'''
# Esercizio 6.1
text: str = "PROD-1234-XY"
result:list[str] = r'^PROD-\d{4}-[A-Z]{2}$'# (Formato specifico: quattro cifre e due lettere maiuscole)
print(result)

# Esercizio 6.2
^[A-Z0-9]{8}$ (Otto caratteri, solo lettere maiuscole e cifre)