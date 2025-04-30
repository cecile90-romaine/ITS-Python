# 1
""""

Qual è il valore delle seguenti espressioni booleane se x vale 5, y vale 10 e z vale 15?

a. (x < 5 AND y > x)
b. (x < 5 OR y > x)
c. (x > 3 OR y < 10 AND z == 15)
d. (NOT(x > 3) AND x != z OR x + y == z)  ,m
Question 1 Answer
a.

a) False, b) False, c) True, d) True
b.

a) False, b) True, c) False, d) True        # risposta giusta
c.

a) False, b) True, c) True, d) True
d.

a) True, b) False, c) False, d) True """


# question: 2
""" 

Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

For example:
Test 	Result

print(transform(4))

2

print(transform(-10))

-5
"""
def transform(x: int) -> int:
    x1 = 4
    x2 = 3
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 - 1
print(transform(4))
print(transform(-10))

# question 3
"""
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

For example:
Test 	Result

print(calcola_stipendio(40))

	400.0

print(calcola_stipendio(0))

	0.0

"""
def calcola_stipendio(ore_lavorate: int) -> float:
    paga_oraria = 10
    ore_extra = 0
    
    if ore_lavorate > 40:
        ore_extra = ore_lavorate - 40
        stipendio = (40 * paga_oraria) + (ore_extra * paga_oraria * 1.5)
    else:
        stipendio = ore_lavorate * paga_oraria
    
    return stipendio
print(calcola_stipendio(40))
print(calcola_stipendio(0))

# question 4
"""
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51
"""

def print_seq(): 
    
    
    print("Sequenza a):")
    for i in range(1, 8):
        
        print(i)
    print()

    print("Sequenza b):")
    i = 3
    while i <= 23:
        
        print(i)
        i += 5
    print()

    print("Sequenza c):")
    i = 20
    while i >= -10:
        
         print(i)
         i -= 6
         
    print()

    print("Sequenza d):")
    i = 19
    while i <= 51:
        
        print(i)
        i += 8
    print()
    
print_seq()

# question: 5
"""
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!

For example:
Test 	Result

print(integerPower(3, 4))

	81

print(integerPower(2, 5))

	32

"""
def integerPower(base: int, exponent: int):
    result = 1
    for i in range(exponent):
        
        result *= base
    return result
    print("final result",integerpower(3, 4))
print(integerPower(3, 4))
print(integerPower(2, 5))

# question:6
"""
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.


Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

For example:
Test 	Result

print(hypotenuse(3.0, 4.0))

	5.0

print(hypotenuse(8.0, 15.0))

	17.0

"""
def hypotenuse(lato_1: float, lato_2: float) -> float:
    squares = [lato_1**2, lato_2**2]
    sum_of_squares = 0.0
    for square in squares:
        sum_of_squares += square
    return sum_of_squares ** 0.5
print(hypotenuse(3.0, 4.0))
print(hypotenuse(8.0, 15.0))

#question:7

"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

For example:
Test 	Result

print(remove_elements({5, 6, 7}, [7, 8, 9]))

	{5, 6}

"""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for numero in elements_to_remove:
        if numero in original_set:
            original_set.remove(numero)
    return(original_set)
print(remove_elements({5, 6, 7}, [7, 8, 9]))

#question:8
"""

Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

For example:
Test 	Result

print(time_difference(1, 0, 0, 3, 15, 30))

	8130

print(time_difference(0, 0, 0, 12, 0, 0))

	43200
"""
def seconds_since_noon(ore, minuti, secondi):
    if ore == 12:
        ore = 0
    return ore * 3600 + minuti * 60 + secondi

def time_difference(h1, m1, s1, h2, m2, s2):
    t1 = seconds_since_noon(h1, m1, s1)
    t2 = seconds_since_noon(h2, m2, s2)
    
    return abs(t2 - t1) % 43200 or 43200
print(time_difference(1, 0, 0, 3, 15, 30))
print(time_difference(0, 0, 0, 12, 0, 0))

# question;9

"""
Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"

 """   
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        tempo += 1
        altezza += velocita
        velocita -= 96

        if altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1
            
        print(f"Tempo: {tempo} Altezza: {altezza}")
rimbalzo()

#question:10

"""
Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."

Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

For example:
"""
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    for i in files:
        compressa = i * 0.8
        blocchi = round(compressa / 512)
        if blocchi <= blocchi_disponibili:
            blocchi_disponibili -= blocchi
memorizza_file([1100, 20000, 1048576, 512, 5000])        




