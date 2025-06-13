# esercizio_2:
"""
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.

"""

def filter_positive_negative(list_1:list) -> dict:
    dict_1 = {"positivi":[], "negativi":[]}
    for element in list_1:
        if element >= 0:

            dict_1["positivi"].append(element)
        else:
            dict_1["negativi"].append(element)
    return dict_1

lista_3: list = [-2, 1, 4, -7, -9]

dict_3:dict = filter_positive_negative(list_1 = lista_3)

print(f"la soluzione dell' esrcizio2 è:{dict_3}")
