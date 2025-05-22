from media import Media


class Movie(Media):
    """
   attribuiti della superclasse Media
   sel.title: str
   self.year: int


   attribuiti della classe Movie 
   self.durata: int 
     
    """
     # inizializzare un oggetto della classe  Movie
    def __init__(self, title: str, year:int, durata: int) -> None:
        # iniziazzo la superclasse richimando il metodo  __init__ della  superclasse Media
        super().__init__(title, year)
        self.setDurata(durata)

        # metodi setter
    def setDurata(self, durata: int) ->None:
        if durata >= 0:
            self.durata = durata
        else:
            print("Errore")

    # metodi getter
    def getDurata(self) -> int:
        return self.durata
    
    # overrinding -> nella classe figlia Movie ridefinire il metodo __str__
    def __str__(self) -> str:
        return f"{super.__str__()}\nDurata:{self.getDurata()}"
    
    
        
""" da scrivere dentro un codice test.py
    film1: MOìovie = Movie(..., ..., ....)
    isistance( film1, Movie) -> True 
    isistance(film1, Media) -> True """