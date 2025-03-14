#esercizio_2. Trova il massimo tra 4 numeri:
"""
Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.
"""

# while
# leggi il primo valore
max_value = float( input ("inserisce il primo numero: "))
cont = 1

while cont < 4:
    cont+= 1 # incrementa il contatore
    n = float(input (" inserisce un numero: ")) # leggi il numero
    if n > max_value:  # controlla se è maggiore
        max_value = n
print(" il massimo valore è:" , max_value)



#REPEAT
# leggi il primo valore
max_value = float(input (" inserisce il primo numero: "))
cont = 1

while True:
    n = float(input (" inserisce un numero: "))
    if n > max_value:  # controlla se è maggiore
        max_value = n
    cont += 1 # incrementa contatore
    if cont == 4: # condizione di uscita
        break
print("il massimo valore è:", max_value)

#ciclo for
# leggi il primo valore
max_value = float(input ("inserisce il primo numero: "))
for i in range():  #il ciclo si repete 3 volte
    n = float(input ("inserisce un mumero: "))
    if n > max_value:  #controlla se è maggiore
        max_value = n
print("il massimo valore è:", max_value)

