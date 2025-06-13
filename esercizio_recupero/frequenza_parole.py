import string

def parola_unica(testo: str) -> dict:
    parole = testo.split()  # Suddivide per spazi bianchi
    frequenze = {}
    
    for parola in parole:
        # 1. Converti in minuscolo
        parola_nor = parola.lower()
        # 2. Rimuovi punteggiatura iniziale e finale
        parola_nor = parola_nor.strip(string.punctuation)
        
        # Ignora parole vuote
        if parola_nor:
            if parola_nor in frequenze:
                frequenze[parola_nor] += 1
            else:
                frequenze[parola_nor] = 1
    
    return frequenze
text= "Hello, world! Hello... PYTHON? world."
risult = parola_unica(text)
print(risult)