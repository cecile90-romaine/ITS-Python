
"""
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido
 
"""

voto: int = int(input("inserire un numero: "))

match voto:
    case voto if 106 <= voto and voto <= 110:
        print("voto è\n 4.0") 
    case voto if 101 <=  voto and voto <= 105:
        print(" voto è\n 3.2")
    case  voto if 96 <= voto and voto <= 100:
        print("voto è\n 3.3")
    case voto if 91 <= voto and voto <= 95:
        print("voto è 3.0")
    case voto if 86 <= voto and voto <= 90:
        print(" il voto è 2.7")
    case voto if 70 <= voto and voto <= 75:
        print("il voto è 1.7")
    case voto if 66 <= voto and voto <= 69:
        print("il voto è 1.0")
    case _:
        print("voto non valido")