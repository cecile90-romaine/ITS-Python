# ricerca binaria:

"""
mplementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.

"""

def ricerca_binaria(lista:list[int], numero:int ) -> bool:
    numeri = []


    if numero in lista:
        return True
    else:
        return False
    
lista = [2, 4, 6, 8, 10]

ricerca1 = ricerca_binaria(lista, 8)
print(f"8 trovato", ricerca1)
ricerca2 = ricerca_binaria(lista, 3)
print(f"3 tovato", ricerca2)



# corezione:
# l = [ 1, 2, 4, 6, 10, 15, 20] # è ordinata

def bin_search( lista: list[int], numero: int) -> None:
    mid: int = len(lista) // 2
    if lista[mid] == numero:
        print("il numero è stato trovato")
    elif len(lista) == 1:
        print("il numero non trovato")
    elif lista[mid] < numero:
        bin_search(lista[mid + 1], numero)

    elif lista[mid] > numero:
        bin_search(lista[mid:], numero)
            

