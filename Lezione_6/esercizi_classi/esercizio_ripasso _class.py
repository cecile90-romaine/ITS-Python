# esrcizio_ ripasso _classe:

"""
sistema per gestire una biblioteca

"""
class Libro:
    def __init__(self):
        self.tittolo:str = ""
        self.autore:str = ""
        self.genere:list= []
    def set_autore(self, nome_autore:str):   # set per assegnare un attribuito a la mia classse.
        self.autore = nome_autore  

    def set_titolo(self, titolo_libro:str):
        self.titolo = titolo_libro
    
    def set_genere(self, lista_genere:list[str]):
        self.genere = lista_genere

    def get_titolo(self) -> str:
        return self.titolo 
    
    def get_autore(self) -> str:
        return self.autore
    
    def get_genere(self) -> list[str]:
        return self.genere
    

class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []
    
    def set_libro(self, libro:Libro):
        (self.libri).append(libro)

    def get_libri_titolo(self) -> str:
        for item in self.libri:
            print(item.get_titolo())
        
collezione:Biblioteca = Biblioteca() # oggetto vuoto
print("Biblioteca creata")

piccolo_principe:Libro = Libro() # libro 1
piccolo_principe.set_titolo("Piccolo principe")
piccolo_principe.set_autore("AutorePiccoloPrincipe")
piccolo_principe.set_genere(["Narrativa"])
print(piccolo_principe.get_titolo(), piccolo_principe.get_autore(), piccolo_principe.get_genere())


fm:Libro = Libro() # libro 2
fm.set_titolo("le avventure di Federico March")
fm.set_autore("Federico March")
fm.set_genere(["comico", "dramma"])
print(fm.get_titolo(), fm.get_autore(), fm.get_genere())

# inserimento libro 1 e libro 2 nella biblioteca
collezione.set_libro(piccolo_principe)
collezione.set_libro(fm)
print("aggiumngi libri nella collezione")
print("----------------------")
collezione.get_libri_titolo()

test:Libro = Libro()
test.set_titolo("Harry Potter")
test.set_autore("JK Rowling")
test.set_genere(["Fantasie"])

collezione.set_libro(test)
print("------------------")
collezione.get_libri_titolo()
        



        