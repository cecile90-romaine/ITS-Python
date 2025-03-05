# Esercizio 3C-4.
animale:str = str(input("inserisce un animale: "))

mammiferi:list =["cane", "gatto", "cavallo", "elefante", "leone" ]
rettili:list =[ "serpente", "lucertola", "tartaruga", "coccodrillo"]  
uccelli: list = ["aquila", "pappagallo", "gufo", "falco."]
pesci: list =["squalo", "trota", "salmone", "carpa"]

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi!: ")
    case animale if animale in rettili:
        print(f"{animale}  appartiene alla categoria dei Rettil!: ")
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria degli Uccelli!: ")
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria dei Pesci!: ")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale{animale} ") 