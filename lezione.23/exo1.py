def inverti_mappa(dizionario):
    invertito = {}
    for chiave, valore in dizionario.items():
        if valore not in invertito:
            invertito[valore] = chiave
    return invertito


print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))


print(inverti_mappa({}))


def somma_condizionale(numeri: list[int]) -> int :
    somma = 0
    numeri:list = [1, 2, 3, 6, 12]
    for numero in numeri:
        if numero % 2 == 0 and numero % 3 == 0:
            somma += numero
    return somma

print(somma_condizionale([1, 2, 3, 6, 12]))

print(somma_condizionale([5, 7, 11]))



def rimuovi_elementi(lista, da_rimuovere):
    risultato = []
    for elemento in lista:
        if elemento not in da_rimuovere:
            risultato.append(elemento)
    return risultato
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))  # [1, 3, 4]
print(rimuovi_elementi([], {2: 1}))     
         # []




def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int, int]) -> list[int]:
    nuova_lista: list[int] = []
    for i in lista:
        if i not in da_rimuovere:
            nuova_lista.append(i)
    return nuova_lista   
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))      



def aggrega_voti(lista):
    risultato = {}
    for d in lista:
        nome = d['nome']
        voto = d['voto']
        if nome in risultato:
            risultato[nome].append(voto)
        else:
            risultato[nome] = [voto]
    return risultato

def aggrega_voti(voti: list[dict]) -> dict[str, list[int]]:
    aggregazione = {}
    for i in voti:
        nome = i["nome"]
        voto = i["voto"]
        if nome in aggregazione:
            aggregazione[nome].append(voto)
        else:
            aggregazione[nome] = [voto]
    return aggregazione
print(aggrega_voti([
    {'nome': 'Alice', 'voto': 90},
    {'nome': 'Bob', 'voto': 75},
    {'nome': 'Alice', 'voto': 85}
]))
# Output: {'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([]))
# Output: {}


def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contact:dict = {"name":name,
        "email":email,
        "telefono": telefono
    }
    return contact

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if dictionary["name"] == name: 
        if email:
            dictionary["email"] = email
        if telefono:
            dictionary["telefono"] = telefono
    else:
        print("contact non trovato!")
    return dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))