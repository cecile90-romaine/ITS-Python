class Media:
    """
    Attribuiti  della classe Media
    self.title: str
    self.year: str
    
    """
    # inizializzara un oggetto della classe Movie
    def __init__(self, title: str, year:int) -> None:
        self.setTitle(title)
        self.setYear(year)


        # metodi setter

    def setTitle( self, title: str) -> None:
        if title:
            self.title = title
        else:
            print("Errore")
    def setYear(self, year:int) -> None:
        if year > 1000:
            self.year - year
        else:
            print("Errore")
    # metodi getter
    def getTitle(self) -> str:
        return self.title
    
    def getYear(self) ->int:
        return self.year 
    # metodi __str__
    def __str__(self) -> str:
        return f"Titolo: {self.getTitle()}\n anno:{self.getYear()}"
        
    


        