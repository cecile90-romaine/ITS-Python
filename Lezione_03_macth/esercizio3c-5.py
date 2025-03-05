# esercizio3c-5
nome:str = str(input("inserire un nome: "))
ruolo:str = str(input("inserire un ruolo: "))
età:int = int(input("inserire l'età: "))
utente:dict ={"nome": nome, "ruolo": ruolo, "età": età}

print(utente)

match utente:
    case {"nome":nome, "ruolo":"admin", "eta": età}:
        print(f"{nome},{ ruolo},{età}  completo a tutte le funzionalità.") 
    case {"nome":nome, "ruolo":"Moderatore", "età": età}:
        print(f" {nome}, {ruolo},{età} Può gestire i contenuti ma non modificare le impostazioni.")
    case {"nome":nome, "ruolo":"Utente adulto(età>=18)", "età":età}:
        print(f" {nome}, {ruolo},{età} Accesso standard a tutti i servizi. ")
    case {"nome": nome, "ruolo":"Utente minorene(eta<18)", "età":età}:
        print(f"{nome},{ruolo}, {età} Accesso limitato! Alcune funzionalità sono bloccate ")
    case {"nome": nome, "ruolo": "Ospite", "età":età}:
        print(f"{nome},{ruolo},{età} Accesso ristretto! Solo visualizzazione dei contenut ")
    case _:
        print(f"{nome},{ruolo},{età}, Attenzione! Ruolo non riconosciuto! Accesso Negato!" )


    


  