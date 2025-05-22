# Esercizio_3:Email semplici.
'''
Obiettivo: Definire pattern per email.

    Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.
    Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.

'''
# Esercizio3.1
import re
text:str = "My email is nome@dominio.com"
result:list[str] = re.findall(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$', text) #"Accetta email nel formato base. Si possono aggiungere restrizioni per maggiore precisione")
print(" my email is", text)

# Esercizio3.2
text:str = "nome@dominio.co.uk "
result:list[str] = re.findall(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}(?:\.[a-z]{2,})?$', text) #"Accetta anche domini con doppia estensione, esempio .co.uk")
print("my email extension is", text)