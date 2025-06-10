import string

def count_unique_words(text: str) -> dict:
    parole = text.split()  # Suddivide per spazi bianchi
    frequenze = {}
    
    for parola in parole:
        # 1. Converti in minuscolo
        parola_norm = parola.lower()
        # 2. Rimuovi punteggiatura iniziale e finale
        parola_norm = parola_norm.strip(string.punctuation)
        
        # Ignora parole vuote
        if parola_norm:
            if parola_norm in frequenze:
                frequenze[parola_norm] += 1
            else:
                frequenze[parola_norm] = 1
    
    return frequenze
text= "Hello, world! Hello... PYTHON? world."
risult = count_unique_words(text)
print(risult)