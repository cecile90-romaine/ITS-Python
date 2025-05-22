# Esercizio_5:Riconoscere date.
'''
Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

    Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
    Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.

'''
# Esercizio 5.1
text:str =  "09/04/2025"

result:list[str] = r'^\d{2}/\d{2}/\d{4}$'#(Formato gg/mm/aaaa)
print(" la data è ", result )

# Esercizio 5.2
text:str = "09-04-2025"
result:list[str] = r' ^\d{2}[-/]\d{2}[-/]\d{4}$' # (Accetta sia / che - come separatori)
print("altro formato è", result)
  