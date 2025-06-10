# esercizio_2:
"""
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
"""

from typing import Union


def product(lista_interi: list[Union[int, float]], soglia: int = 50) -> int:
    prodotto_cumulato: int = 1
    for element in lista_interi:

        if type(element) != int:

            continue
        if element < soglia:
            prodotto_cumulato *= element

        
    return prodotto_cumulato
        

print(product([10, 3.12, 40, 20, 30, 1]))

    
