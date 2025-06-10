# ricerca binaria:
def ricerca_binaria( lista:list, numero:int ) -> bool:
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


