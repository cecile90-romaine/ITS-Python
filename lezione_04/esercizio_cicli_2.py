

"""def calculate_average(numbers: list[int]) -> float:
    
    if len(numbers) == 5:
        return sum(numbers) / len(numbers)
    else:
        return 0
print(calculate_average([1, 2, 3, 4, 5]))
print(0)"""


"""
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se 
entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

For example

def check_combination(A:bool, B:bool, C:bool) ->str:
    if A == A:
        return f" operazione permessa"
    
    else:
        return f"operazione  non permessa"
A = True
B = False
C = False
print(A)
print(B)
print(C)"""
 
"""

Scrivi una funzione che somma tutti i numeri interi
 di una lista che sono maggiori di un dato valore intero definito threshold


"""




"""
def sum_above_threshold(numbers: list[int], threshold:int) -> int:
    numbers:list = [15, 5, 25]
    threshold:int = 20
    for i in numbers :
        if i > threshold:
            return i
    else:
        return sum(numbers + 1)
        
print(sum_above_threshold([15, 5, 25], 20))"""




""""   
La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.


"""
def find_element(lst: list[int], element: int) -> bool:
    lst: list[1, 2, 3, 4, 5]
    element:int = 2
    for item in lst:
        if item == element:
            return True
        else:
            return False
        
        