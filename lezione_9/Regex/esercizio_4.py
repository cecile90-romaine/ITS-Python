# Esercizio_4:  CAP e codici.
'''
Obiettivo: Lavorare con lunghezze fisse e caratteri misti.

    Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).
    Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 6 lettere, 2 numeri, 1 lettera, 2 numeri.

''' 
# Esercizio 4.1
import re
text: str = " 00058 "

# Esercizio 4.1
parttern: r"^\d{5}$" # (Esattamente 5 cifre, tipico CAP italiano)
result:list[str] = re.findall(r'^\d{5}$', text)
print(" il CAP di Santa Marinella è", text)

# Esercizio 4.1.
text:str = " MBZKOCR90N30 "

parttern:r" ^[A-Z]{6}\d{2}[A-Z]\d{2}$" #( Esempio semplificato di codice fiscale italiano)
result:list[str] = re.findall(r'^[A-Z]{6}\d{2}[A-Z]\d{2}}$', text)
print("il codice fiscale italiano è", result)

