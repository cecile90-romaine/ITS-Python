"""
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico


"""

oggetti = [ ] 

for i in range(3):
    oggetto:str = str(input(f"inserire un oggetto: "))
    oggetti.append(oggetto)
print(oggetti)

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico  " )
    case ["pane", "latte", "uova"]:
        print("prodotti alimentari: ") 
    case ["sedia", "tavolo", "armadio"]: 
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettrici: ")
    case _:
        print("categoria sconosciuta: ")