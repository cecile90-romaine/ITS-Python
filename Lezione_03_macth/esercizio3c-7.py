# esercizio3c-7.py
i:int = 1
testa = 0
croce = 0

for i in range(8):
    moneta:str = str(input(f"Lancio {i +1 }: "))
    match moneta:
        case "t"|"T":
            testa +=1
        case "c"|"C":
            croce +=1
        case _:
            print("Scelta non valida")

percentuale_testa: float = (testa *  100) /(8)
percentuale_croce: float = (croce * 100) / (8)
print(f"\nlanci validi: {8}")
print(f"\nTotale 'testa' {testa}")
print(f"\nPercentuale 'testa': {percentuale_testa:2f}%")
print(f"\nTotale 'croce': {croce}")
print(f"percentuale 'croce': {percentuale_croce:2f}%")



