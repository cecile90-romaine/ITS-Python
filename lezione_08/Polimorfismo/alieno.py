class Alieno:

    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("errore la galassia di provinienza non può essere stringa vuota")
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("efrgsnfmjlse") 

    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia{self.getGalaxy()}"