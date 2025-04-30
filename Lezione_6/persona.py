class Persona:
    """
   Di una persona  dobbiamo sappere delle informazioni.
   queste inforrazioni vengono chiamate attribuiti (della classe ) 
   le informazioni sarranno
   - nome
   -cognome
   - età
come gli rappresenziamo in python

self.name:str (attribuito di tipo stringa)
self.lastname: str (attribuito di tipo stringa)
self.age: str (attribuito di tipo int)

    
    """
    # costruzione

class Persona:
    def __init__(self,name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age