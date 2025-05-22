# Esercizio: Sistema di Gestione Biblioteca
"""
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e 
restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri 
al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Codice Driver

    Aggiungi libri alla biblioteca.
    Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
    Mostra i libri disponibili in ogni fase.
    Visualizza lo stato finale di ogni libro.

"""

class Libro:
    def __init__(self) -> None:
        self.setLibro()
    def getLibro(self) -> dict[str, list[str]]:
        return self.libro
    def setLibro(self) -> None:
        self.libro:dict[str, list[str]] = {}
    def __str__(self) -> str:

        string:str = "Libro"
        
        

            