
# esercizio3c_10

giorno = int(input(" inserisce un giorno: "))
mese = int(input("inserisce un mese: "))
data = (giorno,mese)

match data:
    case (1,1):
        print(f"{giorno}/{mese} è Capodanno! ")
    case (14,2):
        print(f"{giorno}/{mese} è San Valentino! ")
    case (2,6):
        print(f"{giorno}/{mese} è Festa della Repubblica Italiana ")
    case (15,8):
        print(f" {giorno}/{mese} è Ferragosto ")
    case (31,10):
        print(f" {giorno}/{mese} è Halloween ")
    case (25,12):
        print(f" {giorno}/{mese} è  Natale")
    case _:
        print(f"{giorno}/{mese} Nessuna festività importante in questa data.")

 
   